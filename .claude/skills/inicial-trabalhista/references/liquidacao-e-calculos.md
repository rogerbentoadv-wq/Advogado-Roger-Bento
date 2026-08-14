# Liquidação — cálculo estimado por pedido (simples)

Regra do escritório: **todo pedido leva um valor estimado ao lado**, e a peça
termina com o **valor da causa** (soma dos pedidos). Cálculo **simples e
conservador** — não é liquidação de sentença. Sempre acompanha a ressalva do
art. 840, §1º, da CLT (valor estimado, não limita a condenação).

## Base de cálculo

- **Remuneração de referência (R):** último salário + médias habituais
  (comissões, "por fora" comprovado, adicionais habituais). Se faltar dado,
  usar o salário informado e marcar `[CÁLCULO A CONFIRMAR]`.
- **Valor da hora (Vh):** `R ÷ 220` (jornada 44h/semana).
- **Meses do período imprescrito (M):** meses do contrato dentro dos últimos 5
  anos (prescrição quinquenal) até o fim do contrato.
- Arredondar para valores "cheios" (dezenas/centenas), como nos modelos.

## Fórmulas por verba (estimativa)

| Verba | Fórmula simples |
|---|---|
| Saldo de salário | (R ÷ 30) × dias trabalhados no mês da saída |
| Aviso-prévio indenizado | R + proporcional (30 dias + 3/ano, máx. 90) → na prática ≈ R a R×1,x |
| 13º proporcional | (R ÷ 12) × meses do ano trabalhados |
| Férias proporcionais + 1/3 | (R ÷ 12) × meses × 1,3333 |
| Férias vencidas + 1/3 | R × 1,3333 (por período vencido) |
| FGTS do período | 8% × R × M (não depositado) |
| Multa 40% do FGTS | 40% × (saldo do FGTS + FGTS deferido) |
| Multa art. 477, §8º | = 1 × R (uma remuneração) |
| Multa art. 467 | 50% × verbas rescisórias incontroversas |
| Horas extras + reflexos | (nº h.e./mês) × Vh × 1,5 × M, e somar ~30–40% de reflexos |
| Intervalo intrajornada | (fração suprimida em h) × Vh × 1,5 × dias trabalhados |
| Adicional noturno | 20% × Vh × (horas noturnas/mês) × M |
| Insalubridade | grau (10/20/40%) × base × M + reflexos → base: salário mínimo (com ressalva SV 4) |
| Periculosidade | 30% × salário-base × M + reflexos |
| Diferenças salariais / acúmulo | (percentual, ex. 20–30%) × R × M + reflexos |
| Dano moral | valor arbitrado fixo (ex.: R$ 5.000–R$ 25.000, conforme gravidade) |
| Honorários sucumbenciais | 15% × soma dos demais pedidos |

> Reflexos (regra rápida): quando a verba é habitual, some uma estimativa de
> reflexos em DSR, 13º, férias+1/3, aviso e FGTS+40%. Para manter simples, pode
> lançar os reflexos como um pedido próprio com valor estimado, como nos modelos.

## Como apresentar (dois formatos aceitos — igual aos modelos)

**Formato A — valor ao lado de cada alínea** (bom para poucas verbas):
```
a) horas extras + reflexos ................... R$ 18.000,00
b) intervalo intrajornada suprimido .......... R$ 6.000,00
...
```

**Formato B — tabela de pedidos** (preferido quando há muitas verbas):
```
| Pedido | Valor estimado |
|---|---|
| Aviso-prévio indenizado | R$ 3.949,00 |
| 13º proporcional | R$ 1.795,00 |
| ... | ... |
| VALOR TOTAL | R$ 94.174,06 |
```

Pedidos que são obrigação de fazer (anotação/retificação de CTPS, entrega de
guias) entram como **"obrigação de fazer"** ou **"a apurar"**, sem valor, mas
listados.

## Valor da causa

`Valor da causa = soma de todos os pedidos com valor estimado`. Fechar com:

> "Dá-se à causa, para fins meramente estimativos e nos termos do art. 840,
> §1º, da CLT, o valor de R$ [soma]."

E, quando houver verbas dependentes de documento/perícia, incluir a ressalva:

> "Os valores são estimativos, formulados para atender ao art. 840, §1º, da CLT,
> não limitando a condenação, especialmente quanto às parcelas cuja apuração
> depende de documentos em poder da reclamada ou de perícia."

## Regra de honestidade

Cálculo estimado **não é** cálculo exato. Onde faltar dado (salário real,
nº de horas, meses), usar premissa razoável e marcar `[CÁLCULO A CONFIRMAR]`
para o advogado validar. Nunca apresentar precisão que os dados não sustentam.
