# Formas e cores dos painéis

## Primeiro a forma, por último a cor

Painel ruim começa escolhendo cor. Comece perguntando **qual é o trabalho do
número**:

| Trabalho do número | Forma | Papel da cor |
|---|---|---|
| Comparar quem é maior (ranking) | barra horizontal ordenada | **uma cor só**, mais escuro = maior |
| Evolução no tempo | linha (área se for série única) | uma cor |
| Distinguir séries diferentes | barra agrupada/empilhada, multilinha | **categórica** |
| Uma série é o assunto, o resto é contexto | destaque: a série na cor, o resto em cinza | 1 cor + cinza |
| Realizado × meta | barra + traço tracejado da meta | 1–2 cores |
| Parte do todo | barra empilhada | categórica |
| Um número só | **cartão de KPI**, não gráfico | — |
| Mais de 7 itens com vários indicadores | **tabela-gráfico** | uma cor por coluna |

## Paleta (já implementada em `scripts/estilo_graficos.py`)

Categórica, **em ordem fixa** — nunca embaralhe, nunca gere uma 9ª cor:

`#2a78d6` azul · `#eb6834` laranja · `#1baf7a` água · `#eda100` amarelo ·
`#e87ba4` magenta · `#008300` verde · `#4a3aa7` violeta · `#e34948` vermelho

Sequencial (magnitude), do claro ao escuro: `#86b6ef` → `#104281`
(`eg.SEQUENCIAL`, aplicada automaticamente por `eg.escala_por_magnitude`).

Cores de estado, **reservadas** — nunca use como "série 4":
`eg.BOM` verde · `eg.ATENCAO` amarelo · `eg.RUIM` vermelho · `eg.VERMELHO` para
os `[CONFERIR]`.

## Regras que não se quebram

- **Nunca dois eixos Y no mesmo gráfico.** Duas grandezas de escala diferente
  viram dois gráficos. É o erro nº 1 de painel.
- **Nunca arco-íris para magnitude.** Magnitude é uma cor só, clara → escura.
- **A cor pertence à entidade, não à posição.** Se o filtro muda, quem sobrou
  mantém a cor.
- **Texto em tinta neutra**, nunca na cor da série.
- **Número na ponta da barra, sim; em cima de todo ponto de linha, não** —
  na linha, rotule o primeiro, o último e o extremo relevante.
- **Legenda sempre que houver 2 séries ou mais**; com uma série só, o título já
  diz o que é.
- **Grade discreta e atrás dos dados**; sem moldura em volta do gráfico.
- **Barra sempre começa no zero.** Cortar o eixo Y para "mostrar melhor a
  diferença" é mentira gráfica.
- **Rosca/pizza: não.** Use barra — o olho compara comprimento, não ângulo.
- Percentual com denominador pequeno (5, 7 casos) **precisa de aviso** ao lado:
  100% de 5 sessões não é o mesmo que 91% de 153.

## Antes de dar por pronto

1. Olhe o `.png` — colisão de rótulo, texto cortado, legenda em cima de título.
2. Todo gráfico tem título que diz **o que se vê**, não o nome da coluna.
3. Todo painel tem fonte no rodapé e os `[CONFERIR]` em vermelho.
4. Um leitor da equipe entende o painel **sem você explicar**. Se precisar
   explicar, o painel ainda não está pronto.
