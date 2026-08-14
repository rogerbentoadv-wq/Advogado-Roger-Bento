# Rotina de atualização da jurisprudência

Protocolo executado a cada passada de verificação (manual ou agendada). O
objetivo é **confirmar procedência** e **capturar revisões**, nunca gerar
enunciado de memória.

## Passos

1. **Varredura das entradas "A CONFERIR".** Para cada uma, pesquisar na web o
   número + tema; se a fonte confirmar o teor, transcrever fielmente, registrar
   `Fonte`, `Verificado em` e mudar `Status` para VERIFICADO. Se não confirmar,
   **manter A CONFERIR** (nunca promover no escuro).

2. **Revisões e cancelamentos.** Pesquisar por resoluções recentes do TST,
   cancelamento/conversão de OJs em súmula, e decisões do STF que suspendam ou
   superem enunciados (ex.: SV 4 → Súmula 228). Marcar SUSPENSO/SUPERADO quando
   for o caso.

3. **Temas sensíveis (prioridade máxima).** Reconferir sempre:
   - Correção monetária e juros (ADCs 58/59 e alterações legislativas);
   - Base de cálculo da insalubridade (SV 4 / Súmula 228);
   - Intervalo intrajornada pós-Reforma (art. 71, §4º x Súmula 437);
   - Vínculo em plataformas/aplicativos (STF/TST);
   - Tema 1.046 do STF (normas coletivas).

4. **TRT-4.** Tentar confirmar súmulas/teses regionais. Registrar honestamente
   quando a fonte não permitir confirmação (site oficial bloqueado neste
   ambiente).

5. **Commit.** Registrar as mudanças com mensagem clara (ex.: "jurisprudência:
   verifica Súmulas 85, 366 e 431; marca Súmula 228 como suspensa").

## Honestidade obrigatória

- Fonte de terceiros **confirma**, não **oficializa**: mantenha o dever de
  conferência final pelo advogado.
- Sem confirmação → sem promoção a VERIFICADO.
- Em dúvida entre duas redações, registre ambas e marque A CONFERIR.

## Sobre "todo dia"

Súmulas e OJs mudam pouco; a passada diária raramente altera algo nelas. O valor
diário está em **monitorar os temas sensíveis** e novos precedentes. Se a
automação diária estiver ligada (ver seção de agendamento no README do projeto),
a maioria das execuções terminará com "nenhuma mudança" — e tudo bem: isso é
sinal de que o banco está estável, não de que faltou trabalho.
