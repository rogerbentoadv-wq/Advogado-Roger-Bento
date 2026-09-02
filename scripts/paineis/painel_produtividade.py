# -*- coding: utf-8 -*-
"""Painel de produtividade do atendimento, por atendente.

Uso:
    python3 scripts/paineis/painel_produtividade.py \
        dados/relatorio-produtividade.xlsx graficos/painel-produtividade.png

Lê o relatório de produtividade (uma linha por atendente) e monta UMA imagem:
faixa de KPIs da equipe + tabela-gráfico com todos os indicadores por pessoa +
ranking de leads gerados.
"""

from __future__ import annotations

import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import estilo_graficos as eg  # noqa: E402


def ler(caminho: str):
    """Devolve (colunas, linhas) do relatório — a 1ª linha é o cabeçalho."""
    ws = openpyxl.load_workbook(caminho, data_only=True).worksheets[0]
    linhas = [list(r) for r in ws.iter_rows(values_only=True) if any(r)]
    cabecalho = [str(c).strip() for c in linhas[0]]
    dados = []
    for linha in linhas[1:]:
        registro = dict(zip(cabecalho, linha))
        registro["Atendente"] = str(registro["Atendente"]).strip()
        dados.append(registro)
    return cabecalho, dados


def main(entrada: str, saida: str) -> None:
    _, dados = ler(entrada)
    dados.sort(key=lambda d: d["Total"], reverse=True)

    nomes = [d["Atendente"] for d in dados]
    total = [d["Total"] for d in dados]
    novas = [d["Sessões novas"] for d in dados]
    leads = [d["Leads"] for d in dados]
    resolvidas = [d["Sessões resolvidas"] for d in dados]
    mensagens = [d["Mensagens trocadas"] for d in dados]
    taxa = [r / t for r, t in zip(resolvidas, total)]

    fig = eg.novo_painel(
        "PRODUTIVIDADE DO ATENDIMENTO",
        f"{len(nomes)} atendentes  ·  relatório por pessoa  ·  "
        "fonte: relatório de produtividade (Kinbox)")

    # ---------------- faixa de KPIs da equipe ----------------
    largura, gap = 0.2125, 0.02
    kpis = [
        (eg.numero(sum(total)), "Sessões atendidas",
         f"média de {eg.numero(sum(total)/len(nomes))} por atendente", None),
        (eg.numero(sum(novas)), "Sessões novas",
         f"{eg.percentual(sum(novas)/sum(total), 0)} de todo o atendimento", None),
        (eg.numero(sum(leads)), "Leads gerados",
         f"{eg.percentual(sum(leads)/sum(novas), 0)} das sessões novas viraram lead",
         None),
        (eg.percentual(sum(resolvidas)/sum(total), 0), "Taxa de resolução",
         f"{eg.numero(sum(resolvidas))} de {eg.numero(sum(total))} sessões "
         "resolvidas", None),
    ]
    for i, (valor, rotulo, apoio, cor) in enumerate(kpis):
        eg.cartao_kpi(fig, [0.045 + i * (largura + gap), 0.755, largura, 0.105],
                      valor, rotulo, apoio, cor)

    # ---------------- tabela-gráfico: todos os indicadores por pessoa -------
    fig.text(0.045, 0.715, "Quadro por atendente", fontsize=12.5,
             fontweight="bold", color=eg.TINTA, va="bottom", ha="left")
    fig.text(0.045, 0.694, "ordenado por sessões atendidas · dentro de cada "
             "coluna, barra mais escura = número maior · “atendidas” = todas as "
             "sessões (novas + retomadas)", fontsize=9.5, color=eg.TINTA_2,
             va="bottom", ha="left")

    eg.tabela_barras(
        fig, [0.045, 0.335, 0.910, 0.325], nomes,
        [
            {"titulo": "Atendidas", "valores": total},
            {"titulo": "Novas", "valores": novas},
            {"titulo": "Leads", "valores": leads},
            {"titulo": "Resolvidas", "valores": resolvidas},
            {"titulo": "% resolvidas", "valores": taxa,
             "formato": lambda v: eg.percentual(v, 0)},
            {"titulo": "Mensagens", "valores": mensagens},
        ])

    # ---------------- captação: quanto de cada sessão nova vira lead -------
    captacao = [l / n if n else 0 for l, n in zip(leads, novas)]
    ordem = sorted(range(len(nomes)), key=lambda i: captacao[i], reverse=True)
    ax = fig.add_axes([0.255, 0.115, 0.215, 0.155])
    eg.barras_horizontais(ax, [nomes[i] for i in ordem],
                          [captacao[i] for i in ordem],
                          formato="{:,.0%}")
    eg.titulo_do_grafico(ax, "Taxa de captação",
                         "leads gerados ÷ sessões novas atendidas", x=-0.98)

    # ---------------- esforço: mensagens por sessão atendida ---------------
    por_sessao = [m / t for m, t in zip(mensagens, total)]
    ordem2 = sorted(range(len(nomes)), key=lambda i: por_sessao[i], reverse=True)
    ax = fig.add_axes([0.740, 0.115, 0.215, 0.155])
    eg.barras_horizontais(ax, [nomes[i] for i in ordem2],
                          [por_sessao[i] for i in ordem2],
                          formato="{:,.1f}")
    eg.titulo_do_grafico(ax, "Esforço por atendimento",
                         "mensagens trocadas ÷ sessões atendidas", x=-0.98)

    eg.nota(fig, "Fonte: relatório de produtividade por atendente — painel "
                 "gerado direto da planilha, nenhum número estimado. Cuidado com "
                 "volume baixo: Gabriel Souza teve 5 sessões novas.", y=0.062)
    eg.nota_conferir(
        fig, "[CONFERIR] A planilha não informa o período nem a data de "
             "extração do relatório — confirmar antes de apresentar como "
             "“números do mês”.", y=0.036)
    eg.nota_conferir(
        fig, "[CONFERIR] “Sessões atendidas” (coluna Total) inclui sessões "
             "novas e retomadas; “Leads” e “Sessões resolvidas” dependem de a "
             "equipe marcar a sessão no Kinbox.", y=0.014)

    eg.salvar(fig, saida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2
         else "graficos/painel-produtividade.png")
