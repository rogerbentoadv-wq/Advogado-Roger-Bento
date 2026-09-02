# -*- coding: utf-8 -*-
"""Estilo visual padrão dos painéis de números do escritório Róger Bento.

Este módulo é a base da skill `graficos-planilha`. Ele existe para que todo
painel gerado a partir de uma planilha saia com a mesma cara: mesma paleta,
mesma tipografia, mesmo cabeçalho com a logo, mesmas regras de rótulo.

Paleta e regras de forma seguem a metodologia de dataviz adotada no projeto
(ver `.claude/skills/graficos-planilha/references/formas-e-cores.md`):

- magnitude (comparar quem é maior)  -> UMA cor, escala clara->escura;
- identidade (séries diferentes)     -> paleta categórica em ordem fixa;
- nunca dois eixos Y no mesmo gráfico;
- texto sempre em tinta neutra, nunca na cor da série;
- número escrito na ponta da barra, não em cima de cada ponto de linha.
"""

from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from matplotlib.patches import FancyBboxPatch

# --------------------------------------------------------------------------
# Paleta (modo claro — painel é feito para imprimir e para mandar no WhatsApp)
# --------------------------------------------------------------------------

SUPERFICIE = "#fcfcfb"      # fundo do painel
CARTAO = "#f4f3f0"          # fundo dos cartões de KPI
TINTA = "#0b0b0b"           # texto primário
TINTA_2 = "#52514e"         # texto secundário
TINTA_3 = "#84837d"         # texto discreto (fonte, notas)
GRADE = "#e3e2dd"           # linhas de grade / eixos
VERMELHO = "#c2262a"        # regra da casa: pendência/conferência sai em vermelho

# Categórica (ordem fixa — nunca embaralhar, nunca gerar uma 9ª cor)
CATEGORICA = [
    "#2a78d6",  # 1 azul
    "#eb6834",  # 2 laranja
    "#1baf7a",  # 3 água
    "#eda100",  # 4 amarelo
    "#e87ba4",  # 5 magenta
    "#008300",  # 6 verde
    "#4a3aa7",  # 7 violeta
    "#e34948",  # 8 vermelho
]

# Sequencial de uma cor só (magnitude). Do mais claro utilizável ao mais escuro.
SEQUENCIAL = [
    "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
    "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281",
]

NEUTRO = "#c9c8c2"          # série de contexto (o "resto") quando há ênfase
DESTAQUE = "#2a78d6"        # a série que é o assunto
BOM = "#008300"
ATENCAO = "#eda100"
RUIM = "#c2262a"

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(RAIZ, "assets", "logo-cabecalho.png")
RODAPE = os.path.join(RAIZ, "assets", "rodape.png")


def aplicar_estilo() -> None:
    """Aplica a tipografia e os padrões de eixo do escritório."""
    plt.rcParams.update({
        "figure.facecolor": SUPERFICIE,
        "axes.facecolor": SUPERFICIE,
        "savefig.facecolor": SUPERFICIE,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Liberation Sans", "FreeSans"],
        "font.size": 10,
        "text.color": TINTA,
        "axes.labelcolor": TINTA_2,
        "axes.edgecolor": GRADE,
        "axes.linewidth": 0.8,
        "axes.grid": False,
        "xtick.color": TINTA_2,
        "ytick.color": TINTA_2,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.frameon": False,
        "legend.fontsize": 9.5,
    })


