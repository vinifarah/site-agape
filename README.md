# Protótipo — Ágape Saúde e Segurança do Trabalho

Protótipo estático em **HTML/CSS puro**, para aprovação visual do responsável
pelo projeto e do cliente. É a especificação visual que depois será reconstruída
no WordPress com Elementor.

**Abra o `index.html` com duplo clique.** Não precisa de servidor, internet ou
instalação. (Sem internet as fontes do Google caem para a fonte de sistema — o
layout continua idêntico.)

---

## 1. As 11 páginas

| Página | Arquivo | Slug preservado |
|---|---|---|
| Home | `index.html` | `/` |
| Sobre Nós | `sobre-nos/index.html` | `/sobre-nos/` |
| Serviços (índice) | `servicos/index.html` | `/servicos/` |
| Medicina Ocupacional | `medicina-ocupacional-empresas/index.html` | `/medicina-ocupacional-empresas/` |
| Segurança do Trabalho | `seguranca-trabalho-empresas/index.html` | `/seguranca-trabalho-empresas/` |
| eSocial SST | `esocial-sst-empresas/index.html` | `/esocial-sst-empresas/` |
| Treinamentos NR’s | `treinamentos-nrs-empresas/index.html` | `/treinamentos-nrs-empresas/` |
| Gestão de Ambulatório | `gestao-ambulatorio-empresas/index.html` | `/gestao-ambulatorio-empresas/` |
| Clínica Credenciada | `clinica-credenciada/index.html` | `/clinica-credenciada/` |
| Contato (2 abas) | `contato/index.html` | `/contato/` |
| Política de Privacidade | `politica-de-privacidade/index.html` | **página nova** (substitui o PDF solto) |

A estrutura de pastas espelha os slugs justamente para não haver dúvida na hora
de recriar as URLs no WordPress.

---

## 2. Arquivos do projeto

```
index.html + pastas de slug   ← O PROTÓTIPO (é isto que se entrega/aprova)
assets/css/style.css          ← todo o CSS, um arquivo só
assets/img/                   ← arte do hero (SVG vetorial)
assets/logos/                 ← 99 logos de clientes, versão web (~2 MB)
png-clientes/                 ← os originais como você enviou (não publicar)
build.py                      ← gerador: monta as páginas
blocos.py                     ← os 9 blocos reutilizáveis + dados de contato
conteudo.py                   ← todos os textos do site
clientes.py                   ← a carteira: arquivo + nome + setor
otimizar_logos.py             ← gera as versões web a partir dos originais
```

### Os logos dos clientes

Os originais chegaram em `png-clientes/`, numerados de 1 a 107:

- **1 a 8** são composições (várias marcas numa imagem só) — ficaram de fora,
  porque não servem como logo individual numa faixa.
- **9 a 107** são um logo por arquivo. São os **99** usados no site.

`python otimizar_logos.py` transforma os originais nas versões que o site
carrega: recorta a moldura vazia, reduz para 168px de altura e salva em tons
de cinza com transparência. **De 10,2 MB para 1,9 MB** — a diferença entre uma
faixa de 99 logos que carrega e uma que trava a página. Rode de novo sempre que
trocar ou acrescentar um original.

O nome de cada empresa está em `clientes.py` e vira o texto ALT da imagem. Um
único arquivo (o `85.png`, uma marca em "A" com barras diagonais) não deu para
identificar com certeza e ficou com ALT genérico — vale confirmar com o cliente.

O HTML é gerado, não escrito à mão, para que header, footer, formulário e as
6 páginas de serviço fiquem **rigorosamente idênticos** entre si.

**Para alterar um texto:** edite `conteudo.py` e rode `python build.py`.
**Para alterar o visual:** edite `assets/css/style.css` (não precisa rodar nada).

> Depois da aprovação, o que vai para o Elementor é o HTML/CSS gerado.
> Os três `.py` se aposentam — não fazem parte do site.

---

## 3. Do protótipo para o Elementor

**Cores e tipografia → Estilos Globais.** O bloco 01 do `style.css` é uma lista
de variáveis CSS com correspondência 1:1 com os Estilos Globais do Elementor.
Trocar um hex lá é o mesmo que trocar aqui.

**Seções → Containers.** Cada `<section class="secao">` é um container. Nada
depende de JavaScript para existir:

| No protótipo | No Elementor |
|---|---|
| Menu mobile (checkbox + CSS) | Menu responsivo nativo do widget Nav Menu |
| FAQ com `<details>` | Widget Accordion |
| Abas do Contato (radio + CSS) | Widget Tabs |
| Banner LGPD (checkbox + CSS) | Plugin de consentimento |
| Formulário (visual) | Fluent Forms ou WPForms |
| Grids `.grade--2/3/4` | Container com 2, 3 ou 4 colunas |

