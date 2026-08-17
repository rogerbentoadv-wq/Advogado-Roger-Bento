# Fluxo de Agendamento — Google Agenda + Google Meet

Regras e passos para transformar o "sim" do lead em um evento real, com Meet, na
agenda do Dr. Roger. Parâmetros (janelas, duração, agendas) em
`parametros-operacionais.md`.

## Regras de disponibilidade (resumo)
- **Duração:** 45 minutos.
- **Fuso:** `America/Sao_Paulo`.
- **Janela padrão de atendimento:** Segunda a sexta, **9h–12h** e **14h–18h**.
- **Exceções (só com confirmação explícita do lead E ciência de que é exceção):**
  após as **18h** em dias úteis, e **sábado 9h–12h**. Nunca ofereça exceção como
  primeira opção; só se o lead pedir ou recusar todas as janelas padrão.
- **Nunca** sugira domingo, feriado (a agenda "Feriados no Brasil" está na conta)
  ou horário de almoço (12h–14h).
- **Antecedência mínima:** ofereça slots com pelo menos ~1h de folga do horário
  atual, para dar tempo de o lead se organizar (ajuste conforme a operação).

## Passo a passo

### 1. Descobrir horários livres (checar as DUAS agendas)
Considere compromissos de **ambas** as agendas para não marcar em cima de nada:
- `rogerbentoadv@gmail.com` (principal)
- `d0ja89u9eq4oi1hl9hiu5ic9k0un8rb9@import.calendar.google.com` (ADVBOX agenda)

Duas formas:

**a) `suggest_time`** (mais direto) — encontra janelas livres cruzando as agendas:
```
mcp__Google_Calendar__suggest_time(
  attendeeEmails = ["rogerbentoadv@gmail.com",
                    "d0ja89u9eq4oi1hl9hiu5ic9k0un8rb9@import.calendar.google.com"],
  durationMinutes = 45,
  startTime = <agora>, endTime = <fim da janela, ex.: +3 dias>,
  timeZone = "America/Sao_Paulo",
  preferences = { startHour: "09:00", endHour: "18:00", excludeWeekends: true }
)
```
> `preferences` não consegue expressar o buraco do almoço; ao montar as ofertas,
> **descarte manualmente** qualquer slot entre 12h e 14h.

**b) `list_events`** (conferência fina) — liste os eventos de cada agenda no dia
alvo e identifique os vãos livres dentro de 9h–12h / 14h–18h.

### 2. Oferecer 2–3 janelas ao lead
Traduza os slots livres em linguagem natural (Mensagem 4 do roteiro):
> "Posso te encaixar **hoje às 15h**, ou prefere **amanhã às 10h**?"

Ofereça no máximo 2–3 opções para não gerar paralisia de escolha. Se o lead
recusar todas, ofereça a próxima janela livre; só então considere exceção
(após 18h / sábado), deixando claro que é um encaixe especial.

### 3. Ao confirmar o horário → criar o evento
Antes de criar, **releia a agenda** para o slot escolhido (evita conflito se
algo foi marcado no intervalo). Depois:
```
mcp__Google_Calendar__create_event(
  calendarId = "rogerbentoadv@gmail.com",     // sempre marca na PRINCIPAL
  summary    = "Análise Jurídica Gratuita — [NOME DO LEAD] (Dr. Roger Bento)",
  startTime  = "AAAA-MM-DDTHH:MM:00-03:00",
  endTime    = "<+45min>",
  timeZone   = "America/Sao_Paulo",
  addGoogleMeetUrl = true,                     // gera o link do Meet
  attendees  = [ { email: "<e-mail do lead, se houver>", displayName: "[NOME]" } ],
  description = "<ver modelo abaixo>",
  overrideReminders = [ { method: "popup", minutes: 30 },
                        { method: "email", minutes: 60 } ]
)
```

**Modelo de descrição do evento:**
```
Lead: [NOME] — WhatsApp: [telefone]
Origem: Kinbox (lead trabalhista)
Resumo do caso (relato do lead): [1–3 linhas do que o lead contou]
Reunião de análise gratuita, individual e reservada, por Google Meet.
Qualificação (3 pilares): problema ✔ / direito ✔ / intenção ✔
SDR responsável: [NOME DA SDR]
```

### 4. Guardar o link do Meet
O `create_event` retorna o evento com a URL do Meet. **Guarde essa URL** — ela é
o `[link-da-reuniao]` usado no lembrete de 30 min antes (ver
`rotina-follow-up.md`). Confirme o agendamento ao lead (Mensagem 5) e siga para a
mensagem pós-agendamento.

## Se o e-mail do lead não estiver disponível
Muitos leads chegam só com WhatsApp. Sem e-mail, o convite do Google não vai
automaticamente para ele — por isso o **link do Meet é enviado pelo WhatsApp** no
lembrete de 30 min. Ainda assim, crie o evento (com o lead no título/descrição)
para reservar a agenda do Dr. Roger.

## Honestidade operacional
- Se o **conector do Google Agenda não estiver ativo** na sessão, **não afirme
  que agendou**. Informe o horário escolhido, monte a confirmação e avise que a
  criação do evento depende do conector ativo (ou de fazê-lo manualmente).
- Nunca invente link de Meet. Se o evento não foi criado, não há link.