def limpar_eixo(ax, grade: str = "y") -> None:
    """Deixa só o essencial: sem moldura, grade discreta atrás dos dados."""
    for lado in ("top", "right", "left" if grade == "y" else "bottom"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom" if grade == "y" else "left"].set_color(GRADE)
    ax.tick_params(length=0)
    if grade:
        ax.grid(axis=grade, color=GRADE, linewidth=0.8, zorder=0)
        ax.set_axisbelow(True)


def titulo_do_grafico(ax, titulo: str, subtitulo: str = "", x: float = 0.0) -> None:
    """`x` em fração do eixo — use negativo para alinhar o título à margem do
    painel quando o gráfico tem rótulos longos no eixo Y."""
    ax.text(x, 1.20, titulo, transform=ax.transAxes, fontsize=12.5,
            fontweight="bold", color=TINTA, va="bottom", ha="left")
    if subtitulo:
        ax.text(x, 1.06, subtitulo, transform=ax.transAxes, fontsize=9.5,
                color=TINTA_2, va="bottom", ha="left")


# --------------------------------------------------------------------------
# Moldura do painel: cabeçalho com logo + rodapé de fonte/notas
# --------------------------------------------------------------------------

def novo_painel(titulo: str, subtitulo: str = "", tamanho=(12.6, 9.4), dpi=170):
    """Cria a figura já com o cabeçalho timbrado. Devolve (fig, gridspec_area)."""
    aplicar_estilo()
    fig = plt.figure(figsize=tamanho, dpi=dpi)

    fig.text(0.045, 0.955, titulo, fontsize=21, fontweight="bold",
             color=TINTA, va="top", ha="left")
    if subtitulo:
        fig.text(0.045, 0.914, subtitulo, fontsize=11.5, color=TINTA_2,
                 va="top", ha="left")

    if os.path.exists(LOGO):
        eixo_logo = fig.add_axes([0.80, 0.895, 0.155, 0.075])
        eixo_logo.imshow(mpimg.imread(LOGO))
        eixo_logo.axis("off")

    # régua fina separando o cabeçalho do conteúdo
    fig.add_artist(plt.Line2D([0.045, 0.955], [0.888, 0.888],
                              color=GRADE, linewidth=1.2))
    return fig


def cartao_kpi(fig, caixa, valor: str, rotulo: str, apoio: str = "",
               cor_apoio: str | None = None) -> None:
    """Cartão de número-síntese. `caixa` = [esq, base, larg, alt] em fração da figura.

    Um número grande vale mais que um gráfico de uma barra só — use isto para
    os totais do mês.
    """
    esq, base, larg, alt = caixa
    fig.patches.append(FancyBboxPatch(
        (esq, base), larg, alt, boxstyle="round,pad=0,rounding_size=0.010",
        transform=fig.transFigure, facecolor=CARTAO, edgecolor="none", zorder=0))
    fig.text(esq + 0.012, base + alt - 0.022, rotulo.upper(), fontsize=8.8,
             color=TINTA_2, va="center", ha="left", fontweight="bold")
    fig.text(esq + 0.012, base + alt * 0.50, valor, fontsize=24,
             fontweight="bold", color=TINTA, va="center", ha="left")
    if apoio:
        fig.text(esq + 0.012, base + 0.022, apoio, fontsize=9.2,
                 color=cor_apoio or TINTA_2, va="center", ha="left")


def nota(fig, texto: str, y: float = 0.045, cor: str = TINTA_3,
         tamanho: float = 9.0) -> None:
    """Rodapé de fonte/metodologia."""
    fig.text(0.045, y, texto, fontsize=tamanho, color=cor, va="center", ha="left")


def nota_conferir(fig, texto: str, y: float = 0.045) -> None:
    """Regra da casa: o que está pendente ou precisa de conferência sai em VERMELHO.

    Mesmo espírito dos colchetes vermelhos das peças — quem olha o painel vê
    na hora o que ainda não está fechado. Nunca 'chute' um número para tapar
    o buraco: marque aqui.
    """
    nota(fig, texto, y=y, cor=VERMELHO, tamanho=9.4)


def salvar(fig, caminho: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(caminho)), exist_ok=True)
    fig.savefig(caminho, facecolor=SUPERFICIE, bbox_inches=None)
    plt.close(fig)
    print(f"gerado: {caminho}")
    return caminho


# --------------------------------------------------------------------------
# Formas
# --------------------------------------------------------------------------

def escala_por_magnitude(valores):
    """Uma cor só, mais escuro = maior. Use sempre que o assunto for ranking."""
    if not valores:
        return []
    vmin, vmax = min(valores), max(valores)
    faixa = (vmax - vmin) or 1
    passo = len(SEQUENCIAL) - 1
    return [SEQUENCIAL[round((v - vmin) / faixa * passo)] for v in valores]


