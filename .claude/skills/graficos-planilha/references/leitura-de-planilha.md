# Leitura da planilha — o que conferir antes de plotar

Um painel bonito com número errado é pior que nenhum painel. Antes de desenhar
qualquer coisa, faça esta passagem.

## 1. Abra com `data_only=True`

Sem isso, células de fórmula voltam como o texto `=SOMA(...)`. Se vierem `None`
mesmo com `data_only=True`, a planilha nunca foi aberta no Excel/Sheets depois da
última edição: avise o usuário em vez de tratar como zero.

## 2. Não confie no número da linha do cabeçalho

Planilha de escritório costuma ter título, subtítulo e linha em branco no topo.
Localize o cabeçalho pelo conteúdo, não pela posição:

```python
cab = next(i for i, l in enumerate(linhas) if (l[0] or "").strip() == "Indicador")
```

## 3. Ache o fim da série real

Coluna de mês preenchida com `0` por causa de fórmula **não é** mês realizado.
Corte a série no último período com lançamento de verdade (ex.: último mês com
contratos > 0). Mês em curso nunca entra no painel — se tiver meta lançada e
nenhum realizado, isso vira `[CONFERIR]` no rodapé.

## 4. Feche as contas

Confira, com os próprios dados:

- as parcelas somam o total (`prev + trab = consolidado`);
- `agendadas − no-show = comparecidas`;
- percentuais batem com numerador ÷ denominador;
- `leads reportados ≥ leads recebidos` (se não, algo está trocado).

**Divergiu?** Plote o que está na planilha e registre em vermelho, com a conta
explícita: `[CONFERIR] Julho: 22 agendadas − 10 no-show = 12, mas a planilha
registra 14 comparecidas.` Nunca "conserte" o número por conta própria.

## 5. Descubra o que a coluna significa

`Total` é o total de quê? Do período todo, ou só das sessões novas? Se a
planilha não diz e o resultado muda conforme a leitura, escreva a sua
interpretação no subtítulo **e** marque `[CONFERIR]`.

## 6. Período

Se a planilha não traz período nem data de extração, o painel **não pode**
anunciar "números do mês". Use um título neutro e um `[CONFERIR]` pedindo a
confirmação do período.

## 7. Nomes de pessoas

Use o nome exatamente como está na planilha (só apare espaços sobrando). Não
"corrija", não abrevie, não inverta — o painel vai circular na equipe.
