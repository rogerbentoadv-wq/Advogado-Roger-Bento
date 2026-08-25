# Projeto Advogado Róger Bento — regras permanentes

Este projeto elabora **peças trabalhistas** (foco TRT-4/RS) por meio de duas
skills:

- `inicial-trabalhista` — **polo ativo**: petições iniciais de reclamatória.
- `contestacao-trabalhista` — **polo passivo**: contestações em defesa da
  **BS Construções e Reformas Ltda.**

As regras abaixo são **padrão fixo do escritório** e valem para **toda peça**
(inicial ou contestação), em qualquer sessão.

## Entrega da peça (INEGOCIÁVEL)

1. **Formato:** toda peça é entregue como **arquivo `.docx` editável**, nunca só
   texto no chat.
2. **Geração:** o `.docx` é gerado **exclusivamente** pelo conversor
   `python3 scripts/gerar_docx.py <peca>.md <peca>.docx`. Nunca gere o `.docx`
   de outra forma, nem cole markdown cru (`**`, `#`, `|`) no resultado.
3. **Papel timbrado SEMPRE:** o conversor aplica automaticamente o cabeçalho com
   a **logo do escritório** (`assets/logo-cabecalho.png`) e o **rodapé de
   contato** (`assets/rodape.png`). Toda peça sai com o timbrado. Se o `.docx`
   sair sem o logo, foi porque não passou pelo conversor ou os arquivos de
   `assets/` não estavam presentes — corrija antes de entregar.
4. **Arquivamento:** após enviar o `.docx` ao usuário, salve-o também na **pasta
   do cliente no Google Drive** indicada no início do caso.

## Campos a preencher / a conferir → VERMELHO (INEGOCIÁVEL)

Sempre que faltar uma informação na petição, ou algo precisar de conferência,
marque **entre colchetes `[...]`**. O conversor deixa **todo texto entre
colchetes em VERMELHO** automaticamente. Use isto para:

- dados ausentes: `[NOME COMPLETO]`, `[CPF]`, `[ENDEREÇO]`, `[DATA DE ADMISSÃO]`;
- conferência de jurisprudência: `[CONFERIR: Súmula X]`;
- cálculos dependentes de dado/perícia: `[CÁLCULO A CONFIRMAR]`;
- na contestação: documentos ainda não recebidos do cliente
  (`[doc. anexo — CONFIRMAR JUNTADA]`) e números de tema/portaria
  (`[CONFERIR Nº DA PORTARIA]`).

Assim o advogado vê de imediato, em vermelho, tudo que falta completar antes do
protocolo. Nunca "invente" um dado para preencher a lacuna — deixe o colchete
vermelho.

## Padrão de formatação (calibrado sobre modelo real do escritório)

A4, margens 2 cm; Times New Roman 12; justificado; entrelinha 1,5; recuo de 1ª
linha de 1,5 cm no corpo e nos títulos (títulos de tópico em negrito);
endereçamento em negrito; "RECLAMAÇÃO TRABALHISTA" ou "CONTESTAÇÃO" e a
assinatura (cidade/data, nome, OAB) centralizados em negrito; cabeçalho dos autos
("Processo nº:", "Rito:", "Reclamante:", "Reclamada:") justificado e sem recuo;
ementas com recuo à esquerda de 4 cm; separação de blocos por linha em branco.
Ver `modelos/MODELO-INICIAL-REFERENCIA` e
`.claude/skills/contestacao-trabalhista/modelos/MODELO-CONTESTACAO`.

## Jurisprudência (INEGOCIÁVEL)

Nunca inventar súmula, OJ, tese ou acórdão. Só citar o que estiver `VERIFICADO`
no diretório `jurisprudencia/` (ver `jurisprudencia/README.md` e a ordem de
confiança). O que não estiver verificado entra na peça como `[CONFERIR]`
(vermelho). A peça é sempre **minuta de apoio**: revisão e protocolo são do
advogado.

## Cálculo em todo pedido — iniciais (INEGOCIÁVEL)

Toda **inicial** traz **valor estimado ao lado de cada pedido** e o **valor da
causa** ao final (ver `references/liquidacao-e-calculos.md`).

## Impugnação específica em toda contestação (INEGOCIÁVEL)

Toda **contestação** enfrenta a inicial **item a item** e fecha com a **tabela de
impugnação pedido a pedido** (um pedido por linha, na mesma letra da inicial,
inclusive os processuais). O que não é impugnado especificamente presume-se
verdadeiro (art. 341 do CPC c/c art. 769 da CLT). Nenhum valor da inicial passa
sem impugnação, e toda tese subsidiária vem precedida da ressalva de
eventualidade (art. 336 do CPC).

## Coerência da versão dos fatos na defesa (INEGOCIÁVEL)

Na contestação, a versão dos fatos vem **dos documentos da empresa e do
preposto** — nunca da criatividade. É vedado negar fato que os próprios
documentos da empresa comprovam (registro, pagamento, CAT emitida): a
contradição documental destrói a defesa e expõe à litigância de má-fé
(arts. 793-A a 793-C da CLT). Linhas de defesa incompatíveis nunca convivem como
tese principal na mesma peça.
