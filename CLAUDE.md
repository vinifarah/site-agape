# CLAUDE.md — Projeto Ágape Saúde e Segurança

> Arquivo de contexto persistente para o Claude Code.
> Lido automaticamente no início de cada sessão nesta pasta.

---

## 0. O QUE É ESTA FASE (leia antes de gerar qualquer coisa)

Estamos construindo um **protótipo estático em HTML/CSS puro** do novo site da Ágape.

- **NÃO** gere PHP, não gere código WordPress, não assuma banco de dados, não use frameworks JS pesados.
- O objetivo é um site navegável que abre com duplo-clique no navegador, para aprovação visual do responsável pelo projeto e do cliente.
- Este protótipo é a **especificação visual** que depois será reconstruída no WordPress com o page builder Elementor.

### Regra de ouro do projeto
**Tudo que for desenhado aqui precisa ser reconstruível no WordPress/Elementor.** Antes de propor qualquer elemento visual, considere se ele é viável num page builder de blocos. Evite:
- Layouts que dependam de JS complexo para existir (animações decorativas leves são ok; funcionalidade que só existe via script, não).
- Grids muito exóticos que um builder não reproduz sem dor.
- Tipografia/efeitos que dependam de bibliotecas que não teriam equivalente em plugin.
Prefira: seções empilhadas, grids simples (flex/grid de 2-4 colunas), cards, blocos repetíveis. Pense em cada seção como um "container do Elementor".

---

## 1. O CLIENTE

- **Nome:** Ágape Saúde e Segurança do Trabalho
- **Setor:** Saúde e Segurança do Trabalho (SST) / Medicina Ocupacional — B2B
- **Fundação:** 1999, em Mogi das Cruzes-SP. Mais de 25 anos de atuação.
- **Alcance:** atende todo o Brasil.
- **Posicionamento:** parceiro confiável, atendimento humanizado, laudos com validade jurídica, cumprimento de prazos e normas.
- **Público-alvo:** empresas de todos os segmentos que precisam cumprir obrigações de SST (RH, gestores, SESMT).
- **Tom da marca:** confiança, conformidade, seriedade técnica, sem ser frio. Institucional, mas humano.

### Slogan/headline atual
"Saúde e Segurança do Trabalho com excelência"

### Descrição-âncora (do site atual)
"Atuamos em todo o Brasil há mais de 25 anos com soluções completas em Medicina Ocupacional, Segurança do Trabalho, Treinamentos, eSocial. Garantimos laudos técnicos com validade jurídica, cumprimento de prazos e atendimento humanizado."

### Diferenciais declarados
- 25 anos de experiência
- Equipe multidisciplinar
- "Descomplicamos a Saúde e Segurança do Trabalho"
- Cumprimento de prazos e normas

---

## 2. DADOS DE CONTATO REAIS (usar no rodapé e página de contato)

- **Endereço (matriz):** Av. Pref. Carlos Ferreira Lopes, 703 – Vila Mogilar, Mogi das Cruzes – SP, 08773-490
- **Recepção Matriz — Fixo:** (11) 4726-3150
- **Recepção Matriz — WhatsApp:** (11) 94791-9138
- **Comercial / Marketing — WhatsApp:** (11) 93406-7014
- **Redes sociais:**
  - Facebook: https://www.facebook.com/agapepericias
  - Instagram: https://www.instagram.com/agape.sst/
  - LinkedIn: https://www.linkedin.com/company/ágape-saúde-e-segurança-do-trabalho/
- **LGPD:** hoje é um PDF solto. NO NOVO SITE vira página própria + banner de consentimento.

---

## 3. ARQUITETURA DE PÁGINAS

Manter os **slugs atuais** sempre que a página já existir (o cliente tem SEO neles — não inventar URLs novas para páginas existentes):

