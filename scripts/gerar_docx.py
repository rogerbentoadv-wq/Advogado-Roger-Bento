#!/usr/bin/env python3
"""
Gera uma petição .docx EDITÁVEL e PADRONIZADA a partir de um arquivo Markdown.

Uso:
    python3 scripts/gerar_docx.py entrada.md saida.docx

Padrão forense aplicado (uniforme em toda a peça):
- A4, margens: esquerda 3 cm, direita/superior/inferior 2,5 cm
- Corpo: Times New Roman 12, JUSTIFICADO, espaçamento 1,5, recuo de 1ª linha 1,25 cm
- Títulos de tópico (linhas iniciadas por # ou em CAIXA ALTA): negrito, à esquerda,
  sem recuo, com espaço antes/depois
- "RECLAMAÇÃO TRABALHISTA" (e variantes) e o fecho/assinatura: centralizados
- Ementas/citações (linhas iniciadas por ">"): recuadas, itálico, corpo 11
- **negrito** inline suportado; tabelas Markdown viram tabelas do Word
- Nenhuma marcação de markdown deve sobrar visível no resultado

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
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

FONTE = "Times New Roman"
CORPO = 12
INDENT = Cm(1.25)

TITULO_ACAO = re.compile(r"^\s*RECLAMA(ÇÃO|CAO)\s+TRABALHISTA\s*$", re.IGNORECASE)
FECHO = re.compile(r"^\s*(nestes|termos em que)[,]?\s+.*pede deferimento\.?\s*$", re.IGNORECASE)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def _set_font(run, size=CORPO, bold=False, italic=False):
    run.font.name = FONTE
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:ascii"), FONTE)
    rfonts.set(qn("w:hAnsi"), FONTE)
    rfonts.set(qn("w:cs"), FONTE)


def set_base_style(document):
    style = document.styles["Normal"]
    style.font.name = FONTE
    style.font.size = Pt(CORPO)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:ascii"), FONTE)
    rfonts.set(qn("w:hAnsi"), FONTE)
    rfonts.set(qn("w:cs"), FONTE)
    pf = style.paragraph_format
    pf.line_spacing = 1.5
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)
    for section in document.sections:
        section.page_height = Cm(29.7)
        section.page_width = Cm(21.0)
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.5)


def add_runs_with_bold(paragraph, text, size=CORPO, italic=False):
    pos = 0
    any_run = False
    for m in BOLD_RE.finditer(text):
        if m.start() > pos:
            _set_font(paragraph.add_run(text[pos:m.start()]), size=size, italic=italic)
            any_run = True
        _set_font(paragraph.add_run(m.group(1)), size=size, bold=True, italic=italic)
        any_run = True
        pos = m.end()
    if pos < len(text):
        _set_font(paragraph.add_run(text[pos:]), size=size, italic=italic)
        any_run = True
    if not any_run:
        _set_font(paragraph.add_run(""), size=size, italic=italic)


def is_heading(line):
    s = line.strip()
    if s.startswith("#"):
        return True
    letters = [c for c in s if c.isalpha()]
    if letters and len(s) <= 130:
        upper = sum(1 for c in letters if c.isupper())
        if upper / len(letters) >= 0.9 and len(letters) >= 3:
            return True
    return False


def parse_table_block(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw = lines[i].strip().strip("|")
        cells = [c.strip() for c in raw.split("|")]
        if not all(set(c) <= set("-: ") for c in cells):  # ignora |---|---|
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

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        # Tabela
        if s.startswith("|"):
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
                        para = row_cells[c].paragraphs[0]
                        para.paragraph_format.first_line_indent = Cm(0)
                        para.paragraph_format.line_spacing = 1.0
                        run = para.add_run(val.replace("**", ""))
                        _set_font(run, size=11, bold=(r == 0))
            continue

        p = document.add_paragraph()
        pf = p.paragraph_format
        text = re.sub(r"^#+\s*", "", s)

        if TITULO_ACAO.match(text):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Cm(0)
            pf.space_before = Pt(12); pf.space_after = Pt(12)
            _set_font(p.add_run(text.replace("**", "")), bold=True)
        elif is_heading(line):
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pf.first_line_indent = Cm(0)
            pf.space_before = Pt(12); pf.space_after = Pt(6)
            _set_font(p.add_run(text.replace("**", "")), bold=True)
        elif s.startswith(">"):  # ementa / citação
            quote = re.sub(r"^>\s?", "", s)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.first_line_indent = Cm(0)
            pf.left_indent = Cm(4.0)
            pf.space_before = Pt(6); pf.space_after = Pt(6)
            add_runs_with_bold(p, quote, size=11, italic=True)
        elif FECHO.match(text) or "OAB" in s or re.match(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ\.\s]+/RS", s):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Cm(0)
            pf.space_before = Pt(6)
            add_runs_with_bold(p, text)
        else:  # corpo
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.first_line_indent = INDENT
            add_runs_with_bold(p, text)
        i += 1

    document.save(saida)
    print(f"OK: {saida}")


if __name__ == "__main__":
    main()
