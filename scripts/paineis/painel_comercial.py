# -*- coding: utf-8 -*-
"""Painel mensal de métricas comerciais (Previdenciário + Trabalhista).

Uso:
    python3 scripts/paineis/painel_comercial.py \
        dados/metricas-comerciais-2026.xlsx graficos/painel-comercial-agosto.png

Lê a aba "Acompanhamento" do painel de métricas e monta UMA imagem com:
faixa de KPIs do mês fechado + 4 gráficos (contratos vs meta, custo por
contrato, funil trabalhista, leads prometidos x recebidos).
"""

from __future__ import annotations

import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import estilo_graficos as eg  # noqa: E402

SECOES = {"PREVIDENCIÁRIO  (BPC / LOAS)": "prev", "TRABALHISTA": "trab",
          "CONSOLIDADO": "cons"}


def ler(caminho: str):
    """Devolve (meses, tabela) onde tabela[(secao, rotulo)] = lista de valores."""
    ws = openpyxl.load_workbook(caminho, data_only=True)["Acompanhamento"]
    linhas = [[c for c in r] for r in ws.iter_rows(values_only=True)]
    # a linha de cabeçalho é a que abre com "Indicador" (pode não ser a 3ª)
    cab = next(i for i, l in enumerate(linhas)
               if (l[0] or "").strip() == "Indicador")
    meses = [c for c in linhas[cab][2:10] if c]
    tabela, secao = {}, None
    for linha in linhas[cab + 1:]:
        rotulo = (linha[0] or "").strip()
        if not rotulo:
            continue
        if rotulo in SECOES:
            secao = SECOES[rotulo]
            continue
        valores = [linha[2 + i] for i in range(len(meses))]
        tabela[(secao, rotulo)] = [v if isinstance(v, (int, float)) else None
                                   for v in valores]
    return meses, tabela