| Página | Slug atual | Observação |
|---|---|---|
| Home | `/` | Refeita do zero visualmente |
| Sobre Nós | `/sobre-nos/` | |
| Serviços (índice) | `/servicos/` | Página que lista os 6 serviços |
| Medicina Ocupacional | `/medicina-ocupacional-empresas/` | |
| Segurança do Trabalho | `/seguranca-trabalho-empresas/` | |
| eSocial SST | `/esocial-sst-empresas/` | |
| Treinamentos NR's | `/treinamentos-nrs-empresas/` | |
| Gestão de Ambulatório | `/gestao-ambulatorio-empresas/` | |
| Clínica Credenciada | `/clinica-credenciada/` | |
| Contato | `/contato/` | Passa a ter DUAS abas (ver seção 5) |

### Mudanças de estrutura em relação ao site atual
- **"Faça parte"** sai do menu principal → vira aba dentro de Contato ("Quero trabalhar com vocês").
- **"Nossos Parceiros / Nossos Clientes"** deixa de ser página isolada → a prova social é **diluída**: bloco forte na Home + logos distribuídos nas páginas de serviço.
- **"Solicite um orçamento"** deixa de ser canhão para WhatsApp → vira formulário estruturado (ver seção 5).

---

## 4. OS 6 SERVIÇOS (núcleo do negócio)

Cada um vira uma página de serviço, todas com a MESMA estrutura de blocos (mudando só o conteúdo):

1. **Medicina Ocupacional** — exames ocupacionais (admissional, periódico, demissional), ASO, PCMSO.
2. **Segurança do Trabalho** — PGR, GRO, laudos técnicos, gestão de riscos.
3. **eSocial SST** — envio dos eventos de SST ao eSocial (S-2210, S-2220, S-2240).
4. **Treinamentos NR's** — treinamentos normativos (NRs).
5. **Gestão de Ambulatório** — terceirização e gestão de ambulatório dentro da empresa cliente.
6. **Clínica Credenciada** — credenciamento de rede.

> Os textos descritivos de cada serviço ainda serão redigidos. No protótipo, usar placeholder realista e coerente com SST (não "lorem ipsum" genérico), para o cliente visualizar o tom.

---

## 5. FUNCIONALIDADES (todas construíveis em WordPress/Elementor + plugin de formulário)

### 5.1 Formulário de orçamento — substitui o "canhão de WhatsApp"
- **UM único formulário**, reutilizado em todo o site.
- Campo "Serviço de interesse" **pré-marcado** conforme o card/página de origem (roteamento por intenção).
- **5 campos, uma única tela** (sem multi-step, mobile-friendly): Nome · Empresa · Telefone · E-mail · Serviço de interesse.
- No protótipo: HTML do formulário funcional visualmente (sem back-end real). No WordPress: Fluent Forms ou WPForms, gravando o lead no banco + notificação por e-mail.
- **WhatsApp continua existindo, como opção SECUNDÁRIA**, nunca como única via.

### 5.2 Contato com duas abas
- Aba "Quero um orçamento" → formulário 5.1.
- Aba "Quero trabalhar com vocês" → formulário de candidatura com **upload de currículo**.

### 5.3 Prova social (na Home, com destaque)
- Bloco logo abaixo do hero: depoimentos reais (nome + cargo + empresa) + números de operação (25 anos, nº de empresas atendidas, nº de exames — **dados reais a coletar com o cliente**).
- Logos de clientes: distribuídos pela Home e páginas de serviço (não mais numa página isolada).
- ⚠️ Depoimentos e números NÃO devem ser inventados no protótipo — usar placeholders claramente marcados como "[DEPOIMENTO A COLETAR]".

### 5.4 SEO e presença no Google (embutir desde o protótipo)
- Estrutura semântica correta (h1 único por página, hierarquia de headings, alt em todas as imagens).
- Preservar slugs (seção 3).
- Preparar campos de title/meta description por página (no protótipo, como comentário ou meta tag placeholder).
- Marca o terreno para: schema LocalBusiness, sitemap, blog futuro (blog = adicional fora do escopo base).

### 5.5 Área do Cliente (SOC) — CONDICIONAL, provavelmente só um link
- SE a Ágape já for assinante do sistema SOC/SOCRH (a confirmar com o cliente), adicionar item "Área do Cliente" no menu apontando para o portal externo do SOC. É só um link, não uma funcionalidade construída.
- SE não for, não incluir. Deixar como visão de futuro.
- No protótipo: incluir o item de menu como placeholder desativado/comentado.

