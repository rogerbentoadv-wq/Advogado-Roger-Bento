#!/usr/bin/env python3
"""
Gera uma petição .docx EDITÁVEL a partir de um Markdown, replicando o padrão
das peças do escritório (calibrado sobre modelo real ROSELI DA ROSA SCRINZ).

Uso:
    python3 scripts/gerar_docx.py entrada.md saida.docx

Padrão aplicado:
- A4, margens 2,0 cm em todos os lados
- Times New Roman 12, JUSTIFICADO, entrelinha 1,5, sem espaço antes/depois
- Recuo de 1ª linha de 1,5 cm no corpo E nos títulos de tópico (títulos em negrito)
- Endereçamento (EXCELENTÍSSIMO/AO JUÍZO...): negrito, justificado, sem recuo
- "RECLAMAÇÃO TRABALHISTA" (linha isolada): centralizado, negrito
- Ementas/citações (linhas iniciadas por ">"): recuo à esquerda de 4 cm
- Listas: "- item" vira marcador (bullet Symbol) e "1. item" vira lista numerada,
  com recuo de 1,27 cm e deslocamento de 0,635 cm, como no modelo do escritório
- Cidade/data, nome do advogado e OAB: centralizados em negrito
- Separação entre blocos por linha em branco (preservada como parágrafo vazio)
- **negrito** inline; tabelas Markdown viram tabelas do Word

Instala o python-docx automaticamente se faltar.
"""
import sys, os, re, subprocess

try:
    import docx
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "python-docx"], check=True)
    import docx

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

FONTE, CORPO = "Times New Roman", 12
RECUO = Cm(1.5)
RECUO_EMENTA = Cm(4.0)
# Listas: mesmos valores do modelo real do escritório (720 e 360 twips)
LISTA_ESQ, LISTA_DESLOC = 720, 360

# Papel timbrado do escritório (logo no cabeçalho + barra de contato no rodapé).
# Procurado em assets/ na raiz do projeto (um nível acima de scripts/).
_ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
LOGO = os.path.join(_ASSETS, "logo-cabecalho.png")   # 5,97 x 3,49 cm
RODAPE = os.path.join(_ASSETS, "rodape.png")          # 17,0 x 2,64 cm


def add_papel_timbrado(document):
    """Adiciona logo (cabeçalho) e barra de contato (rodapé), se os arquivos existirem."""
    sec = document.sections[0]
    sec.header_distance = Cm(1.0)
    sec.footer_distance = Cm(1.0)
    if os.path.exists(LOGO):
        hp = sec.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        hp.paragraph_format.first_line_indent = Cm(0)
        hp.add_run().add_picture(LOGO, width=Cm(5.97))
        sec.header.is_linked_to_previous = False
    if os.path.exists(RODAPE):
        fp = sec.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.paragraph_format.first_line_indent = Cm(0)
        fp.add_run().add_picture(RODAPE, width=Cm(17.0))
        sec.footer.is_linked_to_previous = False

RE_ENDERECO = re.compile(r"^\s*(EXCELENT[IÍ]SSIM|EXM|AO JU[IÍ]ZO|MERIT[IÍ]SSIM)", re.IGNORECASE)
RE_TITULO = re.compile(r"^\s*RECLAMA(ÇÃO|CAO)\s+TRABALHISTA\s*$", re.IGNORECASE)
RE_CIDADE_DATA = re.compile(r"^\s*[\wÀ-ú\.\s]{2,40}/[A-Z]{2},\s*(data do protocolo|\d{1,2}\s+de\s+\w+\s+de\s+\d{4}|data\b).*$", re.IGNORECASE)
RE_OAB = re.compile(r"OAB", re.IGNORECASE)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
# itens de lista: "- item" (marcador) e "1. item" (numerada)
RE_ITEM_MARCADOR = re.compile(r"^\s*[-*\u2022]\s+(.*)$")
RE_ITEM_NUMERADO = re.compile(r"^\s*\d+[.)]\s+(.*)$")


def _font(run, size=CORPO, bold=False, italic=False):
    run.font.name = FONTE
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    rpr = run._element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), FONTE)


