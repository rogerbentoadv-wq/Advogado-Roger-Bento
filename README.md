# Advogado Roger Bento — Agentes Trabalhistas

Projeto com **dois agentes** para o escritório Roger Bento de Souza Advogados:

1. **`inicial-trabalhista`** — elaboração assistida de **petições iniciais de
   reclamatória trabalhista** (polo ativo / reclamante), foco no **TRT da 4ª
   Região (RS)**. Detalhes abaixo.
2. **`atendimento-leads`** — **agente SDR de vendas** que atende leads
   trabalhistas no WhatsApp/Kinbox, qualifica (3 pilares), contorna objeções e
   **agenda a análise gratuita com o Dr. Roger** no Google Agenda + Google Meet.
   Ver [`.claude/skills/atendimento-leads/SKILL.md`](.claude/skills/atendimento-leads/SKILL.md)
   e o guia de integração em
   [`references/integracao-kinbox.md`](.claude/skills/atendimento-leads/references/integracao-kinbox.md).

---

## Agente de Peças (`inicial-trabalhista`)

Elaboração assistida de **petições iniciais de reclamatória trabalhista** (polo
ativo / reclamante), com foco no **TRT da 4ª Região (Rio Grande do Sul)**.

O coração do projeto é a skill **`inicial-trabalhista`**, que faz o Claude Code
atuar como um(a) advogado(a) trabalhista sênior (25+ anos) e conduzir todo o
fluxo: entrevista de fatos → estratégia de teses → redação da peça → liquidação
e valor da causa → revisão crítica.

## Como usar

Dentro do Claude Code, na raiz deste projeto:

```
/inicial-trabalhista
```

ou simplesmente descreva o caso ("preciso de uma inicial para um cliente
dispensado sem justa causa com horas extras não pagas...") que a skill é
acionada automaticamente.

O agente vai **entrevistar você por blocos**, montar um mapa de teses para sua
aprovação e só então redigir a peça completa.

## O que já está incluído

| Arquivo | Conteúdo |
|---|---|
| `.claude/skills/inicial-trabalhista/SKILL.md` | Persona, princípios e fluxo de trabalho do agente |
| `references/estrutura-da-peca.md` | Anatomia técnica da inicial + checklist pós-Reforma |
| `references/checklist-entrevista.md` | Roteiro de coleta de fatos com o cliente |
| `references/teses/verbas-rescisorias.md` | Fundamentos: rescisórias, aviso, 13º, férias, FGTS, multas |
| `references/teses/jornada-horas-extras.md` | Horas extras, intervalos, adicional noturno, sobreaviso |
| `references/teses/insalubridade-periculosidade.md` | Adicionais, perícia, base de cálculo, EPI |
| `references/teses/vinculo-e-rescisao-indireta.md` | Vínculo, terceirização, rescisão indireta, estabilidades |
| `references/estilo-do-escritorio.md` | **A calibrar** com as peças-modelo do escritório |
| `jurisprudencia/` | Banco de súmulas/OJs/teses com **procedência** (fonte + data + status) |

## Banco de jurisprudência e a regra "nunca inventar"

O diretório `jurisprudencia/` é a **única fonte autorizada** de súmulas, OJs,
súmulas vinculantes e teses que o agente pode citar. A regra é inegociável:

> Nada é citado numa peça se não estiver no banco com Status `VERIFICADO`. O que
> não estiver verificado sai marcado como `[CONFERIR]` para o advogado validar.

Isso é o que realmente impede a invenção de jurisprudência: o agente cita do
banco (com fonte registrada), não de memória. Veja `jurisprudencia/README.md`.

### Limites honestos deste ambiente
- **Sites oficiais bloqueados:** o acesso direto a `tst.jus.br` / `trt4.jus.br`
  está bloqueado pela política de rede. A verificação usa **busca na web**, que
  retorna fontes secundárias (Jusbrasil, LexML, etc.) — boas para conferir, mas
  que **não substituem o texto oficial**. Toda citação exige conferência final.
- **"Atualização diária":** possível como monitoramento dos temas sensíveis, mas
  súmulas/OJs mudam pouco — a maioria das passadas termina sem alteração.
- **Não há acesso ao Google Drive `G:\`:** aquele caminho é local do computador
  do escritório e não é alcançável deste servidor na nuvem (ver Próximos passos).

## Próximos passos

1. **Enviar as peças-modelo (bloqueio atual):** o caminho `G:\Meu Drive\...` não
   é acessível daqui. Duas formas de resolver:
   - **Anexar** 1 a 3 iniciais direto nesta conversa (PDF/DOCX), ou colocá-las no
     próprio repositório numa pasta `modelos/`; ou
   - **Conectar o conector de Google Drive** na sua conta claude.ai — aí passo a
     ler a pasta `ESCRITORIO/PEÇAS FINALIZADAS DR ALLAN/PROTOCOLADAS` na nuvem.

   Com as peças em mãos, extraio o padrão e preencho
   `references/estilo-do-escritorio.md`.
2. **Ligar (ou não) a atualização automática:** posso criar um agendamento diário
   que dispara uma sessão para rodar a rotina de verificação da jurisprudência e
   commitar as mudanças. Isso consome uso da sua conta e depende da rede; decida
   se compensa a frequência diária ou algo mais espaçado.
3. **Ampliar as teses e o banco:** conforme surgirem casos, acrescentar teses
   (equiparação, dano moral, acidente, PLR, comissões) e verificar mais entradas.

## Aviso importante

O material produzido é **minuta de apoio**. O advogado responsável revisa,
confere fundamentos e cálculos, valida citações de súmulas/OJs (marcadas com
`[CONFERIR]` quando houver dúvida) e assume a responsabilidade profissional pelo
protocolo. O conteúdo jurídico reflete a legislação e a jurisprudência
consolidadas até a data de elaboração e deve ser conferido diante de alterações
legislativas e da orientação atual do TST e do TRT-4.
