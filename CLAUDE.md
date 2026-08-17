# Projeto Advogado Róger Bento — regras permanentes

Este projeto elabora **petições iniciais de reclamatória trabalhista** (foco
TRT-4/RS) por meio da skill `inicial-trabalhista`. As regras abaixo são
**padrão fixo do escritório** e valem para toda peça, em qualquer sessão.

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
- cálculos dependentes de dado/perícia: `[CÁLCULO A CONFIRMAR]`.

Assim o advogado vê de imediato, em vermelho, tudo que falta completar antes do
protocolo. Nunca "invente" um dado para preencher a lacuna — deixe o colchete
vermelho.

## Padrão de formatação (calibrado sobre modelo real do escritório)

A4, margens 2 cm; Times New Roman 12; justificado; entrelinha 1,5; recuo de 1ª
linha de 1,5 cm no corpo e nos títulos (títulos de tópico em negrito);
endereçamento em negrito; "RECLAMAÇÃO TRABALHISTA" e a assinatura (cidade/data,
nome, OAB) centralizados em negrito; ementas com recuo à esquerda de 4 cm;
separação de blocos por linha em branco. Ver `modelos/MODELO-INICIAL-REFERENCIA`.

## Jurisprudência (INEGOCIÁVEL)

Nunca inventar súmula, OJ, tese ou acórdão. Só citar o que estiver `VERIFICADO`
no diretório `jurisprudencia/` (ver `jurisprudencia/README.md` e a ordem de
confiança). O que não estiver verificado entra na peça como `[CONFERIR]`
(vermelho). A peça é sempre **minuta de apoio**: revisão e protocolo são do
advogado.

## Cálculo em todo pedido (INEGOCIÁVEL)

Toda peça traz **valor estimado ao lado de cada pedido** e o **valor da causa**
ao final (ver `references/liquidacao-e-calculos.md`).
