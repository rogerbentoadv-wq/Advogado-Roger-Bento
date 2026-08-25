# Banco de jurisprudência — protocolo e procedência

Este diretório é a **única fonte autorizada** de súmulas, orientações
jurisprudenciais (OJs), súmulas vinculantes e teses/precedentes que as skills
`inicial-trabalhista` (polo ativo) e `contestacao-trabalhista` (polo passivo)
podem citar nas peças. A regra é simples e inegociável:

> **Nada é citado numa peça se não estiver aqui, com fonte e data. O que não
> estiver verificado sai na peça marcado como `[CONFERIR]`.**

Isso existe para **impedir a invenção de jurisprudência**. O agente NÃO cita de
memória: cita deste banco, e este banco só recebe entradas com procedência.

---

## Esquema de cada entrada

Toda entrada — súmula, OJ, tese — segue este formato:

```
### [Nº] — [Tema curto]
- **Órgão:** TST | STF | TRT-4
- **Texto:** transcrição ou resumo fiel do enunciado.
- **Fonte:** URL consultada.
- **Verificado em:** AAAA-MM-DD.
- **Status:** VERIFICADO | A CONFERIR | SUSPENSO/SUPERADO
- **Observações:** divergências, modulação, suspensão de eficácia, impacto da
  Reforma (Lei 13.467/2017), etc.
```

## Significado do Status

- **VERIFICADO** — o enunciado foi conferido contra uma fonte registrada na data
  indicada. Pode ser citado na peça. Ainda assim, o advogado confere no
  protocolo (fontes de terceiros não substituem o texto oficial).
- **A CONFERIR** — a tese é conhecida, mas o número/texto ainda não foi conferido
  contra fonte nesta base. Na peça, entra **sempre** com `[CONFERIR]`.
- **SUSPENSO/SUPERADO** — enunciado com eficácia suspensa, cancelado ou superado
  por decisão posterior (ex.: Súmula 228 do TST — base de cálculo da
  insalubridade). Serve de alerta; **não** é citado como vigente.

---

## Limitações honestas deste ambiente (leia)

1. **Sites oficiais bloqueados:** neste ambiente de execução, o acesso direto a
   `tst.jus.br`, `trt4.jus.br` e afins está bloqueado pela política de rede. A
   verificação é feita por **busca na web**, que retorna majoritariamente
   **fontes secundárias** (Jusbrasil, LexML, vade-mécuns online, etc.). São boas
   para localizar e conferir número↔tema, mas **não substituem a fonte oficial**.
   Por isso todo enunciado VERIFICADO ainda carrega o dever de conferência final
   pelo advogado.

2. **Súmulas e OJs mudam pouco;** o que muda é a jurisprudência de acórdãos
   (teses, temas repetitivos). Uma "atualização diária" faz sentido para
   monitorar novidades e revisões, mas na maioria dos dias não haverá alteração
   nas súmulas/OJs.

3. **Sem invenção:** se a busca não confirmar um enunciado, ele **não** é
   promovido a VERIFICADO. Fica A CONFERIR. Preferimos uma lacuna honesta a uma
   citação falsa.

---

## Rotina de atualização

Ver `ROTINA-ATUALIZACAO.md`. Cada passada de verificação:
1. Percorre as entradas **A CONFERIR** e tenta confirmá-las por busca.
2. Registra fonte + data + status.
3. Procura revisões/cancelamentos recentes (Resoluções do TST, decisões do STF).
4. Faz commit com o resumo das mudanças.

## Arquivos

- `sumulas-tst.md` — Súmulas do TST.
- `sumulas-vinculantes-stf.md` — Súmulas Vinculantes do STF (recorte trabalhista).
- `orientacoes-jurisprudenciais-sdi.md` — OJs da SDI-1, SDI-2 e Transitórias.
- `sumulas-trt4.md` — Súmulas e teses do TRT da 4ª Região.
- `teses-repetitivas-irr.md` — IRR/IAC/temas repetitivos do TST e TRT-4.
- `precedentes-do-escritorio.md` — ementas reais colhidas das **iniciais**
  protocoladas pela banca (material de reuso; conferir vigência).
- `defesa-do-escritorio.md` — súmulas, OJs, teses vinculantes e normas de foro
  citadas nas **contestações** protocoladas pela banca em favor da BS Construções
  (fonte autorizada da skill `contestacao-trabalhista`; conferir vigência).
- `jurisprudencia-VERIFICADO.md` — banco em formato de tabelas (súmulas, OJs,
  temas sensíveis) gerado por uma passada automática de verificação. **Ver
  cautelas abaixo antes de citar dele.**
- `ROTINA-ATUALIZACAO.md` — protocolo da passada de atualização.

## Relação entre os arquivos e ordem de confiança

Havendo divergência entre arquivos, siga esta ordem de confiança:
1. `sumulas-tst.md` / `precedentes-do-escritorio.md` / `defesa-do-escritorio.md`
   — curados com fonte e data entrada a entrada (precedentes e teses de defesa
   vêm das peças reais da banca).
2. `jurisprudencia-VERIFICADO.md` — visão em tabela, útil para os **temas
   sensíveis** (base de cálculo da insalubridade, Tema 1.046, correção/juros),
   porém contém entradas a corrigir (abaixo). Não cite dele sem conferir.

### ⚠️ Cautelas em `jurisprudencia-VERIFICADO.md` (a corrigir)

Entradas com problema identificado — **não citar até conferência**:
- **Súmula 431** descrita como "intervalo intrajornada irrenunciável": incorreto.
  A Súmula 431 trata do **divisor 220** para 44h semanais. (marcada A CONFERIR)
- **Súmula 192** descrita como "periculosidade": incorreto. Periculosidade é a
  **Súmula 191**; a 192 trata de complementação de aposentadoria. (A CONFERIR)
- **Súmula 437** com teor garbled ("intervalo reduzido... mesma localidade"):
  o teor correto é o pagamento **integral** do intervalo suprimido (regime
  anterior) — ver `sumulas-tst.md`. (A CONFERIR)
- **Súmula 228 / RCL 6275/2024, "Min. Lewandowski"**: citação **duvidosa** — o
  ministro deixou o STF em 2023, o que torna improvável uma decisão dele em
  2024. Tratar a suspensão da Súmula 228 pela via da **SV 4** (Rcl/decisões do
  STF a confirmar), sem afirmar esse número/relator até conferência.
- **SV 4** marcada VERIFICADO com teor simplificado: a redação real veda usar o
  salário mínimo como indexador **e** proíbe o Judiciário de substituí-lo sem
  lei/norma coletiva — manter a nuance ao citar.

> As entradas marcadas VERIFICADO neste arquivo que estão corretas (Súmulas 85 e
> 366; Tema 1.046 do STF) podem ser usadas com a conferência final de praxe.
