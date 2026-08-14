# Banco de jurisprudência — protocolo e procedência

Este diretório é a **única fonte autorizada** de súmulas, orientações
jurisprudenciais (OJs), súmulas vinculantes e teses/precedentes que a skill
`inicial-trabalhista` pode citar nas peças. A regra é simples e inegociável:

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
- `ROTINA-ATUALIZACAO.md` — protocolo da passada de atualização.
