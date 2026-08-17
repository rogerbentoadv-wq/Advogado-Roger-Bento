# Follow-ups, Pós-Agendamento e Lembretes

Sequência de mensagens **depois** que o horário é oferecido/confirmado. Mantêm o
lead engajado e reduzem o "no-show".

## A) Follow-up de inatividade (antes de fechar o horário)
Se o lead ficou **10 minutos sem responder** após a oferta de horário:
> Qual horário seria melhor para você, [nome]?

Se seguir sem resposta, faça no máximo mais 1 tentativa algumas horas depois
(ou no período seguinte), leve e sem pressão. Não bombardeie.

## B) Mensagem pós-agendamento (logo após confirmar)
Enviada no momento em que o lead confirma a reunião:
> Ah, e aproveitando, [nome] 😊
>
> Vou deixar aqui também as redes oficiais do Dr. Roger Bento, onde **ele**
> compartilha orientações jurídicas, dicas importantes e conteúdos sobre
> direitos em diversas áreas ⚖️
>
> Assim você pode acompanhar melhor o trabalho **dele** e ficar por dentro de
> informações que ajudam muitas pessoas no dia a dia.
>
> 👉 Instagram: https://www.instagram.com/advogadorogerbento/
> 👉 TikTok: https://www.tiktok.com/@advogadorogerbento
> 👉 Facebook: https://www.facebook.com/advogadorogerbento
>
> Vale muito a pena acompanhar 😊
> Muitas pessoas conseguem esclarecer dúvidas importantes e entender melhor
> seus direitos através dos conteúdos publicados por lá.

> Links oficiais registrados em `parametros-operacionais.md`.

## C) Rotina no DIA da reunião

### C.1 — Lembrete às 9h da manhã
> Bom dia, [nome]! ☀️
> Passando aqui pra confirmar sua análise jurídica com o Dr. Roger Bento,
> especialista em Direito Trabalhista.
> A reunião está agendada para **hoje, às [X horas]**, e será o momento em que
> **ele** vai avaliar seu caso individualmente pra identificar quais direitos e
> valores a empresa pode estar te devendo.
> É uma conversa rápida, mas muito importante. Podemos contar com sua presença?

Escalonamento de confirmação:
- **Sem confirmação em até 1h** → ligar para o lead buscando a confirmação.
- **Não atendeu a ligação** → enviar: *"[nome]? Está por aí?"*

### C.2 — Lembrete 30 minutos antes
> Olá, [nome]! ⏰
> Em 30 minutos começa sua análise jurídica com o Dr. Roger Bento (às [hora]).
> É só clicar neste link: **[link-da-reuniao]**
> (Entre 2 min antes pra testar áudio e vídeo.)
> Esta é uma agenda exclusiva e individual com o Dr. Roger — **ele** já está com
> tudo organizado pra falar do seu caso! Combinado, [nome]?

> `[link-da-reuniao]` = a URL do Google Meet gerada na criação do evento
> (ver `fluxo-agendamento.md`).

## D) Pedido de avaliação no Google (após o atendimento)
Mensagem **separada**, enviada **depois de uma boa experiência** — de preferência
após a reunião acontecer (ou após um atendimento nota 10). Não envie junto com a
mensagem das redes (B); é um segundo momento.
> [nome], posso te pedir um favor? 🙏
>
> Seria possível você tirar 1 minuto para nos avaliar no Google? 🤩
>
> Esta avaliação é super importante para nós sabermos se estamos no caminho
> certo e buscarmos cada dia mais um atendimento de excelência para você.
>
> Segue o link, é só abrir, clicar em avaliação, escolher a quantidade de
> estrelas e comentar sobre sua experiência conosco. 👇
>
> https://g.page/r/Cd4KXZi07M4AEB0/review

> No Kinbox, `[nome]` corresponde à variável de mescla `{{first_name}}`.

## Observação sobre automação dos lembteres
Quando este agente roda **dentro do Kinbox/automação**, os lembretes das 9h e dos
30 min são disparados por **agendamento/gatilho de tempo** (o Kinbox tem gatilhos
por horário; numa automação n8n/Make, um nó de espera/cron). Quando roda
manualmente aqui, a SDR/operador dispara nos horários. Ver `integracao-kinbox.md`.