---

## 6. IDENTIDADE VISUAL

### Cores (ponto de partida — confirmar hex exato no ambiente real)
O site atual é fortemente baseado em **verde institucional** (saúde), com botões e cabeçalho verdes.
- Definir como variáveis CSS (`--cor-primaria`, `--cor-secundaria`, etc.) para ajuste fácil.
- Verde primário aproximado observado: `#1D9E75` / tons de verde-saúde. **Validar com material de marca do cliente.**
- Sugestão de sistema (a refinar no protótipo): um verde primário para ações, um verde/escuro secundário para texto e áreas de destaque, neutros claros para fundo, um acento para CTAs se necessário.

> IMPORTANTE: no protótipo, TODA cor deve ser variável CSS no topo do arquivo. No WordPress isso vira os "Estilos Globais" do Elementor — a correspondência tem que ser 1:1 para o cliente conseguir editar tudo por lá depois.

### Logo
- Existe logo atual (arquivo "Logo-Clientes-2.png" e versão "siteagape-removebg-preview.png"). Pedir versão vetorial ao cliente. No protótipo, usar placeholder de logo.

### Tipografia
- A definir. Escolher fontes disponíveis no Google Fonts (o Elementor integra Google Fonts nativamente — não usar fonte que não exista lá, senão não é reproduzível no WordPress).

---

## 7. BLOCOS REUTILIZÁVEIS (pensar o site como composição destes)

Cada bloco = um "container" que depois vira template no Elementor. Construir cada um UMA vez, reaproveitar:

1. **Header** (logo + menu + botão "Solicite um orçamento") — global.
2. **Hero** — headline + subtítulo + CTA primário + CTA WhatsApp secundário.
3. **Grade de serviços** — cards (nome do serviço + ícone + botão que leva à página/formulário).
4. **Prova social** — depoimentos + números + logos.
5. **Bloco de diferenciais** — ícone + texto, em linha (os 4 diferenciais da seção 1).
6. **FAQ** — accordion (perguntas frequentes por serviço).
7. **Formulário** — o de orçamento (seção 5.1).
8. **CTA final** — faixa de chamada antes do rodapé.
9. **Footer** — contatos reais (seção 2) + redes + LGPD + mapa do site.

---

## 8. O QUE NÃO FAZER

- Não usar Bootstrap/Tailwind/React no protótipo — HTML/CSS puro (o CSS será portado para o Elementor manualmente; quanto mais limpo, melhor).
- Não inventar dados (depoimentos, números, nomes de clientes). Marcar placeholders.
- Não criar URLs diferentes das da seção 3 para páginas existentes.
- Não desenhar nada que dependa de funcionalidade impossível num page builder.
- Não usar armazenamento de browser (localStorage etc.) — protótipo é estático.
- Não tratar o formulário como funcional de verdade (é visual; o back-end vem no WordPress).

---

## 9. ESTADO DO PROJETO / PRÓXIMOS PASSOS

- [x] Escopo funcional definido
- [x] Análise de concorrentes (BMPC, Salú, Famma, Grupo Mast) feita
- [x] Protótipo HTML/CSS — 11 páginas geradas (ver `README.md`)
- [ ] **← VOCÊ ESTÁ AQUI:** aprovação do protótipo (responsável + cliente)
- [ ] Ambiente WordPress local (Local by WP Engine)
- [ ] Construção no Elementor + child theme
- [ ] Formulário, SEO técnico, LGPD
- [ ] Staging no HostGator → produção

### Ordem sugerida de construção do protótipo
1. Definir o sistema de design (variáveis CSS: cores, tipografia, espaçamento) num arquivo único.
2. Header + Footer (aparecem em todas as páginas).
3. Home completa (é onde vivem quase todos os blocos).
4. UMA página de serviço modelo (as outras 5 herdam a estrutura).
5. Contato com as duas abas.
6. Sobre Nós.