# -*- coding: utf-8 -*-
"""
GERADOR DO PROTÓTIPO ESTÁTICO — Ágape Saúde e Segurança do Trabalho
====================================================================
Monta as páginas .html a partir dos blocos reutilizáveis (blocos.py) e
dos textos (conteudo.py). Assim header, footer, formulário e as 6 páginas
de serviço ficam rigorosamente iguais entre si.

Uso:   python build.py
Saída: index.html na raiz + uma pasta por slug, cada uma com index.html.
       Abre com duplo clique, sem servidor.

Quando o protótipo for aprovado, o que vai para o Elementor é o HTML/CSS
gerado — este script se aposenta.
"""

import os

from blocos import (
    u, ico, arte, documento, trilha, formulario,
    bloco_formulario, bloco_faq, bloco_carrossel_logos,
    bloco_setores_abas, bloco_fecho, bloco_numeros, bloco_servicos, bloco_diferenciais,
    bloco_cta_final, schema_local, CONTATO, PAGINAS, RAIZ,
)
from conteudo import (
    HOME, PROCESSO, FAQ_HOME, SERVICOS,
    SOBRE, SERVICOS_INDICE, CONTATO_PAGINA, PRIVACIDADE,
)
from clientes import CLIENTES

# ============================================================================
# HOME
# ============================================================================
def pagina_home():
    prof = 0
    d = HOME

    confianca = "\n".join(
        '        <li>%s<span>%s</span></li>' % (ico(i), t) for i, t in d["confianca"]
    )

    hero = """
<!-- BLOCO 2: HERO — headline + subtítulo + CTA primário + WhatsApp secundário -->
<section class="hero com-diagonal com-diagonal--para-alt">
  <div class="container hero-grade">
    <div>
      <span class="olho">Medicina e Segurança do Trabalho</span>
      <h1>%s<em>%s</em></h1>
      <p class="lead">%s</p>
      <div class="grupo-botoes">
        <a class="btn btn--primario" href="%s">Solicite um orçamento</a>
        <!-- WhatsApp é via SECUNDÁRIA (seção 5.1): existe, mas nunca sozinho. -->
        <a class="btn btn--whatsapp" href="%s" target="_blank" rel="noopener">%s Falar no WhatsApp</a>
      </div>
      <ul class="hero-confianca">
%s
      </ul>
    </div>
    <div class="hero-midia">%s
      <div class="hero-cartao-flutuante">
        <span class="numero">%s</span>
        <p>%s</p>
      </div>
    </div>
  </div>
</section>""" % (
        d["h1_antes"], d["h1_destaque"], d["lead"],
        u(prof, "contato", "#orcamento"),
        CONTATO["whats_comercial_href"], ico("whatsapp"),
        confianca,
        arte(prof, "hero",
             "Profissionais de uniforme e capacete em uma planta industrial "
             "atendida pela Ágape", classe="hero-arte"),
        d["hero_card"][0], d["hero_card"][1],
    )

    prova = """
<!-- BLOCO 4: PROVA SOCIAL — seção 5.3: vem logo abaixo do hero, com destaque.
     Números confirmados + a carteira real de clientes em carrossel. -->
<section class="secao secao--alt">
  <div class="container">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">Quem confia na Ágape</span>
      <h2>Um quarto de século resolvendo SST para empresas brasileiras</h2>
      <p class="lead">Desde 1999 traduzimos obrigação legal em rotina possível —
      com laudo que se sustenta e prazo que se cumpre.</p>
    </div>
%s
  </div>

  <div class="mt-2xl">
    <p class="faixa-logos-titulo">Algumas das %d empresas atendidas pela Ágape</p>
%s
  </div>

  <div class="container texto-centro mt-xl">
    <a class="link-seta" href="%s">Ver todos os serviços %s</a>
  </div>
</section>""" % (bloco_numeros(), len(CLIENTES),
                 bloco_carrossel_logos(prof), u(prof, "servicos"), ico("seta"))

    servicos = bloco_servicos(prof)

    diferenciais = """
<!-- BLOCO 5: DIFERENCIAIS — os 4 da seção 1 do CLAUDE.md.
     Duas colunas: arte à esquerda, os quatro diferenciais empilhados à
     direita. No Elementor: container de 2 colunas com Icon Box dentro. -->
<section class="secao secao--tinta">
  <div class="container duas-colunas duas-colunas--midia">
    <div class="midia-coluna">%s</div>
    <div>
      <span class="olho">Por que a Ágape</span>
      <h2>Descomplicamos a Saúde e Segurança do Trabalho</h2>
      <div class="lista-diferenciais mt-xl">
%s
      </div>
    </div>
  </div>
</section>""" % (
        arte(prof, "diferenciais",
             "Arte do bloco de diferenciais da Ágape, em losangos sobre verde profundo"),
        bloco_diferenciais(empilhado=True))

    passos = "\n".join(
        '      <div class="passo">\n'
        '        <span class="indice">ETAPA %02d</span>\n'
        '        <h3>%s</h3>\n        <p>%s</p>\n      </div>' % (i + 1, t, txt)
        for i, (t, txt) in enumerate(PROCESSO)
    )
    processo = """
<!-- BLOCO EXTRA "Como funciona" — não estava na lista de 9 blocos do
     CLAUDE.md. Grade simples, reproduzível no Elementor.
     Se o cliente achar redundante, esta seção sai sem afetar o resto. -->
<section class="secao">
  <div class="container">
    <div class="duas-colunas duas-colunas--midia mb-xl">
      <div>
        <span class="olho">Como funciona</span>
        <h2>Do primeiro contato à rotina que roda sozinha</h2>
        <p class="lead mt-md">Quatro etapas, sem surpresa no meio do caminho.
        Você sabe o que vem antes de assinar.</p>
      </div>
      <div class="midia-coluna">%s</div>
    </div>
    <div class="grade grade--4">
%s
    </div>
  </div>
</section>""" % (
        arte(prof, "processo",
             "Arte do bloco de processo da Ágape, em losangos sobre verde profundo"),
        passos)

    corpo = "\n".join([
        hero, prova, servicos, diferenciais, processo,
        bloco_faq(FAQ_HOME),
        bloco_fecho(prof),
    ])

    return documento(
        prof, "home", HOME["title"], HOME["meta"], corpo, atual="home",
        schema=schema_local(),
        nota_pagina="H1 único: a headline do hero. Demais seções usam H2.",
    )


