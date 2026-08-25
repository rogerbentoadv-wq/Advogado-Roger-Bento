# Advogado Roger Bento — Agente de Peças Trabalhistas

Projeto para elaboração assistida de **peças trabalhistas** com foco no **TRT da
4ª Região (Rio Grande do Sul)**, nos dois polos:

| Skill | Polo | O que faz |
|---|---|---|
| **`inicial-trabalhista`** | ativo (reclamante) | Petições iniciais de reclamatória: entrevista de fatos → estratégia de teses → redação → liquidação e valor da causa → revisão crítica |
| **`contestacao-trabalhista`** | passivo (reclamada) | Contestações em defesa da **BS Construções e Reformas Ltda.**: dissecação da inicial → escolha da linha de defesa → preliminares, impugnação de provas e mérito → tabela pedido a pedido → revisão crítica |

Ambas fazem o Claude Code atuar como advogado(a) trabalhista sênior, entregam a
peça em **`.docx` timbrado e editável** e só citam jurisprudência do banco
`jurisprudencia/`.

## Como usar

Dentro do Claude Code, na raiz deste projeto:

```
/inicial-trabalhista        # do lado do trabalhador
/contestacao-trabalhista    # defesa da BS Construções
```

ou simplesmente descreva o caso ("preciso de uma inicial para um cliente
dispensado sem justa causa com horas extras não pagas...", "chegou uma
reclamatória contra a BS na 4ª Vara de Taquara, preciso da contestação") que a
skill certa é acionada automaticamente.

O agente vai **entrevistar você por blocos**, montar um mapa de teses (ou de
defesa) para sua aprovação e só então redigir a peça completa.

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

### Defesa (skill `contestacao-trabalhista`)

| Arquivo | Conteúdo |
|---|---|
| `.claude/skills/contestacao-trabalhista/SKILL.md` | Persona de defesa, linhas de defesa e fluxo de trabalho |
| `references/cliente-bs-construcoes.md` | Dados fixos da ré, particularidades e documentos a pedir |
| `references/checklist-analise-inicial.md` | Roteiro de coleta e dissecação da inicial |
| `references/estrutura-da-contestacao.md` | Anatomia da peça, capítulo a capítulo |
| `references/matriz-de-defesas.md` | Do pedido do autor à tese de defesa, em uma tabela |
| `references/estilo-da-defesa.md` | Estilo calibrado nas contestações protocoladas |
| `references/teses/` | Preliminares, vínculo/eventualidade, jornada, insalubridade, rescisão/multas, danos morais/acidente, impugnação de provas, honorários |
| `modelos/MODELO-CONTESTACAO.md` (e `.docx`) | Esqueleto pronto para preencher |
| `jurisprudencia/defesa-do-escritorio.md` | Teses de defesa já protocoladas pela banca, com procedência e alertas de conferência |

As quatro contestações reais que calibraram a skill (processos de Edson
Mauricio Nunes de Souza, Vanderlei dos Santos, Alcides Natalino Alves e Lucas
Rodrigues Rosa) são a fonte do estilo, das teses e do banco de defesa.

## Banco de jurisprudência e a regra "nunca inventar"

O diretório `jurisprudencia/` é a **única fonte autorizada** de súmulas, OJs,
súmulas vinculantes e teses que o agente pode citar. A regra é inegociável:

> Nada é citado numa peça se não estiver no banco com Status `VERIFICADO`. O que
> não estiver verificado sai marcado como `[CONFERIR]` para o advogado validar.

Na defesa, três itens saem **sempre** com `[CONFERIR]`, por serem os erros mais
fáceis e mais caros: o **número do tema repetitivo** (Tema 190 do IRR/TST), o
**número da Portaria da Direção do Foro de Taquara** (as peças da banca divergem
entre 01/2018 e 03/2018) e os **itens sensíveis** (OJ 394, SV 4, ADI 5766,
ADCs 58/59).

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
