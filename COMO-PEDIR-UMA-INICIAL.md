# Como pedir uma inicial (passo a passo)

Guia rápido para solicitar a elaboração de uma reclamatória trabalhista com o
agente deste projeto.

> Para a **defesa** (contestação da BS Construções), veja
> `COMO-PEDIR-UMA-CONTESTACAO.md`.

## Passo a passo

**1. Abra uma conversa NOVA** no Claude Code, dentro deste projeto
(Advogado-Roger-Bento). Use **uma conversa por caso/cliente** — começa limpa,
sem misturar processos.

**2. Confirme que o Google Drive está ligado** no seletor de conectores da
conversa (para o agente ler os documentos e salvar a peça na pasta do cliente).

**3. Dispare o agente** de um destes jeitos:
- digite **`/inicial-trabalhista`**; ou
- **descreva o caso** em uma frase (ex.: "preciso de uma inicial para um
  motorista dispensado sem justa causa, com horas extras não pagas").

**4. Indique a pasta do cliente no Drive** (link ou nome). É de onde o agente lê
TRCT, CTPS, holerites, cartão-ponto, extrato de FGTS e prints — e onde a peça
final será arquivada.

**5. Responda à entrevista por blocos.** O agente pergunta em partes (partes,
contrato, jornada, ambiente, rescisão, verbas, provas). Responda no chat e/ou
aponte os documentos. O que faltar, ele marca para conferência.

**6. Aprove o mapa de teses.** Antes de redigir, ele mostra os pedidos cabíveis,
o rito, a competência e a estimativa de valor. Você confirma ou ajusta.

**7. Receba a entrega:**
- o arquivo **`.docx` editável** (enviado no chat e **salvo na pasta do cliente
  no Drive**), com cálculo estimado em cada pedido e o valor da causa;
- no chat, um resumo curto + o bloco **"Pontos de atenção antes do protocolo"**.

**8. Revise e protocole.** Confira cálculos, valide as citações marcadas
`[CONFERIR]` e ajuste o que quiser no Word.

## Exemplo de mensagem para começar

> `/inicial-trabalhista`
> Cliente: João da Silva, pedreiro. Admitido em 03/2023, dispensado sem justa
> causa em 06/2026. Salário R$ 2.400 + R$ 500 "por fora". Fazia ~2h extras/dia
> sem pagar, sem EPI. A pasta do cliente no Drive é
> [colar link da pasta]. Os documentos (TRCT, CTPS, extrato FGTS) estão lá.

O agente assume a partir daí: entrevista, mapa de teses, redação, cálculo,
geração do `.docx` e arquivamento no Drive.

## Lembretes

- **Nunca inventa jurisprudência:** o que não estiver verificado no banco sai
  marcado `[CONFERIR]` para você validar.
- **A peça é minuta de apoio:** a revisão e o protocolo são sempre seus.
- Se o conector do Drive estiver fora do ar, o agente entrega o `.docx` pelo
  chat e avisa que não conseguiu salvar no Drive.