# ============================================================================
# SOBRE NÓS
# ============================================================================
def pagina_sobre():
    prof = 1
    d = SOBRE

    paragrafos = "\n      ".join("<p>%s</p>" % p for p in d["historia"])

    topo = """
<section class="pagina-topo com-diagonal com-diagonal--para-branco">
  <div class="container">
%s
    <div class="pagina-topo-grade">
      <div>
        <h1>%s</h1>
        <p class="lead">%s</p>
      </div>
      <div>%s</div>
    </div>
  </div>
</section>""" % (
        trilha(prof, [("Sobre Nós", None)]), d["h1"], d["lead"],
        arte(prof, "institucional",
             "Arte institucional da Ágape, em losangos sobre verde profundo"),
    )

    historia = """
<section class="secao">
  <div class="container container--estreito">
    <div class="secao-cabecalho">
      <span class="olho">Nossa história</span>
      <h2>%s</h2>
    </div>
    <div>
      %s
    </div>
  </div>
</section>""" % (d["historia_titulo"], paragrafos)

    consultoria = """
<section class="secao secao--alt">
  <div class="container">
    <div class="secao-cabecalho">
      <span class="olho">Como atuamos</span>
      <h2>Consultoria e estrutura próprias</h2>
    </div>
    <div class="grade grade--2">
      <article class="card">
        <span class="icone-caixa">%s</span>
        <h3>%s</h3>
        <div class="mt-md">%s</div>
      </article>
      <article class="card">
        <span class="icone-caixa">%s</span>
        <h3>%s</h3>
        <div class="mt-md">%s</div>
      </article>
    </div>
    <p class="nota-prototipo mt-xl"><strong>NOTA DE PROTÓTIPO —</strong> %s</p>
  </div>
</section>""" % (
        ico("alvo"), d["consultoria_titulo"],
        "\n        ".join("<p>%s</p>" % p for p in d["consultoria"]),
        ico("documento"), d["pericias_titulo"],
        "\n        ".join("<p>%s</p>" % p for p in d["pericias"]),
        d["pericias_nota"],
    )

    esporte = """
<section class="secao secao--compacta">
  <div class="container duas-colunas">
    <div>
      <span class="olho">%s</span>
      <h2>Suzano Vôlei</h2>
      <p class="lead mt-md">%s</p>
    </div>
    <div>%s</div>
  </div>
</section>""" % (
        d["esporte_titulo"], d["esporte"],
        arte(prof, "esporte",
             "Partida de vôlei em quadra coberta — a Ágape apoia o Suzano Vôlei",
             classe="foto-tratada--larga"),
    )

    valores_itens = "\n".join(
        '      <div class="diferencial">\n'
        '        <span class="icone-caixa">%s</span>\n'
        '        <div>\n          <h3>%s</h3>\n          <p>%s</p>\n        </div>\n'
        '      </div>' % (ico(i), t, txt)
        for i, t, txt in d["valores"]
    )
    valores = """
<section class="secao secao--alt">
  <div class="container">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">O que nos guia</span>
      <h2>Nossos valores</h2>
    </div>
    <div class="grade grade--4">
%s
    </div>
    <p class="nota-prototipo mt-2xl"><strong>NOTA DE PROTÓTIPO —</strong> %s</p>
  </div>
</section>""" % (valores_itens, d["valores_nota"])

    equipe_itens = "\n".join(
        '        <li>%s<span>%s</span></li>' % (ico("check"), e) for e in d["equipe"]
    )
    equipe = """
<section class="secao">
  <div class="container duas-colunas">
    <div>%s</div>
    <div>
      <span class="olho">Time</span>
      <h2>%s</h2>
      <p class="lead mt-md">%s</p>
      <ul class="lista-check mt-xl">
%s
      </ul>
    </div>
  </div>
</section>""" % (
        arte(prof, "equipe",
             "Arte que representa a equipe multidisciplinar da Ágape"),
        d["equipe_titulo"], d["equipe_texto"], equipe_itens,
    )

    numeros = """
<section class="secao secao--escura">
  <div class="container">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">Em números</span>
      <h2>A operação da Ágape hoje</h2>
    </div>
%s
  </div>
</section>""" % bloco_numeros()

    corpo = "\n".join([
        topo, historia, consultoria, valores, equipe, numeros, esporte,
        bloco_servicos(prof, titulo="O que fazemos", olho="Serviços",
                       intro="As seis frentes que a Ágape opera para empresas."),
        bloco_cta_final(prof),
    ])

    return documento(prof, "sobre", d["title"], d["meta"], corpo, atual="sobre")


