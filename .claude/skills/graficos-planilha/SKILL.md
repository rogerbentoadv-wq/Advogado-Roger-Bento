---
name: graficos-planilha
description: >-
  Transforma planilhas (.xlsx/.csv) em painéis de gráficos prontos para
  apresentar à equipe — uma imagem .png por planilha, com a identidade visual do
  escritório Róger Bento (logo, paleta e tipografia padrão). Lê a planilha,
  identifica os indicadores e o período já fechado, escolhe a forma de gráfico
  adequada a cada número (ranking, evolução, funil, meta x realizado,
  tabela-gráfico), destaca os KPIs do mês em cartões e marca em VERMELHO tudo o
  que estiver faltando ou inconsistente na planilha. Use quando o usuário
  anexar/indicar uma planilha e pedir gráfico, painel, dashboard, "os números do
  mês", relatório visual para a equipe ou reunião, ou disparar
  /graficos-planilha.
---

# Painéis de números do escritório — de planilha para imagem

## O que esta skill entrega

**Uma imagem `.png` por planilha.** Não é um gráfico solto: é um **painel**
— faixa de KPIs no topo + 3 a 5 gráficos que contam a história do mês — para
o usuário mandar no grupo da equipe, projetar na reunião ou imprimir.

O padrão foi calibrado nos painéis já existentes em `scripts/paineis/`. Use-os
como referência antes de escrever um novo.

## Princípios inegociáveis

1. **Nunca invente número.** Nada de projetar mês incompleto, estimar dado que
   falta ou "arredondar para ficar bonito". O painel só mostra o que a planilha
   lançou.
2. **O que falta ou não bate sai em VERMELHO** — mesma regra dos colchetes das
   peças. Use `eg.nota_conferir(fig, "[CONFERIR] ...")` no rodapé para: período
   não informado na planilha, linha que não fecha com a conta, meta lançada sem
   realizado, coluna de significado ambíguo. Quem olha o painel precisa ver na
   hora o que ainda não está confirmado.
3. **Confira a aritmética da planilha antes de plotar.** Some as parcelas e
   compare com o total, verifique se `agendadas − no-show = comparecidas`, se
   `%` bate com numerador/denominador. Divergência não se corrige em silêncio:
   plota o que está na planilha e registra em vermelho.
4. **Mês em curso fica fora.** Detecte o último mês efetivamente lançado e corte
   a série ali (ver `painel_comercial.py`, variável `fim`).
5. **Toda imagem sai timbrada** com a logo do escritório — o conversor de estilo
   já faz isso em `novo_painel()`.
6. **A fonte vem no rodapé**: nome da planilha e aba de origem.

## Como trabalhar

### 1. Ler a planilha antes de decidir qualquer coisa

```bash
python3 - <<'EOF'
import openpyxl
wb = openpyxl.load_workbook("<arquivo>.xlsx", data_only=True)
for ws in wb.worksheets:
    print("ABA:", ws.title, ws.max_row, "x", ws.max_column)
    for r in ws.iter_rows(max_row=60, values_only=True):
        if any(c is not None for c in r):
            print([str(c)[:30] if c is not None else "" for c in r])
EOF
```

`data_only=True` é obrigatório: sem isso as células de fórmula voltam como
texto `=B3/C3`. Nunca leia a planilha "no olho" pela pré-visualização — leia os
valores.

Enquanto lê, responda: **qual é a pergunta que a equipe vai fazer olhando isso?**
O painel responde a essa pergunta; o resto é ruído.

### 2. Escolher a forma de cada número

Regra completa em `references/formas-e-cores.md`. Resumo:

| O número serve para… | Forma |
|---|---|
| Um total do mês, sozinho | **cartão de KPI** (`eg.cartao_kpi`) — nunca um gráfico de uma barra |
| Comparar pessoas/itens (ranking) | barras horizontais ordenadas (`eg.barras_horizontais`) |
| Vários indicadores × várias pessoas | **tabela-gráfico** (`eg.tabela_barras`) — não repita os nomes em 4 gráficos |
| Evolução ao longo dos meses | linha |
| Realizado contra meta | barras + traço tracejado da meta |
| Perda etapa a etapa | funil (barras horizontais em degradê de uma cor só) |
| Prometido × entregue | barras agrupadas, com a diferença rotulada |

### 3. Montar o painel

Modelo de arquivo: copie um dos scripts de `scripts/paineis/` e adapte. Sempre:

```python
import estilo_graficos as eg
fig = eg.novo_painel("TÍTULO DO PAINEL — MÊS/ANO", "subtítulo com escopo e fonte")
eg.cartao_kpi(fig, [x, y, larg, alt], valor, rótulo, apoio, cor)
ax = fig.add_axes([x, y, larg, alt]);  ...  ; eg.limpar_eixo(ax)
eg.titulo_do_grafico(ax, "Título do gráfico", "o que ele mostra")
eg.nota(fig, "Fonte: ...");  eg.nota_conferir(fig, "[CONFERIR] ...")
eg.salvar(fig, "graficos/<nome>.png")
```

Grade de posições que funciona (fração da figura, painel 12,6 × 9,4 pol):

| Bloco | `[esq, base, larg, alt]` |
|---|---|
| 4 cartões de KPI | `[0.045 + i*0.2325, 0.755, 0.2125, 0.105]` |
| gráfico sup. esq. / dir. | `[0.055, 0.475, 0.375, 0.195]` / `[0.575, 0.475, 0.375, 0.195]` |
| gráfico inf. esq. / dir. | `[0.195, 0.150, 0.235, 0.195]` / `[0.575, 0.150, 0.375, 0.195]` |
| tabela-gráfico (largura toda) | `[0.045, 0.335, 0.910, 0.325]` |
| rodapé: fonte / conferir | `y=0.062` / `y=0.036` e `y=0.014` |

### 4. Olhar a imagem gerada — sempre

Abra o `.png` e confira **antes de entregar**:

- rótulo encavalado em barra, linha de meta ou legenda;
- texto do rodapé cortado na margem direita (quebre em duas linhas);
- título de um gráfico colidindo com a legenda do gráfico de cima;
- número ilegível por estar sobre a barra escura.

Nenhum painel vai para o usuário sem essa conferência visual.

### 5. Entregar

- Salve em `graficos/<assunto>-<mês>.png`.
- Mande o arquivo ao usuário (é imagem: abre direto no WhatsApp e no PowerPoint).
- Diga em uma frase **o que o painel mostra** e **o que está em vermelho**.
- Arquive o `.png` na pasta do Google Drive do escritório, quando indicada.

## Dependências

```bash
pip install -r scripts/requirements-graficos.txt   # openpyxl + matplotlib
```

## Arquivos de referência

| Arquivo | Para quê |
|---|---|
| `references/formas-e-cores.md` | qual gráfico usar, paleta, o que nunca fazer |
| `references/leitura-de-planilha.md` | como ler a planilha e o que conferir antes de plotar |
| `scripts/estilo_graficos.py` | módulo de estilo (paleta, cartões, formas, rodapé) |
| `scripts/paineis/painel_comercial.py` | exemplo: série mensal, meta, funil |
| `scripts/paineis/painel_produtividade.py` | exemplo: ranking por pessoa, tabela-gráfico |