def set_base_style(document):
    st = document.styles["Normal"]
    st.font.name = FONTE
    st.font.size = Pt(CORPO)
    rf = st.element.get_or_add_rPr().get_or_add_rFonts()
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), FONTE)
    pf = st.paragraph_format
    pf.line_spacing = 1.5
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    for s in document.sections:
        s.page_height, s.page_width = Cm(29.7), Cm(21.0)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.0)


def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    return e


def nova_lista(document, formato="bullet"):
    """Cria uma definição de lista nova (marcador ou numerada) e devolve o numId.

    Cada bloco recebe a sua própria definição para que as listas numeradas
    recomecem em 1, como nas peças do escritório.
    """
    numbering = document.part.numbering_part.element
    usados_abs = [int(a.get(qn("w:abstractNumId")))
                  for a in numbering.findall(qn("w:abstractNum"))]
    usados_num = [int(n.get(qn("w:numId")))
                  for n in numbering.findall(qn("w:num"))]
    abs_id = max(usados_abs, default=-1) + 1
    num_id = max(usados_num, default=0) + 1

    abstract = _el("w:abstractNum", abstractNumId=abs_id)
    abstract.append(_el("w:multiLevelType", val="hybridMultilevel"))
    lvl = _el("w:lvl", ilvl=0)
    lvl.append(_el("w:start", val=1))
    lvl.append(_el("w:numFmt", val="bullet" if formato == "bullet" else "decimal"))
    lvl.append(_el("w:lvlText", val="" if formato == "bullet" else "%1."))
    lvl.append(_el("w:lvlJc", val="left"))
    ppr = OxmlElement("w:pPr")
    ppr.append(_el("w:ind", left=LISTA_ESQ, hanging=LISTA_DESLOC))
    lvl.append(ppr)
    if formato == "bullet":
        rpr = OxmlElement("w:rPr")
        rpr.append(_el("w:rFonts", ascii="Symbol", hAnsi="Symbol", hint="default"))
        lvl.append(rpr)
    abstract.append(lvl)

    ultimo_abs = numbering.findall(qn("w:abstractNum"))[-1]
    ultimo_abs.addnext(abstract)

    num = _el("w:num", numId=num_id)
    num.append(_el("w:abstractNumId", val=abs_id))
    numbering.append(num)
    return num_id


def aplica_lista(paragraph, num_id):
    """Vincula o parágrafo à definição de lista (marcador/numeração)."""
    numPr = OxmlElement("w:numPr")
    numPr.append(_el("w:ilvl", val=0))
    numPr.append(_el("w:numId", val=num_id))
    paragraph._p.get_or_add_pPr().insert(0, numPr)


VERMELHO = RGBColor(0xFF, 0x00, 0x00)
# tokens inline: **negrito** ou [placeholder a preencher/conferir]
TOKEN = re.compile(r"\*\*(.+?)\*\*|\[[^\]]*\]")


def add_runs(paragraph, text, size=CORPO, base_bold=False, italic=False):
    """Adiciona texto interpretando **negrito** e deixando [colchetes] em VERMELHO."""
    pos = 0
    added = False
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            _font(paragraph.add_run(text[pos:m.start()]), size=size, bold=base_bold, italic=italic)
        tok = m.group(0)
        if tok.startswith("**"):
            inner = m.group(1)
            r = paragraph.add_run(inner)
            _font(r, size=size, bold=True, italic=italic)
            if inner.strip().startswith("[") and inner.strip().endswith("]"):
                r.font.color.rgb = VERMELHO  # placeholder em negrito -> negrito + vermelho
        else:  # [ ... ] -> campo a preencher / conferir -> vermelho
            r = paragraph.add_run(tok)
            _font(r, size=size, bold=base_bold, italic=italic)
            r.font.color.rgb = VERMELHO
        pos = m.end()
        added = True
    if pos < len(text) or not added:
        _font(paragraph.add_run(text[pos:]), size=size, bold=base_bold, italic=italic)