# ============================================================================
# SERVIÇOS (página índice)
# ============================================================================
def pagina_servicos():
    prof = 1
    d = SERVICOS_INDICE

    topo = """
<section class="pagina-topo com-diagonal com-diagonal--para-branco">
  <div class="container">
%s
    <div class="pagina-topo-grade">
      <div>
        <h1>%s</h1>
        <p class="lead">%s</p>
        <div class="grupo-botoes mt-xl">
          <a class="btn btn--primario" href="%s">Solicite um orçamento</a>
          <a class="btn btn--whatsapp" href="%s" target="_blank" rel="noopener">%s Falar no WhatsApp</a>
        </div>
      </div>
      <div>%s</div>
    </div>
  </div>
</section>""" % (
        trilha(prof, [("Serviços", None)]), d["h1"], d["lead"],
        u(prof, "contato", "#orcamento"),
        CONTATO["whats_comercial_href"], ico("whatsapp"),
        arte(prof, "servicos",
             "Arte que representa as seis frentes de serviço da Ágape"),
    )

    ajuda = """
<section class="secao secao--tinta">
  <div class="container container--estreito texto-centro">
    <span class="olho">Não sabe por onde começar?</span>
    <h2>A gente faz o diagnóstico antes de vender qualquer coisa</h2>
    <p class="lead mt-md">Levantamos o que a sua empresa já tem, o que está
    vencido e o que gera risco imediato de autuação. Só depois disso é que
    existe proposta.</p>
    <div class="grupo-botoes grupo-botoes--centro mt-xl">
      <a class="btn btn--primario" href="%s">Pedir um diagnóstico</a>
    </div>
  </div>
</section>""" % u(prof, "contato", "#orcamento")

    corpo = "\n".join([
        topo,
        bloco_servicos(prof, titulo="As seis frentes da Ágape",
                       olho="Serviços",
                       intro="Contrate uma, algumas ou todas — o interlocutor é o mesmo."),
        ajuda,
        """
<section class="secao">
  <div class="container">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">Carteira de clientes</span>
      <h2>De posto de combustível a hospital, de metalúrgica a colégio</h2>
      <p class="lead">A obrigação de SST é a mesma; o risco de cada operação
      não. Estas são as %d empresas que hoje confiam essa gestão à Ágape.</p>
    </div>
%s
  </div>
</section>""" % (len(CLIENTES), bloco_setores_abas(prof)),
        bloco_fecho(prof),
    ])

    return documento(prof, "servicos", d["title"], d["meta"], corpo, atual="servicos")


