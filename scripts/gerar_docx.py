#!/usr/bin/env python3
"""
Gera uma petição .docx EDITÁVEL a partir de um arquivo Markdown.

Uso:
    python3 scripts/gerar_docx.py entrada.md saida.docx

Formatação (padrão forense do escritório):
- A4, margens ~2,5 cm
- Times New Roman 12, texto justificado, espaçamento 1,5
- Títulos (linhas iniciadas por # ou totalmente em CAIXA ALTA): negrito
- **negrito** inline suportado
- Tabelas em Markdown (| ... |) viram tabelas do Word (grade)
- Bloco de assinatura (linha com "OAB") centralizado

Se o python-docx não estiver instalado, o script tenta instalá-lo.
"""
import sys, re, subprocess

try:
    import docx
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "python-docx"], check=True)
    import docx

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_base_style(document):
    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    # garante a fonte também para caracteres especiais
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:ascii"), "Times New Roman")
    rfonts.set(qn("w:hAnsi"), "Times New Roman")
    pf = style.paragraph_format
    pf.line_spacing = 1.5
    pf.space_after = Pt(6)
    for section in document.sections:
        section.page_height = Cm(29.7)
        section.page_width = Cm(21.0)
        section.top_margin = section.bottom_margin = Cm(2.5)
        section.left_margin = section.right_margin = Cm(2.5)


def add_page_footer(document):
    """Rodapé 'Página X de Y', centralizado — padrão das peças do escritório."""
    footer = document.sections[0].footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.text = ""

    def field(instr):
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), instr)
        r = OxmlElement("w:r")
        fld.append(r)
        return fld

    run = p.add_run("Página ")
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    p._p.append(field(" PAGE "))
    run = p.add_run(" de ")
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    p._p.append(field(" NUMPAGES "))


BOLD_RE = re.compile(r"\*\*(.+?)\*\*")

# Títulos que identificam a espécie de peça — vão centralizados sob o
# endereçamento, como nas peças protocoladas do escritório.
TIPO_DE_PECA_RE = re.compile(
    r"^(RECLAMA(ÇÃO|TÓRIA) TRABALHISTA|RECURSO ORDINÁRIO|CONTESTAÇÃO|RÉPLICA|"
    r"EMBARGOS DE DECLARAÇÃO|AGRAVO DE PETIÇÃO|RECURSO DE REVISTA)$"
)
# Linha que qualifica o rito, logo abaixo do tipo de peça.
RITO_RE = re.compile(r"^(pelo|sob o) rito (ordinário|sumaríssimo|sumário)$", re.I)


def add_runs_with_bold(paragraph, text):
    """Adiciona texto a um parágrafo interpretando **negrito**."""
    pos = 0
    for m in BOLD_RE.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        run = paragraph.add_run(m.group(1))
        run.bold = True
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])


def is_heading(line):
    stripped = line.strip()
    if stripped.startswith("#"):
        return True
    letters = [c for c in stripped if c.isalpha()]
    # linha curta e majoritariamente em maiúsculas = título de tópico
    if letters and len(stripped) <= 120:
        upper = sum(1 for c in letters if c.isupper())
        if upper / len(letters) >= 0.85 and len(letters) >= 3:
            return True
    return False


def parse_table_block(lines, i):
    """Lê um bloco de tabela Markdown começando em lines[i]. Retorna (linhas_da_tabela, prox_i)."""
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw = lines[i].strip().strip("|")
        cells = [c.strip() for c in raw.split("|")]
        # ignora a linha separadora |---|---|
        if not all(set(c) <= set("-: ") for c in cells):
            rows.append(cells)
        i += 1
    return rows, i


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 gerar_docx.py entrada.md saida.docx")
        sys.exit(1)
    entrada, saida = sys.argv[1], sys.argv[2]
    with open(entrada, encoding="utf-8") as f:
        lines = f.read().split("\n")

    document = Document()
    set_base_style(document)
    add_page_footer(document)

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # tabela
        if stripped.startswith("|"):
            rows, i = parse_table_block(lines, i)
            if rows:
                ncols = max(len(r) for r in rows)
                table = document.add_table(rows=0, cols=ncols)
                table.style = "Table Grid"
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                for r, cells in enumerate(rows):
                    cells += [""] * (ncols - len(cells))
                    row_cells = table.add_row().cells
                    for c, val in enumerate(cells):
                        row_cells[c].paragraphs[0].text = ""
                        run = row_cells[c].paragraphs[0].add_run(val.replace("**", ""))
                        if r == 0:
                            run.bold = True
            continue

        # próxima linha não vazia (usada para reconhecer o bloco de assinatura)
        proxima = next((l.strip() for l in lines[i + 1:] if l.strip()), "")

        p = document.add_paragraph()
        text = re.sub(r"^#+\s*", "", stripped)

        # citação recuada: ementas, súmulas e doutrina marcadas com "> " no .md
        if stripped.startswith(">"):
            texto_citacao = re.sub(r"^>\s?", "", stripped)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf = p.paragraph_format
            pf.left_indent = Cm(4.0)
            pf.line_spacing = 1.0
            pf.space_before = Pt(6)
            pf.space_after = Pt(6)
            add_runs_with_bold(p, texto_citacao)
            for run in p.runs:
                run.font.size = Pt(10)
            i += 1
            continue

        if TIPO_DE_PECA_RE.match(text.replace("**", "")) or RITO_RE.match(text):
            # espécie da peça e rito: centralizados, a espécie em negrito
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text.replace("**", ""))
            run.bold = bool(TIPO_DE_PECA_RE.match(text.replace("**", "")))
        elif "OAB" in stripped or "OAB" in proxima:
            # bloco de assinatura: nome do advogado e linha da OAB
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text.replace("**", ""))
            run.bold = True
        elif stripped.lower() in (
            "termos em que, pede deferimento.",
            "termos em que pede deferimento.",
            "nestes termos, pede deferimento.",
        ):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_runs_with_bold(p, text)
        elif is_heading(line):
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text.replace("**", ""))
            run.bold = True
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_runs_with_bold(p, text)
        i += 1

    document.save(saida)
    print(f"OK: {saida}")


if __name__ == "__main__":
    main()