def barras_horizontais(ax, rotulos, valores, formato="{:,.0f}", cores=None,
                       destaque: int | None = None):
    """Ranking. Já vem ordenado por quem chama; rotula o valor na ponta da barra."""
    y = range(len(rotulos))
    if cores is None:
        cores = ([NEUTRO] * len(valores) if destaque is not None
                 else escala_por_magnitude(valores))
        if destaque is not None:
            cores[destaque] = DESTAQUE
    ax.barh(list(y), valores, color=cores, height=0.62, zorder=3)
    ax.set_yticks(list(y), rotulos)
    ax.invert_yaxis()
    limpar_eixo(ax, grade="x")
    ax.set_xlim(0, max(valores) * 1.18)
    ax.set_xticks([])
    ax.spines["left"].set_visible(True)
    ax.spines["left"].set_color(GRADE)
    for i, v in enumerate(valores):
        ax.text(v + max(valores) * 0.02, i, _pt(formato.format(v)),
                va="center", ha="left", fontsize=10, fontweight="bold",
                color=TINTA)


def _pt(texto: str) -> str:
    """Formata número no padrão brasileiro (1.234,5)."""
    return texto.replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def moeda(v: float, casas: int = 0) -> str:
    return "R$ " + _pt(f"{v:,.{casas}f}")


def numero(v: float, casas: int = 0) -> str:
    return _pt(f"{v:,.{casas}f}")


def percentual(v: float, casas: int = 0) -> str:
    """v em fração (0,25 -> 25%)."""
    return _pt(f"{v * 100:,.{casas}f}") + "%"


def tabela_barras(fig, caixa, nomes, colunas, largura_nomes: float = 0.235,
                  gap: float = 0.012):
    """Tabela-gráfico: uma linha por pessoa/item, uma coluna por indicador.

    É a forma certa quando há muitos itens (>7) e vários indicadores: repetir
    sete nomes em quatro gráficos separados cansa; aqui os nomes aparecem uma
    vez só e a comparação é imediata coluna a coluna.

    `caixa` = [esq, base, larg, alt] em fração da figura.
    `colunas` = lista de dicts: {"titulo", "valores", "formato" (opcional),
                "cor" (opcional, cor única no lugar da escala de magnitude)}.
    """
    esq, base, larg, alt = caixa
    n = len(colunas)
    larg_col = (larg - largura_nomes - gap * (n - 1)) / n
    y = list(range(len(nomes)))

    # faixas zebradas para o olho não pular de linha
    for i in y:
        if i % 2 == 0:
            fig.patches.append(plt.Rectangle(
                (esq, base + alt * (1 - (i + 1) / len(nomes))),
                larg, alt / len(nomes), transform=fig.transFigure,
                facecolor=CARTAO, edgecolor="none", zorder=-10))

    for i, nome in enumerate(nomes):
        fig.text(esq + 0.008,
                 base + alt * (1 - (i + 0.5) / len(nomes)),
                 nome, fontsize=10, color=TINTA, va="center", ha="left",
                 fontweight="bold")

    for j, col in enumerate(colunas):
        x0 = esq + largura_nomes + j * (larg_col + gap)
        ax = fig.add_axes([x0, base, larg_col, alt])
        ax.patch.set_alpha(0)
        valores = col["valores"]
        cores = ([col["cor"]] * len(valores) if col.get("cor")
                 else escala_por_magnitude(valores))
        ax.barh(y, valores, color=cores, height=0.45, zorder=3)
        ax.set_ylim(len(nomes) - 0.5, -0.5)
        ax.set_xlim(0, max(valores) * 1.55)
        ax.set_xticks([])
        ax.set_yticks([])
        for lado in ("top", "right", "left", "bottom"):
            ax.spines[lado].set_visible(False)
        formato = col.get("formato", numero)
        for i, v in enumerate(valores):
            ax.text(v + max(valores) * 0.06, i, formato(v), va="center",
                    ha="left", fontsize=10, fontweight="bold", color=TINTA)
        ax.text(0, 1.02, col["titulo"], transform=ax.transAxes, fontsize=10,
                fontweight="bold", color=TINTA_2, va="bottom", ha="left")