# ============================================================================
# PÁGINA DE SERVIÇO — modelo único, usado pelos 6 (seção 4 do CLAUDE.md)
# ============================================================================
def pagina_servico(s):
    prof = 1
    chave = s["chave"]

    nota = ""
    if s.get("nota_escopo"):
        nota = ('\n    <p class="nota-prototipo mt-xl"><strong>NOTA DE PROTÓTIPO —'
                '</strong> %s</p>' % s["nota_escopo"])

    topo = """
<section class="pagina-topo com-diagonal com-diagonal--para-branco">
  <div class="container">
%s
    <div class="pagina-topo-grade">
      <div>
        <span class="olho">Serviço</span>
        <h1>%s</h1>
        <p class="lead">%s</p>
        <div class="grupo-botoes mt-xl">
          <a class="btn btn--primario" href="#orcamento">Solicitar orçamento</a>
          <a class="btn btn--whatsapp" href="%s" target="_blank" rel="noopener">%s Falar no WhatsApp</a>
        </div>%s
      </div>
      <div>%s</div>
    </div>
  </div>
</section>""" % (
        trilha(prof, [("Serviços", "servicos"), (s["nome"], None)]),
        s["h1"], s["lead"],
        CONTATO["whats_comercial_href"], ico("whatsapp"), nota,
        arte(prof, chave, "Arte da frente de %s da Ágape" % s["nome"]),
    )

    paragrafos = "\n      ".join("<p>%s</p>" % p for p in s["intro_paragrafos"])
    bullets = "\n".join(
        '        <li>%s<span>%s</span></li>' % (ico("check"), b)
        for b in s["intro_bullets"]
    )
    intro = """
<section class="secao">
  <div class="container duas-colunas">
    <div>
      <span class="olho">O que fazemos</span>
      <h2>%s</h2>
      <div class="mt-lg">
      %s
      </div>
    </div>
    <div class="card">
      <h3>Em resumo</h3>
      <ul class="lista-check mt-lg">
%s
      </ul>
    </div>
  </div>
</section>""" % (s["intro_titulo"], paragrafos, bullets)

    cards = "\n".join(
        '      <article class="card">\n'
        '        <span class="icone-caixa">%s</span>\n'
        '        <h3>%s</h3>\n'
        '        <p class="mt-sm">%s</p>\n'
        '      </article>' % (ico("documento"), t, txt)
        for t, txt in s["entregaveis"]
    )
    entregaveis = """
<section class="secao secao--alt">
  <div class="container">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">Escopo</span>
      <h2>O que está incluído</h2>
      <p class="lead">Os itens abaixo são o padrão de entrega. O escopo final é
      dimensionado conforme o porte e o grau de risco da sua empresa.</p>
    </div>
    <div class="grade grade--3">
%s
    </div>
  </div>
</section>""" % cards

    porque_itens = "\n".join(
        '      <div class="diferencial">\n'
        '        <span class="icone-caixa">%s</span>\n'
        '        <div>\n          <h3>%s</h3>\n          <p>%s</p>\n        </div>\n'
        '      </div>' % (ico(i), t, txt)
        for i, (t, txt) in zip(["escudo", "relogio", "alvo"], s["porque"])
    )
    porque = """
<section class="secao">
  <div class="container">
    <div class="secao-cabecalho">
      <span class="olho">Diferenciais</span>
      <h2>Por que fazer isso com a Ágape</h2>
    </div>
    <div class="grade grade--3">
%s
    </div>
  </div>
</section>""" % porque_itens

    corpo = "\n".join([
        topo, intro, entregaveis, porque,
        bloco_faq(s["faq"], titulo="Perguntas frequentes sobre %s" % s["nome"]),
        # Formulário com o serviço PRÉ-MARCADO — roteamento por intenção.
        bloco_formulario(
            prof, servico_sel=chave,
            titulo_secao="Quer um orçamento de %s?" % s["nome"],
            texto_secao="O campo de serviço já vem preenchido. Conte o porte e o "
                        "ramo da sua empresa que devolvemos o escopo.",
        ),
        bloco_servicos(prof, titulo="Outros serviços da Ágape",
                       olho="Continue explorando",
                       intro="As demais frentes que podem ser contratadas junto.",
                       excluir=[chave], alt=True),
        bloco_cta_final(prof),
    ])

    nota_pg = ("Página de serviço — mesma estrutura de blocos nas 6. "
               "Formulário chega com o serviço pré-marcado.")
    return documento(prof, chave, s["title"], s["meta"], corpo,
                     atual="servicos", nota_pagina=nota_pg)