def main(entrada: str, saida: str) -> None:
    meses, t = ler(entrada)

    def v(secao, rotulo):
        for chave, valores in t.items():
            if chave[0] == secao and chave[1].startswith(rotulo):
                return valores
        raise KeyError(f"{secao}/{rotulo}")

    # Mês fechado = último com contratos lançados (não projeta mês em curso).
    contratos_tot = v("cons", "Total de contratos")
    fim = max(i for i, x in enumerate(contratos_tot) if x) + 1
    m = meses[:fim]
    ult = fim - 1

    prev_contr = v("prev", "Contratos fechados")[:fim]
    trab_contr = v("trab", "Contratos fechados")[:fim]
    meta_tot = v("cons", "Meta total de contratos")[:fim]
    custo_contrato = v("cons", "Custo por contrato")[:fim]
    invest_tot = v("cons", "Investimento total")[:fim]
    leads_tot = v("cons", "Total de leads recebidos")[:fim]
    atingimento = v("cons", "Atingimento da meta")[:fim]

    reportados = [v("prev", "Leads reportados")[i] + v("trab", "Leads reportados")[i]
                  for i in range(fim)]
    recebidos = [v("prev", "Leads recebidos")[i] + v("trab", "Leads recebidos")[i]
                 for i in range(fim)]

    fig = eg.novo_painel(
        f"PAINEL COMERCIAL — {m[ult].upper()}/2026",
        f"Previdenciário (BPC/LOAS) + Trabalhista  ·  série {m[0]}–{m[ult]}  ·  "
        "fonte: Métricas Comerciais 2026")

    # ---------------- faixa de KPIs do mês fechado ----------------
    delta_custo = custo_contrato[ult] - custo_contrato[ult - 1]
    delta_leads = leads_tot[ult] - leads_tot[ult - 1]
    largura, gap = 0.2125, 0.02
    kpis = [
        (eg.numero(contratos_tot[ult]), "Contratos fechados",
         f"meta {eg.numero(meta_tot[ult])}  ·  {eg.percentual(atingimento[ult], 1)} da meta",
         eg.BOM if atingimento[ult] >= 0.9 else eg.ATENCAO),
        (eg.numero(leads_tot[ult]), "Leads recebidos",
         f"{'+' if delta_leads >= 0 else '−'}{eg.numero(abs(delta_leads))} "
         f"vs {m[ult-1].lower()}", eg.BOM if delta_leads >= 0 else eg.RUIM),
        (eg.moeda(invest_tot[ult]), "Investimento em anúncio",
         f"CPL médio {eg.moeda(invest_tot[ult]/leads_tot[ult], 2)}", None),
        (eg.moeda(custo_contrato[ult]), "Custo por contrato",
         f"{'+' if delta_custo >= 0 else '−'}{eg.moeda(abs(delta_custo), 2)} "
         f"vs {m[ult-1].lower()}",
         eg.BOM if delta_custo < 0 else eg.RUIM),
    ]
    for i, (valor, rotulo, apoio, cor) in enumerate(kpis):
        eg.cartao_kpi(fig, [0.045 + i * (largura + gap), 0.755, largura, 0.105],
                      valor, rotulo, apoio, cor)

    # ---------------- (a) contratos por área vs meta ----------------
    ax = fig.add_axes([0.055, 0.475, 0.375, 0.195])
    x = range(len(m))
    ax.bar(x, prev_contr, color=eg.CATEGORICA[0], label="Previdenciário",
           width=0.6, zorder=3)
    ax.bar(x, trab_contr, bottom=prev_contr, color=eg.CATEGORICA[1],
           label="Trabalhista", width=0.6, zorder=3,
           edgecolor=eg.SUPERFICIE, linewidth=2)
    for i in x:
        ax.plot([i - 0.36, i + 0.36], [meta_tot[i]] * 2, color=eg.TINTA_2,
                linewidth=2, linestyle=(0, (3, 2)), zorder=4)
        ax.text(i, max(contratos_tot[i], meta_tot[i]) + max(meta_tot) * 0.06,
                eg.numero(contratos_tot[i]), ha="center", va="bottom",
                fontsize=10.5, fontweight="bold", color=eg.TINTA)
    ax.plot([], [], color=eg.TINTA_2, linewidth=2, linestyle=(0, (3, 2)),
            label="Meta do mês")
    ax.set_xticks(list(x), m)
    ax.set_ylim(0, max(max(meta_tot), max(contratos_tot)) * 1.25)
    eg.limpar_eixo(ax)
    eg.titulo_do_grafico(ax, "Contratos fechados vs meta",
                         "por área de atuação · unidades")
    ax.legend(loc="upper left", bbox_to_anchor=(0, -0.13), ncol=3,
              handlelength=1.4, columnspacing=1.4)

    # ---------------- (b) custo por contrato ----------------
    ax = fig.add_axes([0.575, 0.475, 0.375, 0.195])
    ax.plot(x, custo_contrato, color=eg.DESTAQUE, linewidth=2.4,
            marker="o", markersize=7, markerfacecolor=eg.DESTAQUE,
            markeredgecolor=eg.SUPERFICIE, markeredgewidth=2, zorder=3)
    for i in (0, ult):
        ax.annotate(eg.moeda(custo_contrato[i]), (i, custo_contrato[i]),
                    textcoords="offset points", xytext=(0, 13), ha="center",
                    fontsize=10.5, fontweight="bold", color=eg.TINTA)
    ax.set_xticks(list(x), m)
    ax.set_xlim(-0.35, len(m) - 0.65)
    ax.set_ylim(0, max(custo_contrato) * 1.32)
    ax.yaxis.set_major_formatter(lambda v, _: eg.moeda(v))
    eg.limpar_eixo(ax)
    variacao = (custo_contrato[ult] - custo_contrato[0]) / custo_contrato[0]
    sentido = "queda de" if variacao < 0 else "alta de"
    eg.titulo_do_grafico(
        ax, "Custo por contrato",
        f"investimento total ÷ contratos · {sentido} "
        f"{eg.percentual(abs(variacao), 1)} de {m[0].lower()} a {m[ult].lower()}")

    # ---------------- (c) funil trabalhista do mês ----------------
    ax = fig.add_axes([0.195, 0.150, 0.235, 0.195])
    etapas = ["Leads recebidos", "Reuniões agendadas", "Reuniões comparecidas",
              "Contratos fechados"]
    valores = [v("trab", "Leads recebidos")[ult], v("trab", "Reuniões agendadas")[ult],
               v("trab", "Reuniões comparecidas")[ult], trab_contr[ult]]
    cores = [eg.SEQUENCIAL[8], eg.SEQUENCIAL[6], eg.SEQUENCIAL[4], eg.SEQUENCIAL[2]]
    eg.barras_horizontais(ax, etapas, valores, cores=cores)
    for i in range(1, len(valores)):
        ax.text(max(valores) * 1.02, i - 0.5,
                f"→ {eg.percentual(valores[i] / valores[i-1], 0)} avançam",
                va="center", ha="left", fontsize=9, color=eg.TINTA_2)
    ax.set_xlim(0, max(valores) * 1.30)
    eg.titulo_do_grafico(ax, f"Funil trabalhista — {m[ult].lower()}",
                         "quantas oportunidades sobrevivem a cada etapa", x=-0.60)

    # ---------------- (d) leads prometidos x recebidos ----------------
    ax = fig.add_axes([0.575, 0.150, 0.375, 0.195])
    ax.bar([i - 0.19 for i in x], reportados, width=0.36,
           color=eg.CATEGORICA[0], label="Reportados pelo marketing", zorder=3)
    ax.bar([i + 0.19 for i in x], recebidos, width=0.36,
           color=eg.CATEGORICA[2], label="Recebidos no Kinbox", zorder=3)
    for i in x:
        falta = reportados[i] - recebidos[i]
        ax.text(i, max(reportados) * 1.05,
                f"−{eg.numero(falta)}" if falta else "0",
                ha="center", va="bottom", fontsize=10, fontweight="bold",
                color=eg.RUIM if falta > 20 else eg.TINTA_2)
    ax.set_xticks(list(x), m)
    ax.set_ylim(0, max(reportados) * 1.24)
    eg.limpar_eixo(ax)
    eg.titulo_do_grafico(ax, "Leads: prometidos x chegaram na operação",
                         "número em destaque = leads que não entraram no Kinbox")
    ax.legend(loc="upper left", bbox_to_anchor=(0, -0.13), ncol=2,
              handlelength=1.4, columnspacing=1.4)

    eg.nota(fig, "Fonte: planilha “Métricas Comerciais 2026 — Roger Bento”, aba "
                 "Acompanhamento. Nenhum número foi estimado: o painel só mostra "
                 "meses já lançados.", y=0.062)
    eg.nota_conferir(
        fig, "[CONFERIR] Julho: 22 reuniões agendadas − 10 no-show = 12, mas a "
             "planilha registra 14 reuniões comparecidas.", y=0.036)
    eg.nota_conferir(
        fig, "[CONFERIR] Setembro já tem meta lançada (30 previdenciário + 25 "
             "trabalhista) e ainda não tem realizado — mês fora do painel.", y=0.014)

    eg.salvar(fig, saida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2
         else "graficos/painel-comercial.png")
