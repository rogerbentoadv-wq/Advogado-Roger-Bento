# Advogado Roger Bento — Agente de Peças Trabalhistas

Projeto para elaboração assistida de **petições iniciais de reclamatória
trabalhista** (polo ativo / reclamante), com foco no **TRT da 4ª Região (Rio
Grande do Sul)**.

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

## Próximos passos

1. **Enviar peças-modelo:** forneça 1 a 3 iniciais que você redigiu e considera
   bem escritas. O agente extrai seu padrão de estrutura, vocabulário e teses e
   preenche `references/estilo-do-escritorio.md`, passando a escrever no *seu*
   jeito.
2. **Ampliar as teses:** conforme surgirem casos, novos arquivos de tese podem
   ser adicionados em `references/teses/` (ex.: equiparação salarial, dano moral,
   acidente de trabalho, PLR, comissões).
3. **Modelos de cálculo:** opcionalmente, incluir planilhas/roteiros de
   liquidação padronizados.

## Aviso importante

O material produzido é **minuta de apoio**. O advogado responsável revisa,
confere fundamentos e cálculos, valida citações de súmulas/OJs (marcadas com
`[CONFERIR]` quando houver dúvida) e assume a responsabilidade profissional pelo
protocolo. O conteúdo jurídico reflete a legislação e a jurisprudência
consolidadas até a data de elaboração e deve ser conferido diante de alterações
legislativas e da orientação atual do TST e do TRT-4.