# ============================================================================
# CONTATO — duas abas (seção 5.2)
# ============================================================================
def form_candidatura(prof):
    """Aba 2: candidatura com upload de currículo."""
    areas = ["Medicina do trabalho", "Enfermagem do trabalho",
             "Engenharia de segurança", "Técnico de segurança do trabalho",
             "Administrativo e atendimento", "Comercial", "Outra área"]
    opcoes = "\n              ".join(
        '<option value="%s">%s</option>' % (a.lower().replace(" ", "-"), a)
        for a in areas
    )
    return """
<div class="form-cartao">
  <h3>Envie seu currículo</h3>
  <p class="form-sub">A Ágape mantém banco de talentos para as vagas que abrem
  ao longo do ano.</p>

  <form class="campos campos--2col" method="post" action="#" novalidate>
    <div class="campo">
      <label for="cv-nome">Nome completo <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="text" id="cv-nome" name="nome" placeholder="Seu nome" required>
    </div>
    <div class="campo">
      <label for="cv-email">E-mail <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="email" id="cv-email" name="email" placeholder="voce@email.com" required>
    </div>
    <div class="campo">
      <label for="cv-telefone">Telefone <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="tel" id="cv-telefone" name="telefone" placeholder="(00) 00000-0000" required>
    </div>
    <div class="campo">
      <label for="cv-cidade">Cidade / UF</label>
      <input type="text" id="cv-cidade" name="cidade" placeholder="Mogi das Cruzes / SP">
    </div>
    <div class="campo campo--largo">
      <label for="cv-area">Área de interesse</label>
      <select id="cv-area" name="area">
              <option value="">Selecione a área</option>
              %s
      </select>
    </div>
    <div class="campo campo--largo">
      <label for="cv-arquivo">Currículo <span class="obrigatorio" aria-hidden="true">*</span></label>
      <!-- UPLOAD DE CURRÍCULO (seção 5.2). No WordPress: campo de upload do
           Fluent Forms/WPForms, com limite de tamanho e tipos permitidos. -->
      <div class="campo-arquivo">
        %s
        <strong>Arraste seu currículo aqui ou selecione o arquivo</strong>
        <p class="campo-ajuda">PDF ou DOC, até 5 MB.</p>
        <input type="file" id="cv-arquivo" name="curriculo" accept=".pdf,.doc,.docx">
      </div>
    </div>
    <div class="campo campo--largo">
      <label for="cv-msg">Mensagem (opcional)</label>
      <textarea id="cv-msg" name="mensagem" placeholder="Conte brevemente sua experiência em SST."></textarea>
    </div>
    <div class="campo campo--largo">
      <label class="consentimento" for="cv-lgpd">
        <input type="checkbox" id="cv-lgpd" name="lgpd" required>
        <span>Autorizo a Ágape a armazenar meus dados e meu currículo para
        processos seletivos, conforme a <a href="%s">Política de Privacidade</a>.</span>
      </label>
    </div>
    <div class="campo campo--largo form-rodape">
      <button type="button" class="btn btn--primario btn--bloco">Enviar currículo</button>
      <p class="form-nota">Protótipo: o envio está desativado. No WordPress,
      o arquivo é recebido e o RH notificado por e-mail.</p>
    </div>
  </form>
</div>""" % (opcoes, ico("upload"), u(prof, "privacidade"))