def is_heading(s):
    if s.startswith("#"):
        return True
    letters = [c for c in s if c.isalpha()]
    return bool(letters) and len(s) <= 130 and len(letters) >= 3 and \
        sum(1 for c in letters if c.isupper()) / len(letters) >= 0.9


def parse_table(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not all(set(c) <= set("-: ") for c in cells):
            rows.append(cells)
        i += 1
    return rows, i


def next_nonempty(lines, i):
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    return lines[j].strip() if j < len(lines) else ""


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 gerar_docx.py entrada.md saida.docx"); sys.exit(1)
    entrada, saida = sys.argv[1], sys.argv[2]
    with open(entrada, encoding="utf-8") as f:
        lines = f.read().split("\n")

    doc = Document()
    set_base_style(doc)
    add_papel_timbrado(doc)
    pending_blank = False
    wrote = False
    lista_atual = None   # (formato, numId) do bloco de lista em curso

    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()

        if not s:
            pending_blank = True
            i += 1
            continue

        item_marcador = RE_ITEM_MARCADOR.match(s)
        item_numerado = None if item_marcador else RE_ITEM_NUMERADO.match(s)
        if item_marcador or item_numerado:
            formato = "bullet" if item_marcador else "decimal"
            texto = (item_marcador or item_numerado).group(1).strip()
            if pending_blank and wrote:
                doc.add_paragraph()
            pending_blank = False
            # linha em branco entre itens não quebra a lista; bloco novo, numeração nova
            if lista_atual is None or lista_atual[0] != formato:
                lista_atual = (formato, nova_lista(doc, formato))
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            # sem w:ind no parágrafo: os recuos vêm da definição da lista,
            # como nas peças reais do escritório
            aplica_lista(p, lista_atual[1])
            add_runs(p, texto)
            wrote = True
            i += 1
            continue
        lista_atual = None

        if s.startswith("|"):
            if pending_blank and wrote:
                doc.add_paragraph()
            pending_blank = False
            rows, i = parse_table(lines, i)
            if rows:
                ncols = max(len(r) for r in rows)
                t = doc.add_table(rows=0, cols=ncols)
                t.style = "Table Grid"
                t.alignment = WD_TABLE_ALIGNMENT.CENTER
                for r, cells in enumerate(rows):
                    cells += [""] * (ncols - len(cells))
                    rc = t.add_row().cells
                    for c, val in enumerate(cells):
                        para = rc[c].paragraphs[0]
                        para.paragraph_format.first_line_indent = Cm(0)
                        para.paragraph_format.line_spacing = 1.0
                        add_runs(para, val, size=11, base_bold=(r == 0))
                wrote = True
            continue

        if pending_blank and wrote:
            doc.add_paragraph()
        pending_blank = False

        p = doc.add_paragraph()
        pf = p.paragraph_format
        text = re.sub(r"^#+\s*", "", s)
        J, C = WD_ALIGN_PARAGRAPH.JUSTIFY, WD_ALIGN_PARAGRAPH.CENTER

        if RE_ENDERECO.match(s):
            p.alignment = J; pf.first_line_indent = Cm(0)
            add_runs(p, text, base_bold=True)
        elif RE_TITULO.match(text):
            p.alignment = C; pf.first_line_indent = Cm(0)
            add_runs(p, text, base_bold=True)
        elif RE_CIDADE_DATA.match(s) or RE_OAB.search(s) or (is_heading(s) and RE_OAB.search(next_nonempty(lines, i))):
            # bloco de assinatura: cidade/data, nome do advogado, OAB
            p.alignment = C; pf.first_line_indent = Cm(0)
            add_runs(p, text, base_bold=True)
        elif s.startswith(">"):
            p.alignment = J; pf.first_line_indent = Cm(0); pf.left_indent = RECUO_EMENTA
            add_runs(p, re.sub(r"^>\s?", "", s))
        elif is_heading(s):
            p.alignment = J; pf.first_line_indent = RECUO
            add_runs(p, text, base_bold=True)
        else:
            p.alignment = J; pf.first_line_indent = RECUO
            add_runs(p, text)
        wrote = True
        i += 1

    doc.save(saida)
    print(f"OK: {saida}")


if __name__ == "__main__":
    main()
