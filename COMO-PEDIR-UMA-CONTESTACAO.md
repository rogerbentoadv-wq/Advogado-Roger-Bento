# Como pedir uma contestação (passo a passo)

Guia rápido para solicitar a elaboração de uma **defesa da BS Construções e
Reformas Ltda.** com o agente deste projeto.

## Passo a passo

**1. Abra uma conversa NOVA** no Claude Code, dentro deste projeto
(Advogado-Roger-Bento). Use **uma conversa por processo** — começa limpa, sem
misturar casos.

**2. Confirme que o Google Drive está ligado** no seletor de conectores (para o
agente ler a inicial e os documentos, e salvar a peça na pasta do processo).

**3. Dispare o agente** de um destes jeitos:
- digite **`/contestacao-trabalhista`**; ou
- **descreva o caso** em uma frase (ex.: "chegou uma reclamatória contra a BS na
  4ª Vara de Taquara, audiência dia 12, preciso da contestação").

**4. Diga logo o prazo.** Data da audiência inicial ou o termo final para
contestar — é a primeira coisa que o agente pergunta.

**5. Indique a pasta do processo no Drive** (link ou nome), com a **inicial** e
os documentos que a instruem, e os **documentos da empresa**.

**6. Responda à entrevista por blocos.** O agente pergunta em partes:
identificação do processo, versão da empresa sobre a relação de trabalho,
jornada, rescisão, condições de trabalho e provas disponíveis. Aqui é onde a
defesa se ganha — quanto mais preciso o relato do preposto e mais completo o
conjunto de documentos, mais forte a peça.

**7. Aprove o mapa de defesa.** Antes de redigir, ele mostra: a **linha de
defesa** escolhida (vínculo formal, prestação eventual/"bicos", ilegitimidade
passiva, dona da obra), as preliminares cabíveis, as teses subsidiárias, as
provas a requerer, os **documentos que ainda faltam** e o **risco residual
estimado**. Você confirma ou ajusta.

**8. Receba a entrega:**
- o arquivo **`.docx` editável** (enviado no chat e **salvo na pasta do processo
  no Drive**), com a tabela de impugnação pedido a pedido;
- no chat, um resumo curto, a **lista de documentos a juntar** e o bloco
  **"Pontos de atenção antes do protocolo"**.

**9. Revise e protocole.** Confira as datas e os valores com o cliente, valide as
citações marcadas `[CONFERIR]` — em especial o **número da Portaria do Foro de
Taquara** e o **número do Tema do TST** — e ajuste o que quiser no Word.

## Documentos que valem ouro (peça ao cliente antes)

- Carta de preposto e procuração.
- Ficha de Registro de Empregado / CTPS Digital, TRCT, holerites.
- **Pedido de demissão assinado**, se houver.
- **Relatório de todos os pagamentos feitos ao autor** (PIX, caixa, recibos), com
  datas e valores — é a prova central quando a defesa é de prestação eventual.
- Comprovante do **quadro de pessoal** (menos de 20 empregados) no período — é o
  que sustenta a tese mais valiosa em horas extras.
- Extrato do FGTS, fichas de entrega de EPI, CCT do período.
- CTPS do novo emprego do autor, quando houver.

## Exemplo de mensagem para começar

> `/contestacao-trabalhista`
> Processo 0020506-65.2026.5.04.0384, 4ª VT de Taquara, sumaríssimo. Reclamante
> Fulano de Tal, pede vínculo de 18/12 a 17/03 como carpinteiro e salário de
> R$ 4.400. Na real ele fez só alguns dias de bico, pago por diária via PIX.
> Audiência dia [data]. A pasta do processo no Drive é [colar link] — a inicial e
> os relatórios de pagamento estão lá.

O agente assume a partir daí: dissecação da inicial, mapa de defesa, redação,
geração do `.docx` e arquivamento no Drive.

## Lembretes

- **Nunca inventa fatos nem jurisprudência.** A versão dos fatos vem dos
  documentos e do preposto; o que não estiver verificado no banco sai marcado
  `[CONFERIR]`. Se um documento ainda não chegou, a peça sai com
  `[doc. anexo — CONFIRMAR JUNTADA]` em vermelho.
- **Se os documentos da empresa contrariam a versão pedida, o agente avisa** e
  propõe a defesa tecnicamente viável — negar o que o próprio papel prova
  destrói a peça inteira.
- **A peça é minuta de apoio:** a revisão e o protocolo são sempre seus.
- Se o conector do Drive estiver fora do ar, o agente entrega o `.docx` pelo chat
  e avisa que não conseguiu salvar no Drive.