def pagina_contato():
    prof = 1
    d = CONTATO_PAGINA

    topo = """
<section class="pagina-topo com-diagonal com-diagonal--para-branco">
  <div class="container">
%s
    <h1>%s</h1>
    <p class="lead">%s</p>
  </div>
</section>""" % (trilha(prof, [("Contato", None)]), d["h1"], d["lead"])

    info_orcamento = """
    <div>
      <span class="olho">Orçamento</span>
      <h2>Um formulário, cinco campos, uma tela</h2>
      <p class="lead mt-md">Nada de multi-step nem de canhão para o WhatsApp:
      preencha os cinco campos e o time comercial recebe o pedido completo.</p>
      <ul class="lista-check mt-xl">
        <li>%s<span>Retorno do time comercial da Ágape</span></li>
        <li>%s<span>Escopo por serviço, sem pacote fechado</span></li>
        <li>%s<span>Diagnóstico inicial sem compromisso</span></li>
      </ul>
      <p class="mt-xl"><strong>Prefere WhatsApp?</strong><br>
      Comercial: <a href="%s" target="_blank" rel="noopener">%s</a></p>
    </div>""" % (ico("check"), ico("check"), ico("check"),
                 CONTATO["whats_comercial_href"], CONTATO["whats_comercial"])

    info_trabalhe = """
    <div>
      <span class="olho">Trabalhe conosco</span>
      <h2>Quero trabalhar com vocês</h2>
      <p class="lead mt-md">Esta aba substitui a antiga página "Faça parte", que
      saiu do menu principal e passou a viver dentro de Contato.</p>
      <ul class="lista-check mt-xl">
        <li>%s<span>Equipe multidisciplinar de saúde e segurança</span></li>
        <li>%s<span>Matriz em Mogi das Cruzes, com atuação nacional</span></li>
        <li>%s<span>Currículos ficam no banco de talentos da Ágape</span></li>
      </ul>
    </div>""" % (ico("check"), ico("check"), ico("check"))

    abas = """
<!-- CONTATO COM DUAS ABAS (seção 5.2). Abas em CSS puro, via radio.
     No Elementor: widget Tabs nativo — inclusive com link direto para a
     segunda aba, que o protótipo estático não consegue fazer sem JS. -->
<section class="secao">
  <div class="container">
    <div class="abas">
      <input class="aba-radio" type="radio" name="aba-contato" id="aba-orcamento" checked>
      <input class="aba-radio" type="radio" name="aba-contato" id="aba-trabalhe">

      <div class="aba-lista">
        <label for="aba-orcamento">Quero um orçamento</label>
        <label for="aba-trabalhe">Quero trabalhar com vocês</label>
      </div>

      <div class="aba-conteudo">
        <div class="aba-painel" id="painel-orcamento">
          <div class="form-bloco-grade">
%s
%s
          </div>
        </div>

        <div class="aba-painel" id="painel-trabalhe">
          <div class="form-bloco-grade">
%s
%s
          </div>
        </div>
      </div>
    </div>
  </div>
</section>""" % (info_orcamento, formulario(prof), info_trabalhe,
                 form_candidatura(prof))

    dados = """
<section class="secao secao--alt">
  <div class="container">
    <div class="secao-cabecalho">
      <span class="olho">Onde estamos</span>
      <h2>Matriz em Mogi das Cruzes, atendimento em todo o Brasil</h2>
    </div>
    <div class="grade grade--2">
      <div class="grade">
        <div class="contato-item">
          <span class="icone-caixa">%s</span>
          <div>
            <h3>Endereço</h3>
            <p>%s – %s<br>%s – %s, %s</p>
          </div>
        </div>
        <div class="contato-item">
          <span class="icone-caixa">%s</span>
          <div>
            <h3>Recepção matriz</h3>
            <p><a href="%s">%s</a> · WhatsApp
            <a href="%s" target="_blank" rel="noopener">%s</a></p>
          </div>
        </div>
        <div class="contato-item">
          <span class="icone-caixa">%s</span>
          <div>
            <h3>Comercial e marketing</h3>
            <p>WhatsApp <a href="%s" target="_blank" rel="noopener">%s</a></p>
          </div>
        </div>
        <div class="contato-item">
          <span class="icone-caixa">%s</span>
          <div>
            <h3>Horário de atendimento</h3>
            <p>[HORÁRIO A CONFIRMAR com o cliente — ex.: seg. a sex., 7h às 17h]</p>
          </div>
        </div>
      </div>
      <div>
        <!-- MAPA: no WordPress, incorporar o Google Maps da matriz.
             Aqui fica o placeholder para não depender de script externo. -->
        %s
      </div>
    </div>
  </div>
</section>""" % (
        ico("mapa"), CONTATO["rua"], CONTATO["bairro"],
        CONTATO["cidade"], CONTATO["uf"], CONTATO["cep"],
        ico("telefone"), CONTATO["fixo_href"], CONTATO["fixo"],
        CONTATO["whats_recepcao_href"], CONTATO["whats_recepcao"],
        ico("whatsapp"), CONTATO["whats_comercial_href"], CONTATO["whats_comercial"],
        ico("relogio"),
        arte(prof, "mapa",
             "Arte no lugar do mapa da matriz — no WordPress, incorporar o "
             "Google Maps do endereço", classe="foto-tratada--mapa"),
    )

    corpo = "\n".join([topo, abas, dados, bloco_cta_final(prof)])

    return documento(prof, "contato", d["title"], d["meta"], corpo,
                     atual="contato", schema=schema_local())


