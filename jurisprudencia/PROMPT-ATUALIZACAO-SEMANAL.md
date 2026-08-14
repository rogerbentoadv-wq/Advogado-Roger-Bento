# Prompt para o agendamento semanal (colar no trigger/automação)

Este é o texto a ser usado num **agendamento (trigger) do Claude Code na web**,
apontando para este repositório. Sugestão de cadência: **1x por semana** (ex.:
segunda-feira de manhã). Cada disparo abre uma sessão que executa a rotina e
faz commit se houver mudança.

---

## Prompt

```
Você está fazendo a passada SEMANAL de atualização do banco de jurisprudência
deste projeto (advogado trabalhista, foco TRT-4/RS).

Siga estritamente jurisprudencia/ROTINA-ATUALIZACAO.md. Em resumo:

1. Abra os arquivos em jurisprudencia/ e percorra as entradas com Status
   "A CONFERIR". Para cada uma, faça WebSearch pelo número + tema. Se uma fonte
   confiável confirmar o teor, transcreva fielmente e promova para VERIFICADO,
   registrando Fonte (URL) e "Verificado em" com a data de hoje. Se NÃO
   confirmar, mantenha "A CONFERIR" — nunca promova no escuro.

2. Reconfira os TEMAS SENSÍVEIS (mesmo que já verificados): correção monetária e
   juros (ADCs 58/59 e leis posteriores), base de cálculo da insalubridade
   (SV 4 / Súmula 228), intervalo intrajornada pós-Reforma (art. 71, §4º x
   Súmula 437), vínculo em plataformas/aplicativos, e Tema 1.046 do STF. Procure
   revisões, resoluções do TST e decisões recentes do STF que alterem, suspendam
   ou superem enunciados. Marque SUSPENSO/SUPERADO quando for o caso.

3. Nunca invente enunciado. Fonte de terceiros confirma, não oficializa: mantenha
   o dever de conferência final pelo advogado.

4. Se houver qualquer mudança, faça commit no branch de trabalho com mensagem
   clara resumindo o que foi verificado/alterado, e push. Se nada mudou, apenas
   registre em resposta "nenhuma alteração nesta passada" e não faça commit.

Trabalhe apenas dentro do diretório jurisprudencia/. Não altere as skills nem as
peças nesta rotina.
```

---

## Como configurar o agendamento (interface web)

1. No Claude Code na web, abra este projeto/repositório.
2. Procure a opção de **Agendar / Automação / Schedule** (cria uma sessão
   recorrente).
3. Defina a frequência **semanal** e cole o prompt acima.
4. Salve. A cada semana, uma sessão nova roda a rotina e commita as mudanças.

> Observação honesta: a verificação usa busca na web (fontes secundárias), pois
> os sites oficiais estão bloqueados neste ambiente. A maioria das passadas
> semanais terminará sem mudança — sinal de banco estável, não de falha.