---

## 3.1. Identidade visual aplicada

O protótipo segue o guia **"Identidade Visual — Referência para interface web"**
enviado pelo cliente. O que veio de lá e onde está:

| Diretriz do guia | Onde foi aplicada |
|---|---|
| Paleta oficial (6 cores) | Bloco 01 do `style.css`, sem alteração de hex |
| Hero: verde profundo + título branco/lima | Home e topo de todas as páginas internas |
| Botão primário: verde-limão com texto escuro | `.btn--primario` |
| Botão secundário: contorno claro ou verde | `.btn--contorno` / `.btn--whatsapp` |
| Cards simples, cantos discretamente arredondados | `--raio: 10px` (era 14px) |
| Alternar blocos claros e escuros | Ordem das seções em todas as páginas |
| Ícones de traço simples, monocromáticos | SVG inline, `stroke: currentColor` |
| Símbolo ampliado como textura de fundo | `--textura-losango`, nos blocos escuros |
| Recortes diagonais entre claro e escuro | `.com-diagonal` (Elementor: Shape Divider "Inclinado") |
| Fotografia P&B / baixa saturação + verde | `.foto-tratada`, pronta para a foto real entrar |
| Logotipo monocromático, caixa baixa | `.logo` — preto no header, branco no footer |

**Tipografia.** O guia pede "sans-serif geométrica e limpa" e não fixa família
oficial. Escolhi **Poppins** nos títulos — é a geométrica do Google Fonts mais
próxima do wordmark (os bojos circulares do "ágape") — e **Inter** no texto
corrido, pela leitura em bloco. As duas existem no Google Fonts, então o
Elementor as carrega nativamente. **É uma proposta: se a Ágape tiver a fonte
original do logotipo, ela substitui a Poppins.**

**Uma ressalva de contraste.** O verde institucional (`#46B148`) tem 2,7:1
sobre branco e o verde-limão (`#AFD745`) tem 1,7:1 — nenhum dos dois serve
como **texto** sobre fundo claro, reprovaria no WCAG AA. A solução não mexe na
marca: o verde-limão continua sendo a cor de ênfase, aplicada sobre fundo
escuro e nos botões (onde o texto por cima é escuro, 10,2:1); apenas
textos e links verdes sobre fundo claro usam `--cor-primaria` (`#2D762E`), um
escurecimento do verde institucional que mantém o matiz e alcança 5,6:1.

**Símbolo do logotipo.** O guia proíbe distorcer ou alterar a assinatura, e o
vetor não veio junto. Por isso o protótipo usa uma **aproximação geométrica**
do símbolo, claramente marcada no HTML, e a textura de fundo é uma malha de
losangos em CSS — não uma cópia do símbolo. **Pedir o SVG vetorial oficial**
(assinatura positiva e negativa) para a fase WordPress.

---

## 4. O que ainda é placeholder

Nada disso foi inventado — está tudo marcado no HTML entre colchetes ou em
caixas amarelas de "NOTA DE PROTÓTIPO".

**A prova social está completa — não há mais placeholder nela:**
- Números: **25 anos**, **+300 empresas**, **+600 CNPJs**, **~20 mil vidas**.
  Todos confirmados pelo cliente.
- **99 clientes** na carteira, com os logos reais, exibidos de três formas:
  carrossel infinito na Home (mostra a *quantidade*), mural agrupado por setor
  em `servicos/` (mostra a *variedade* — de posto de combustível a hospital) e
  recorte por afinidade em cada página de serviço.
- **Depoimentos foram removidos** do escopo, a pedido.
- E-mail comercial, complemento do endereço (Edifício Helbor Dual, salas
  1301/1302/1303) e domínio, no rodapé e no schema.
- Conteúdo real de Treinamentos (da NR-1 à NR-35, CIPA, Primeiros Socorros,
  Brigada/AVCB, SIPAT), de Medicina do Trabalho (palestras e campanhas) e de
  Ambulatório (empresas com SESMT próprio).

**Ainda a coletar com o cliente:**
- **Logotipo vetorial da Ágape** (assinatura positiva e negativa) — o guia
  proíbe alterar a assinatura, e o protótipo usa uma aproximação do símbolo.
- **Fotos das páginas internas** — cada placeholder traz, no comentário HTML
  ao lado, o texto ALT sugerido. Tratamento definido pelo guia: P&B ou baixa
  saturação com sobreposição verde (regra pronta em `.foto-tratada`).
- **Horário de atendimento** (página de Contato).
- **Missão, visão e valores** — o texto em `sobre-nos/` é uma proposta redigida
  a partir do posicionamento declarado. Validar ou substituir pelo oficial.