# ============================================================================
# POLÍTICA DE PRIVACIDADE (LGPD) — página nova, substitui o PDF solto
# ============================================================================
def pagina_privacidade():
    prof = 1
    d = PRIVACIDADE

    secoes = []
    for titulo, itens in d["secoes"]:
        corpo_secao = "\n".join("      <p>%s</p>" % i for i in itens) \
            if len(itens) == 1 else \
            "      <ul>\n%s\n      </ul>" % "\n".join(
                "        <li>%s</li>" % i for i in itens)
        secoes.append("    <h2>%s</h2>\n%s" % (titulo, corpo_secao))

    topo = """
<section class="pagina-topo com-diagonal com-diagonal--para-branco">
  <div class="container">
%s
    <h1>%s</h1>
    <p class="lead">%s</p>
  </div>
</section>""" % (trilha(prof, [("Política de Privacidade", None)]), d["h1"], d["lead"])

    conteudo = """
<section class="secao">
  <div class="container container--estreito texto-legal">
    <p class="nota-prototipo mb-xl"><strong>NOTA DE PROTÓTIPO —</strong> %s</p>
%s
    <h2>Fale com a gente sobre seus dados</h2>
    <p>%s – %s, %s – %s, %s.<br>
    Telefone: <a href="%s">%s</a></p>
  </div>
</section>""" % (
        d["aviso"], "\n\n".join(secoes),
        CONTATO["rua"], CONTATO["bairro"], CONTATO["cidade"],
        CONTATO["uf"], CONTATO["cep"], CONTATO["fixo_href"], CONTATO["fixo"],
    )

    corpo = "\n".join([topo, conteudo, bloco_cta_final(prof)])
    return documento(prof, "privacidade", d["title"], d["meta"], corpo, atual="")


# ============================================================================
# ESCRITA DOS ARQUIVOS
# ============================================================================
def escrever(chave, html):
    destino = os.path.join(RAIZ, PAGINAS[chave].replace("/", os.sep), "index.html")
    pasta = os.path.dirname(destino)
    if pasta and not os.path.isdir(pasta):
        os.makedirs(pasta)
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return os.path.relpath(destino, RAIZ)


def gerar():
    saidas = []
    saidas.append(escrever("home", pagina_home()))
    saidas.append(escrever("sobre", pagina_sobre()))
    saidas.append(escrever("servicos", pagina_servicos()))
    for s in SERVICOS:
        saidas.append(escrever(s["chave"], pagina_servico(s)))
    saidas.append(escrever("contato", pagina_contato()))
    saidas.append(escrever("privacidade", pagina_privacidade()))

    print("Protótipo gerado:")
    for caminho in saidas:
        tamanho = os.path.getsize(os.path.join(RAIZ, caminho)) / 1024
        print("  %-52s %6.1f KB" % (caminho, tamanho))
    print("\n%d páginas. Abra index.html com duplo clique." % len(saidas))


if __name__ == "__main__":
    gerar()