- **Política de Privacidade** — a estrutura cobre o que a LGPD exige, mas o
  texto precisa de revisão jurídica. Atenção especial: dados de saúde de exame
  ocupacional têm base legal distinta dos dados de formulário.
- **ALT do arquivo `85.png`** — marca em "A" com barras diagonais que não deu
  para nomear com certeza. Está no site com ALT genérico; confirmar o nome.

---

## 4.1. A imagem principal da Home

Não é foto nem imagem gerada por IA: é uma **composição vetorial autoral**
(`assets/img/hero-conformidade.svg`), desenhada na linguagem do guia —
verde-limão como ênfase, verde profundo no texto, malha de losangos ao fundo.

A escolha de mostrar a **documentação em dia** (PGR, PCMSO, treinamentos,
eSocial, cada um com seu check) em vez de uma foto genérica de trabalhador é
proposital: comunica o que a Ágape entrega, não uma cena de banco de imagens.
Sendo vetor, escala sem perder nitidez e pesa poucos KB.

Se o cliente preferir fotografia, a troca é direta: sai o `<img class="hero-arte">`
e entra a foto com a classe `.foto-tratada`, que já aplica o tratamento do guia.

**Textos dos serviços:** são placeholder realista de SST (PGR, PCMSO, eventos
do eSocial, NRs), escritos para o cliente ver o tom — **não são texto final**.
Precisam de revisão do responsável técnico. Onde havia risco de afirmar algo
específico demais (prazos legais exatos, periodicidades, lista de NRs), a frase
está marcada `[A CONFIRMAR]` em vez de chutada.

---

## 5. Decisões que precisam de resposta

1. **Perícias Médicas é o 7º serviço?** O portfólio apresenta Perícias Médicas
   como frente consolidada há mais de duas décadas — e o Facebook da empresa é
   literalmente `/agapepericias`. Mas ela **não está** entre os 6 serviços do
   escopo do site. Como criar página nova é decisão de arquitetura e de SEO,
   não a criei: por ora ela aparece em `sobre-nos/`, como parte da estrutura da
   empresa, com a pendência sinalizada na própria página. **Decidir:** página
   própria (slug novo), bloco dentro de Segurança do Trabalho, ou só a menção?
2. **Clínica Credenciada fala com quem?** O portfólio confirma o uso da rede
   credenciada para atender empresas em todo o Brasil — esse público já virou
   o principal da página. Falta decidir se ela **também** capta clínicas que
   queiram se credenciar. Se não, a página encolhe.
3. **Área do Cliente (SOC)** — o item de menu está pronto e **comentado** no
   HTML (`blocos.py`, função `cabecalho`). Se a Ágape for assinante do
   SOC/SOCRH, basta descomentar e apontar para o portal.
4. **Fonte dos títulos** — Poppins é proposta minha, não do guia. Se existir a
   fonte original do logotipo, ela manda.
5. **Menu com ou sem submenu de Serviços?** Optei por menu plano de 4 itens
   (Home · Sobre Nós · Serviços · Contato), com os 6 serviços no rodapé e na
   página de índice. Um submenu suspenso é viável no Elementor, se preferirem.
6. **Seção "Como funciona"** na Home (4 etapas) é um bloco a mais além dos 9
   previstos. Sai sem afetar nada, se for considerada redundante.
7. **Lista de praças atendidas** — a comunicação hoje diz só "todo o Brasil".
   Uma lista real de cidades é ganho direto de SEO local.

---

## 6. O que já está resolvido conforme o escopo

- **Formulário único, 5 campos, uma tela** — reutilizado em todo o site, com o
  campo "Serviço de interesse" **pré-marcado** pela página de origem. Confira:
  abra a página de Segurança do Trabalho e role até o formulário.
- **WhatsApp como via secundária** — presente em todas as páginas, nunca como
  única opção.
- **Contato com duas abas** — orçamento e candidatura com upload de currículo.
  "Faça parte" saiu do menu principal.
- **Prova social diluída** — bloco forte na Home, logos também nas páginas de
  serviço. A página isolada de clientes deixou de existir.
- **SEO** — H1 único por página, hierarquia de headings, title e meta
  description por página, breadcrumbs, ALT sugerido em cada imagem, schema
  LocalBusiness com os dados confirmados.
- **LGPD** — página própria + banner de consentimento.
- **Acessibilidade** — foco visível, link "pular para o conteúdo", contraste
  AA nos textos, navegação por teclado no menu e nas abas.

O formulário **não envia nada** (o botão é `type="button"`) e o protótipo não
usa `localStorage` nem qualquer armazenamento — o back-end vem no WordPress.
Todas as páginas estão com `noindex, nofollow`; remover ao publicar.
