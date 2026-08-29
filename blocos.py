# -*- coding: utf-8 -*-
"""
BLOCOS REUTILIZÁVEIS — Ágape Saúde e Segurança do Trabalho
===========================================================
Os 9 blocos da seção 7 do CLAUDE.md, cada um construído UMA vez:
header, hero, grade de serviços, prova social, diferenciais, FAQ,
formulário, CTA final e footer. Mais os dados de contato reais e o
mapa de slugs.

Este módulo não gera nada sozinho — quem monta as páginas é build.py.
Execute:  python build.py
"""

import os
import re
from datetime import date

from conteudo import NUMEROS_HOME, DIFERENCIAIS, SERVICOS
from clientes import CLIENTES, SETORES

RAIZ = os.path.dirname(os.path.abspath(__file__))
ANO = date.today().year

# ============================================================================
# DADOS REAIS DO CLIENTE (seção 2 do CLAUDE.md)
# ============================================================================
EMPRESA = "Ágape Saúde e Segurança do Trabalho"

CONTATO = {
    "rua": "Av. Pref. Carlos Ferreira Lopes, 703",
    # Complemento veio do PORTFÓLIO ÁGAPE (não estava no briefing inicial)
    "complemento": "Edifício Helbor Dual — Salas 1301, 1302 e 1303",
    "bairro": "Vila Mogilar",
    "cidade": "Mogi das Cruzes",
    "uf": "SP",
    "cep": "08773-490",
    # E-mail e site também vieram do portfólio
    "email": "mktecomercial@agapesaudeseguranca.com.br",
    "site": "www.agapesaudeseguranca.com.br",
    "fixo": "(11) 4726-3150",
    "fixo_href": "tel:+551147263150",
    "whats_recepcao": "(11) 94791-9138",
    "whats_recepcao_href": "https://wa.me/5511947919138",
    "whats_comercial": "(11) 93406-7014",
    "whats_comercial_href": "https://wa.me/5511934067014",
    "facebook": "https://www.facebook.com/agapepericias",
    "instagram": "https://www.instagram.com/agape.sst/",
    "linkedin": "https://www.linkedin.com/company/"
                "%C3%A1gape-sa%C3%BAde-e-seguran%C3%A7a-do-trabalho/",
}

# ============================================================================
# MAPA DE PÁGINAS — slugs do site atual (seção 3). NÃO renomear: há SEO neles.
# ============================================================================
PAGINAS = {
    "home":         "",
    "sobre":        "sobre-nos/",
    "servicos":     "servicos/",
    "medicina":     "medicina-ocupacional-empresas/",
    "seguranca":    "seguranca-trabalho-empresas/",
    "esocial":      "esocial-sst-empresas/",
    "treinamentos": "treinamentos-nrs-empresas/",
    "ambulatorio":  "gestao-ambulatorio-empresas/",
    "clinica":      "clinica-credenciada/",
    "contato":      "contato/",
    "privacidade":  "politica-de-privacidade/",
}

ROTULOS = {
    "home": "Home",
    "sobre": "Sobre Nós",
    "servicos": "Serviços",
    "contato": "Contato",
    "privacidade": "Política de Privacidade",
}
for _s in SERVICOS:
    ROTULOS[_s["chave"]] = _s["nome"]


def u(prof, chave, ancora=""):
    """URL relativa — o protótipo precisa funcionar via file:// (duplo clique)."""
    return ("../" * prof) + PAGINAS[chave] + "index.html" + ancora


def css(prof):
    return ("../" * prof) + "assets/css/style.css"


def marca(atual, chave):
    return ' aria-current="page"' if atual == chave else ""


# ============================================================================
# ÍCONES — SVG inline, sem biblioteca externa.
# No Elementor: biblioteca de ícones nativa ou upload de SVG.
# ============================================================================
def _svg(corpo, cheio=False):
    if cheio:
        return ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                + corpo + "</svg>")
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">' + corpo + "</svg>")


ICONES = {
    "check": _svg('<path d="M20 6L9 17l-5-5"/>'),
    "seta": _svg('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "telefone": _svg(
        '<path d="M21.5 16.9v2.7a2 2 0 0 1-2.2 2 19.6 19.6 0 0 1-8.5-3 19.3 19.3 '
        '0 0 1-6-6 19.6 19.6 0 0 1-3-8.6A2 2 0 0 1 3.8 2h2.7a2 2 0 0 1 2 1.7c.12 '
        '1 .35 1.9.67 2.8a2 2 0 0 1-.45 2.1L7.6 9.7a16 16 0 0 0 6 6l1.1-1.1a2 2 0 '
        '0 1 2.1-.45c.9.32 1.84.55 2.8.67a2 2 0 0 1 1.9 2.05z"/>'),
    "whatsapp": _svg(
        '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22.5l5.6-1.4A10 10 0 1 0 12 2zm0 '
        '18.1a8 8 0 0 1-4.3-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.1 8.1 0 1 1 12 20.1z"/>'
        '<path d="M17 14.3c-.3-.15-1.7-.85-2-.95-.26-.1-.45-.15-.64.15s-.74.94-.9 '
        '1.13c-.17.2-.34.22-.63.07a8.1 8.1 0 0 1-2.4-1.5 9 9 0 0 1-1.66-2.06c-.17-'
        '.3 0-.46.13-.6.14-.14.3-.35.45-.53.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-'
        '.08-.15-.64-1.55-.88-2.12-.23-.55-.47-.48-.64-.49h-.55c-.2 0-.5.07-.77.37-'
        '.26.3-1 .98-1 2.4s1.03 2.78 1.17 2.98c.15.2 2.03 3.1 4.9 4.35.69.3 1.22.47 '
        '1.64.6.69.22 1.32.19 1.81.11.55-.08 1.7-.7 1.94-1.36.24-.67.24-1.24.17-'
        '1.36-.07-.12-.26-.2-.55-.34z"/>', cheio=True),
    "mapa": _svg('<path d="M20 10.5c0 5.8-8 11.5-8 11.5s-8-5.7-8-11.5a8 8 0 1 1 '
                 '16 0z"/><circle cx="12" cy="10.2" r="3"/>'),
    "email": _svg('<rect x="2.5" y="4.5" width="19" height="15" rx="2.4"/>'
                  '<path d="M3.2 6.6l8.8 5.9 8.8-5.9"/>'),
    "relogio": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7.2V12l3.2 1.9"/>'),
    "escudo": _svg('<path d="M12 2.5l7.6 3v5.9c0 4.9-3.2 8.6-7.6 10.1-4.4-1.5-7.6-'
                   '5.2-7.6-10.1V5.5z"/><path d="M9 12l2.1 2.1L15.4 9.9"/>'),
    "usuarios": _svg('<path d="M15.8 20.5v-1.7a4 4 0 0 0-4-4H6.2a4 4 0 0 0-4 4v1.7"/>'
                     '<circle cx="9" cy="7.2" r="3.6"/><path d="M21.8 20.5v-1.7a4 4 '
                     '0 0 0-3-3.87"/><path d="M16.2 3.8a4 4 0 0 1 0 6.9"/>'),
    "calendario": _svg('<rect x="3" y="5" width="18" height="16" rx="2.4"/>'
                       '<path d="M8 3v4M16 3v4M3 10.2h18"/>'),
    "documento": _svg('<path d="M14 3H7.4A2.4 2.4 0 0 0 5 5.4v13.2A2.4 2.4 0 0 0 '
                      '7.4 21h9.2a2.4 2.4 0 0 0 2.4-2.4V8z"/><path d="M14 3v5h5"/>'
                      '<path d="M9.4 14.4l1.8 1.8 3.4-3.4"/>'),
    "estetoscopio": _svg('<path d="M6 3v5.6a4 4 0 0 0 8 0V3"/><path d="M4.2 3H6M12.2 '
                         '3H14"/><path d="M10 12.6v2.1a5 5 0 0 0 10 0v-1.4"/>'
                         '<circle cx="20" cy="10.6" r="2.1"/>'),
    "capacete": _svg('<path d="M3.6 18v-2.1a8.4 8.4 0 0 1 16.8 0V18"/>'
                     '<rect x="2" y="18" width="20" height="3.1" rx="1.5"/>'
                     '<path d="M9 5V9.6M15 5V9.6"/><path d="M9 5a3 3 0 0 1 6 0"/>'),
    "sistema": _svg('<rect x="2.5" y="4" width="19" height="13" rx="2.2"/>'
                    '<path d="M8.4 21h7.2M12 17.2V21"/>'
                    '<path d="M8.8 10.6l2.1 2.1 4.3-4.3"/>'),
    "formacao": _svg('<path d="M12 3.2L2.6 8 12 12.8 21.4 8z"/><path d="M6.2 10.2v4.4'
                     'c0 1.7 2.6 3 5.8 3s5.8-1.3 5.8-3v-4.4"/><path d="M21.4 8v5.6"/>'),
    "predio": _svg('<rect x="4" y="3" width="16" height="18" rx="2.2"/>'
                   '<path d="M12 8.4v5.2M9.4 11h5.2"/><path d="M4 21h16"/>'),
    "rede": _svg('<circle cx="12" cy="4.6" r="2.2"/><circle cx="5" cy="19.2" r="2.2"/>'
                 '<circle cx="19" cy="19.2" r="2.2"/><circle cx="12" cy="12" r="1.9"/>'
                 '<path d="M12 6.8v3.3M10.6 13.4L6.4 17.4M13.4 13.4l4.2 4"/>'),
    "alvo": _svg('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/>'
                 '<circle cx="12" cy="12" r="1.4"/>'),
    "coracao": _svg('<path d="M12 20.4s-7.4-4.6-7.4-9.7A3.9 3.9 0 0 1 12 8.1a3.9 3.9 '
                    '0 0 1 7.4 2.6c0 5.1-7.4 9.7-7.4 9.7z"/>'),
    "globo": _svg('<circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/>'
                  '<path d="M12 3a14.5 14.5 0 0 1 0 18 14.5 14.5 0 0 1 0-18z"/>'),
    "aspas": _svg('<path d="M9.6 6.2C6.4 7.8 4.8 10.3 4.8 13.5v4.3h5.8v-5.9H8.1c.1-'
                  '1.9.9-3.2 2.6-4.1zM19.2 6.2c-3.2 1.6-4.8 4.1-4.8 7.3v4.3h5.8v-5.9'
                  'h-2.5c.1-1.9.9-3.2 2.6-4.1z"/>', cheio=True),
    "imagem": _svg('<rect x="3" y="4.2" width="18" height="15.6" rx="2.4"/>'
                   '<circle cx="8.6" cy="9.6" r="1.8"/>'
                   '<path d="M20.4 15.6l-4.8-4.8-8.4 8.4"/>'),
    "upload": _svg('<path d="M12 15.6V3.6"/><path d="M8 7.6l4-4 4 4"/>'
                   '<path d="M4 15.6v2.8A2 2 0 0 0 6 20.4h12a2 2 0 0 0 2-2v-2.8"/>'),
    "menu": _svg('<path d="M4 7h16M4 12h16M4 17h16"/>'),
    # APROXIMAÇÃO do símbolo da marca (losangos entrelaçados), para o
    # protótipo. Trocar pelo SVG oficial quando o cliente enviar o vetor.
    "losango": _svg('<path d="M12 1.8L22.2 12 12 22.2 1.8 12z"/>'
                    '<path d="M12 1.8L17.1 6.9 12 12 6.9 6.9z"/>'
                    '<path d="M12 12l5.1 5.1L12 22.2 6.9 17.1z"/>'
                    '<path d="M8.4 12L12 8.4l3.6 3.6L12 15.6z"/>'),
    "raio": _svg('<path d="M13.2 2.5L4.5 13.4h6.3l-1 8.1 8.7-10.9h-6.3z"/>'),
    "facebook": _svg('<path d="M13.4 22v-8.1h2.7l.42-3.15H13.4V8.73c0-.9.25-1.53 '
                     '1.56-1.53h1.67V4.38A22 22 0 0 0 14.2 4.25c-2.4 0-4.05 1.47-'
                     '4.05 4.17v2.33H7.42V13.9h2.73V22z"/>', cheio=True),
    "instagram": _svg('<rect x="3" y="3" width="18" height="18" rx="5"/>'
                      '<circle cx="12" cy="12" r="4"/>'
                      '<circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" '
                      'stroke="none"/>'),
    "linkedin": _svg('<rect x="3" y="3" width="18" height="18" rx="3.4"/>'
                     '<path d="M7.6 10.4v6.5"/><circle cx="7.6" cy="7.4" r="1" '
                     'fill="currentColor" stroke="none"/><path d="M11.5 16.9v-6.5"/>'
                     '<path d="M11.5 13.4c0-1.7 1.05-2.9 2.65-2.9s2.65 1.2 2.65 '
                     '2.9v3.5"/>'),
}


def ico(nome):
    return ICONES[nome]


# ============================================================================
# BLOCOS REUTILIZÁVEIS (seção 7 do CLAUDE.md)
# ============================================================================
def arte(prof, nome, alt, classe=""):
    """Imagem de uma posição do site.

    Prefere a FOTO (assets/fotos/<nome>.jpg) quando ela existe; se não existe,
    cai para a ARTE VETORIAL (assets/img/<nome>.svg). Assim dá para trocar
    posição por posição sem tocar no HTML: colocar o .jpg troca para foto,
    apagar o .jpg volta para o vetor. O site nunca fica com buraco.

    A foto vai dentro de .foto-tratada, que aplica o tratamento do guia da
    marca por CSS — baixa saturação com sobreposição verde. O arquivo original
    fica intacto, e o tratamento é ajustável sem rebaixar imagem.
    """
    cls = ((" " + classe) if classe else "")
    foto = os.path.join(RAIZ, "assets", "fotos", nome + ".jpg")

    if os.path.exists(foto):
        return ('\n<!-- FOTO — Pexels, licença de uso comercial livre.\n'
                '     Procedência em assets/fotos/CREDITOS.md.\n'
                '     Tratamento (dessatura + verde) vem do CSS .foto-tratada.\n'
                '     Para voltar ao vetor: apague o .jpg e rode build.py. -->\n'
                '<figure class="foto-tratada%s">\n'
                '  <img src="%sassets/fotos/%s.jpg" alt="%s" loading="lazy" '
                'decoding="async">\n</figure>\n'
                % (cls, "../" * prof, nome, alt))

    return ('\n<!-- ARTE VETORIAL — autoral, gerada por arte.py.\n'
            '     Vira foto assim que existir assets/fotos/%s.jpg -->\n'
            '<img class="arte%s" src="%sassets/img/%s.svg" alt="%s" loading="lazy">\n'
            % (nome, cls, "../" * prof, nome, alt))


def img_ph(rotulo, descricao, alt, classe=""):
    """Placeholder de imagem. O texto ALT sugerido fica no comentário HTML,
    para ser aplicado direto no Elementor quando a foto real entrar."""
    cls = "img-placeholder" + ((" " + classe) if classe else "")
    return (
        '\n<!-- IMAGEM A SUBSTITUIR | alt sugerido: "%s" -->\n'
        '<div class="%s" role="img" aria-label="%s">\n'
        '  <div>\n    %s\n'
        '    <span class="rotulo">%s</span>\n'
        '    <p class="desc">%s</p>\n'
        '  </div>\n</div>\n' % (alt, cls, alt, ico("imagem"), rotulo, descricao)
    )


def logo(prof):
    destino = u(prof, "home")
    return (
        '<!-- LOGOTIPO — PLACEHOLDER.\n'
        '     Reproduz a estrutura da assinatura oficial: símbolo de losangos\n'
        '     + wordmark "ágape" em caixa baixa + tagline. O símbolo aqui é uma\n'
        '     APROXIMAÇÃO: substituir pelo SVG vetorial oficial.\n'
        '     Regra do guia (item 02): versão preta sobre fundo claro, branca\n'
        '     sobre fundo escuro; não distorcer, inclinar nem aplicar efeitos. -->\n'
        '<a class="logo" href="%s" aria-label="%s — página inicial">\n'
        '  <span class="logo-marca">%s</span>\n'
        '  <span class="logo-texto">\n'
        '    <span class="logo-nome">ágape</span>\n'
        '    <span class="logo-sub">Saúde e Segurança do Trabalho</span>\n'
        '  </span>\n</a>' % (destino, EMPRESA, ico("losango"))
    )


def cabecalho(prof, atual):
    itens = ["home", "sobre", "servicos", "contato"]
    li = "\n".join(
        '      <li><a href="%s"%s>%s</a></li>' % (u(prof, k), marca(atual, k), ROTULOS[k])
        for k in itens
    )
    return """<header class="site-header">
  <div class="container header-inner">
    %s

    <!-- Menu mobile em CSS puro. No Elementor: menu responsivo nativo. -->
    <input type="checkbox" id="abrir-menu" class="nav-check" aria-label="Abrir e fechar o menu">
    <span class="nav-abre" aria-hidden="true">%s</span>

    <nav class="site-nav" aria-label="Menu principal">
      <ul>
%s
        <!-- ÁREA DO CLIENTE (SOC) — seção 5.5 do CLAUDE.md.
             Item CONDICIONAL: só entra se a Ágape for assinante do SOC/SOCRH.
             É apenas um link para o portal externo, não uma funcionalidade.
             Descomente e aponte para a URL do portal quando confirmado.
        <li><a href="#" target="_blank" rel="noopener">Área do Cliente</a></li>
        -->
        <li class="nav-cta-mobile">
          <a class="btn btn--primario" href="%s">Solicite um orçamento</a>
        </li>
      </ul>
    </nav>

    <div class="header-acoes">
      <a class="header-tel" href="%s">%s %s</a>
      <a class="btn btn--primario btn--pequeno" href="%s">Solicite um orçamento</a>
    </div>
  </div>
</header>""" % (
        logo(prof), ico("menu"), li,
        u(prof, "contato", "#orcamento"),
        CONTATO["fixo_href"], ico("telefone"), CONTATO["fixo"],
        u(prof, "contato", "#orcamento"),
    )


def rodape(prof):
    links_servicos = "\n".join(
        '        <li><a href="%s">%s</a></li>' % (u(prof, s["chave"]), s["nome"])
        for s in SERVICOS
    )
    return """<footer class="site-footer">
  <div class="container">
    <div class="footer-grade">

      <div>
        %s
        <p class="footer-sobre">Saúde e Segurança do Trabalho com excelência.
        Atuação em todo o Brasil desde 1999.</p>
        <div class="footer-redes">
          <a href="%s" target="_blank" rel="noopener" aria-label="Facebook da Ágape">%s</a>
          <a href="%s" target="_blank" rel="noopener" aria-label="Instagram da Ágape">%s</a>
          <a href="%s" target="_blank" rel="noopener" aria-label="LinkedIn da Ágape">%s</a>
        </div>
      </div>

      <div>
        <h2 class="footer-titulo">Serviços</h2>
        <ul class="footer-lista">
%s
        </ul>
      </div>

      <div>
        <h2 class="footer-titulo">Institucional</h2>
        <ul class="footer-lista">
          <li><a href="%s">Home</a></li>
          <li><a href="%s">Sobre Nós</a></li>
          <li><a href="%s">Contato</a></li>
          <li><a href="%s">Trabalhe conosco</a></li>
          <li><a href="%s">Política de Privacidade</a></li>
        </ul>
      </div>

      <div>
        <h2 class="footer-titulo">Contato</h2>
        <ul class="footer-contato">
          <li>%s
            <span>
              <span class="rotulo">Matriz</span>
              %s – %s<br>%s – %s, %s<br>%s
            </span>
          </li>
          <li>%s
            <span>
              <span class="rotulo">Recepção · fixo</span>
              <a href="%s">%s</a>
            </span>
          </li>
          <li>%s
            <span>
              <span class="rotulo">Recepção · WhatsApp</span>
              <a href="%s" target="_blank" rel="noopener">%s</a>
            </span>
          </li>
          <li>%s
            <span>
              <span class="rotulo">Comercial · WhatsApp</span>
              <a href="%s" target="_blank" rel="noopener">%s</a>
            </span>
          </li>
          <li>%s
            <span>
              <span class="rotulo">E-mail comercial</span>
              <a href="mailto:%s">%s</a>
            </span>
          </li>
        </ul>
      </div>

    </div>

    <div class="footer-base">
      <p>© %s %s. Todos os direitos reservados.</p>
      <nav aria-label="Links do rodapé">
        <a href="%s">Política de Privacidade</a>
      </nav>
      <p><strong>PROTÓTIPO</strong> — versão para aprovação, não é o site publicado.</p>
    </div>
  </div>
</footer>""" % (
        logo(prof),
        CONTATO["facebook"], ico("facebook"),
        CONTATO["instagram"], ico("instagram"),
        CONTATO["linkedin"], ico("linkedin"),
        links_servicos,
        u(prof, "home"), u(prof, "sobre"), u(prof, "contato"),
        u(prof, "contato"), u(prof, "privacidade"),
        ico("mapa"), CONTATO["rua"], CONTATO["bairro"],
        CONTATO["cidade"], CONTATO["uf"], CONTATO["cep"], CONTATO["complemento"],
        ico("telefone"), CONTATO["fixo_href"], CONTATO["fixo"],
        ico("whatsapp"), CONTATO["whats_recepcao_href"], CONTATO["whats_recepcao"],
        ico("whatsapp"), CONTATO["whats_comercial_href"], CONTATO["whats_comercial"],
        ico("email"), CONTATO["email"], CONTATO["email"],
        ANO, EMPRESA,
        u(prof, "privacidade"),
    )


def banner_lgpd(prof):
    return """
<!-- BANNER LGPD (seção 2 e 5 do CLAUDE.md).
     No protótipo é só visual: fecha via CSS, sem gravar nada — a regra 8
     proíbe localStorage. No WordPress vira plugin de consentimento que
     registra a escolha do visitante. -->
<input type="checkbox" id="lgpd-ok" class="lgpd-check" aria-label="Fechar aviso de cookies">
<div class="lgpd-banner" role="region" aria-label="Aviso de cookies">
  <p>Usamos cookies para melhorar sua experiência e medir a audiência do site.
  Ao continuar, você concorda com a nossa
  <a href="%s">Política de Privacidade</a>.</p>
  <div class="lgpd-acoes">
    <label class="btn btn--contorno btn--pequeno" for="lgpd-ok">Recusar</label>
    <label class="btn btn--primario btn--pequeno" for="lgpd-ok">Aceitar</label>
  </div>
</div>""" % u(prof, "privacidade")


def formulario(prof, servico_sel=None, ident="orcamento", titulo=None, sub=None):
    """FORMULÁRIO ÚNICO DE ORÇAMENTO (seção 5.1 do CLAUDE.md).

    5 campos, uma única tela, sem multi-step. O campo "Serviço de interesse"
    chega PRÉ-MARCADO conforme a página de origem — é o roteamento por intenção.
    No WordPress: Fluent Forms ou WPForms, gravando o lead + notificação.
    """
    titulo = titulo or "Solicite um orçamento"
    sub = sub or ("Retornamos com um escopo por serviço. Sem compromisso.")

    opcoes = ['<option value="">Selecione o serviço</option>']
    for s in SERVICOS:
        sel = " selected" if s["chave"] == servico_sel else ""
        opcoes.append('<option value="%s"%s>%s</option>' % (s["chave"], sel, s["nome"]))
    sel_geral = " selected" if servico_sel is None else ""
    opcoes.append('<option value="orientacao"%s>Ainda não sei — preciso de orientação'
                  '</option>' % sel_geral)
    opcoes_html = "\n              ".join(opcoes)

    origem = ("<!-- Serviço PRÉ-MARCADO nesta página: %s -->" % servico_sel
              if servico_sel else
              "<!-- Sem pré-marcação: formulário genérico -->")

    return """
<div class="form-cartao" id="%s">
  <h3>%s</h3>
  <p class="form-sub">%s</p>

  %s
  <form class="campos campos--2col" method="post" action="#" novalidate>
    <div class="campo">
      <label for="%s-nome">Nome <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="text" id="%s-nome" name="nome" placeholder="Seu nome" required>
    </div>
    <div class="campo">
      <label for="%s-empresa">Empresa <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="text" id="%s-empresa" name="empresa" placeholder="Nome da empresa" required>
    </div>
    <div class="campo">
      <label for="%s-telefone">Telefone <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="tel" id="%s-telefone" name="telefone" placeholder="(00) 00000-0000" required>
    </div>
    <div class="campo">
      <label for="%s-email">E-mail <span class="obrigatorio" aria-hidden="true">*</span></label>
      <input type="email" id="%s-email" name="email" placeholder="voce@empresa.com.br" required>
    </div>
    <div class="campo campo--largo">
      <label for="%s-servico">Serviço de interesse</label>
      <select id="%s-servico" name="servico">
              %s
      </select>
    </div>

    <div class="campo campo--largo">
      <label class="consentimento" for="%s-lgpd">
        <input type="checkbox" id="%s-lgpd" name="lgpd" required>
        <span>Autorizo a Ágape a usar meus dados para responder a esta
        solicitação, conforme a <a href="%s">Política de Privacidade</a>.</span>
      </label>
    </div>

    <div class="campo campo--largo form-rodape">
      <!-- type="button": no protótipo o formulário NÃO envia (seção 8). -->
      <button type="button" class="btn btn--primario btn--bloco">Solicitar orçamento</button>
      <p class="form-nota">Protótipo: o envio está desativado. No WordPress,
      este formulário grava o lead e dispara notificação por e-mail.</p>
    </div>
  </form>

  <p class="form-alternativa">
    Prefere conversar agora? <a href="%s" target="_blank" rel="noopener">Chamar o
    comercial no WhatsApp %s</a>
  </p>
</div>""" % (
        ident, titulo, sub, origem,
        ident, ident, ident, ident, ident, ident, ident, ident,
        ident, ident, opcoes_html,
        ident, ident, u(prof, "privacidade"),
        CONTATO["whats_comercial_href"], CONTATO["whats_comercial"],
    )


def bloco_formulario(prof, servico_sel=None, titulo_secao=None, texto_secao=None):
    """Seção escura com o formulário à direita. Usada na Home e nos serviços."""
    titulo_secao = titulo_secao or "Vamos dimensionar o que a sua empresa precisa"
    texto_secao = texto_secao or (
        "Conte o cenário da sua operação e devolvemos um escopo com o que é "
        "obrigatório, o que está vencido e o que pode esperar."
    )
    return """
<section class="secao secao--escura" id="orcamento">
  <div class="container form-bloco-grade">
    <div>
      <span class="olho">Orçamento</span>
      <h2>%s</h2>
      <p class="lead mt-md">%s</p>
      <ul class="lista-check mt-xl">
        <li>%s<span>Resposta do time comercial, não de robô</span></li>
        <li>%s<span>Escopo por serviço — você contrata só o que precisa</span></li>
        <li>%s<span>Diagnóstico inicial sem compromisso</span></li>
      </ul>
    </div>
    %s
  </div>
</section>""" % (titulo_secao, texto_secao,
                 ico("check"), ico("check"), ico("check"),
                 formulario(prof, servico_sel))


def bloco_fecho(prof, servico_sel=None, titulo_secao=None, texto_secao=None,
                titulo_cta=None, texto_cta=None):
    """Formulário + CTA final num único bloco escuro.

    Os dois eram seções escuras vizinhas, cada uma com a própria textura de
    losangos — e como o padrão reinicia a cada elemento, aparecia uma emenda
    visível na divisa. Aqui a textura fica no invólucro e as duas seções
    entram transparentes: o fundo passa a ser contínuo.
    """
    return """
<!-- FECHO DA PÁGINA — formulário + CTA sob uma textura só, sem emenda. -->
<div class="faixa-escura">
%s
%s
</div>""" % (
        bloco_formulario(prof, servico_sel, titulo_secao, texto_secao),
        bloco_cta_final(prof, titulo_cta, texto_cta),
    )


def bloco_faq(itens, titulo="Perguntas frequentes", olho="FAQ", intro=None):
    linhas = []
    for i, (p, r) in enumerate(itens):
        aberto = " open" if i == 0 else ""
        linhas.append(
            '      <details class="faq-item"%s>\n'
            '        <summary>%s</summary>\n'
            '        <div class="faq-resposta"><p>%s</p></div>\n'
            '      </details>' % (aberto, p, r)
        )
    intro_html = ('\n      <p class="lead">%s</p>' % intro) if intro else ""
    # O FAQ é sempre o último bloco claro antes do formulário (escuro),
    # então leva o recorte diagonal da transição (guia de identidade, item 03).
    return """
<section class="secao secao--alt com-diagonal com-diagonal--para-escuro">
  <div class="container container--estreito">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">%s</span>
      <h2>%s</h2>%s
    </div>
    <!-- Accordion nativo com <details>. No Elementor: widget Accordion. -->
    <div class="faq">
%s
    </div>
  </div>
</section>""" % (olho, titulo, intro_html, "\n".join(linhas))


# Dimensões reais de cada logo otimizado, lidas uma vez e reaproveitadas.
# Emitir width/height no <img> evita o salto de layout enquanto a imagem
# carrega — com 99 logos numa página, isso é a diferença entre a página
# assentar de vez e ficar pulando.
_DIM = {}


def _dimensao(numero):
    if numero not in _DIM:
        caminho = os.path.join(RAIZ, "assets", "logos", "%d.png" % numero)
        try:
            from PIL import Image
            with Image.open(caminho) as im:
                _DIM[numero] = im.size
        except Exception:
            _DIM[numero] = (560, 180)
    return _DIM[numero]


def _logo(prof, numero, nome):
    w, h = _dimensao(numero)
    return ('        <li><img src="%sassets/logos/%d.png" alt="%s" '
            'loading="lazy" decoding="async" width="%d" height="%d"></li>'
            % ("../" * prof, numero, nome, w, h))


def bloco_logos(prof, titulo="Empresas que confiam na Ágape", clientes=None):
    """Faixa estática de logos — usada nas páginas de serviço."""
    clientes = clientes or CLIENTES[:6]
    itens = "\n".join(_logo(prof, s, n) for s, n, _ in clientes)
    return """
    <!-- LOGOS DE CLIENTES — seção 5.3: prova social DILUÍDA pelo site.
         Cada arquivo em assets/logos/ é hoje um placeholder com o nome da
         empresa; substituir pelo PNG oficial mantendo o mesmo nome. -->
    <p class="faixa-logos-titulo">%s</p>
    <ul class="faixa-logos">
%s
    </ul>""" % (titulo, itens)


def bloco_setores_abas(prof):
    """Carteira por setor, em abas.

    Nove carrosséis empilhados viravam uma parede monótona: muito espaço para
    pouca informação, e ninguém lê até o fim. Em abas, o mesmo conteúdo cabe
    num bloco só — e a fileira de rótulos ("Indústria · Postos · Saúde ·
    Colégios…") já conta a história da variedade antes de qualquer logo
    aparecer. Quem se interessa por um setor clica e vê só aquele.

    CSS puro, via radio + :checked. No Elementor: widget Tabs (gratuito).
    """
    radios, rotulos, paineis = [], [], []
    for i, (chave, rotulo) in enumerate(SETORES.items()):
        grupo = [c for c in CLIENTES if c[2] == chave]
        if not grupo:
            continue
        marcado = " checked" if i == 0 else ""
        radios.append('      <input class="setor-radio" type="radio" name="setor" '
                      'id="set-%s"%s>' % (chave, marcado))
        rotulos.append('        <label for="set-%s">%s</label>' % (chave, rotulo))
        itens = "\n".join(_logo(prof, s, n) for s, n, _ in grupo)
        paineis.append('        <div class="setor-painel" id="painel-%s">\n'
                       '          <ul class="faixa-logos faixa-logos--densa">\n%s\n'
                       '          </ul>\n        </div>' % (chave, itens))

    return """
    <!-- CARTEIRA POR SETOR, EM ABAS — CSS puro (radio + :checked).
         No Elementor: widget Tabs, com uma galeria de imagens por aba. -->
    <div class="setores">
%s
      <div class="setor-abas" role="tablist">
%s
      </div>
      <div class="setor-paineis">
%s
      </div>
    </div>""" % ("\n".join(radios), "\n".join(rotulos), "\n".join(paineis))


def bloco_mural_setores(prof):
    """Versão anterior: um carrossel por setor, empilhados.

    Mantida porque pode ser útil numa página só de clientes, mas não é mais
    usada — na página de Serviços ela foi trocada pelo bloco em abas acima.
    """
    partes = []
    for i, (chave, rotulo) in enumerate(SETORES.items()):
        grupo = [c for c in CLIENTES if c[2] == chave]
        if not grupo:
            continue
        # cada setor vira um carrossel próprio; duplicamos a lista para o
        # laço não ter emenda. Setores pequenos ganham cópias extras, senão
        # a faixa fica curta demais para preencher a tela.
        repeticoes = max(2, -(-14 // len(grupo)))
        itens = "\n".join(_logo(prof, s, n) for s, n, _ in grupo)
        copia = itens.replace("<li>", '<li aria-hidden="true">')
        pista = itens + ("\n" + copia) * (repeticoes - 1)
        partes.append(
            '      <div class="setor">\n'
            '        <h3 class="setor-titulo">%s</h3>\n'
            '        <div class="marquee marquee--%s">\n'
            '          <ul class="marquee-grupo">\n%s\n          </ul>\n'
            '          <ul class="marquee-grupo" aria-hidden="true">\n%s\n          </ul>\n'
            '        </div>\n      </div>'
            % (rotulo, "esq" if i % 2 == 0 else "dir", pista,
               pista.replace("<li>", '<li aria-hidden="true">'))
        )
    return """
    <!-- CARROSSÉIS POR SETOR — a carteira real, um laço por segmento.
         No Elementor: um widget "Carrossel de imagens" por container. -->
    <div class="mural-setores">
%s
    </div>""" % "\n".join(partes)


def bloco_carrossel_logos(prof, linhas=3):
    """Carrossel infinito com a carteira inteira de clientes.

    O objetivo é mostrar VARIEDADE e QUANTIDADE: a carteira toda, dividida em
    faixas que correm em sentidos alternados. Cada faixa é duplicada no HTML
    para o laço ficar contínuo — a segunda cópia leva aria-hidden, para o
    leitor de tela não repetir a lista inteira.

    No Elementor: widget "Carrossel de imagens" (gratuito), com autoplay,
    loop infinito e velocidade lenta — um widget por faixa.
    """
    por_linha = -(-len(CLIENTES) // linhas)   # divisão arredondando para cima
    faixas = []
    for i in range(linhas):
        grupo = CLIENTES[i * por_linha:(i + 1) * por_linha]
        if not grupo:
            continue
        itens = "\n".join(_logo(prof, s, n) for s, n, _ in grupo)
        copia = itens.replace("<li>", '<li aria-hidden="true">')
        sentido = "esq" if i % 2 == 0 else "dir"
        faixas.append(
            '    <div class="marquee marquee--%s">\n'
            '      <ul class="marquee-grupo">\n%s\n      </ul>\n'
            '      <ul class="marquee-grupo" aria-hidden="true">\n%s\n      </ul>\n'
            '    </div>' % (sentido, itens, copia)
        )
    return """
  <!-- CARROSSEL DE CLIENTES — %d empresas da carteira real da Ágape.
       Animação puramente decorativa: com prefers-reduced-motion o laço para
       e as faixas ficam estáticas, sem perder conteúdo. -->
  <div class="carrossel-logos" role="group" aria-label="Empresas atendidas pela Ágape">
%s
  </div>""" % (len(CLIENTES), "\n".join(faixas))


def _partes_numero(valor):
    """Quebra "~20 mil" em ("~", 20, " mil") para o contador conseguir animar.
    Se não houver dígito, devolve None — o valor fica estático."""
    m = re.search(r"\d[\d.]*", valor)
    if not m:
        return None
    return valor[:m.start()], int(m.group(0).replace(".", "")), valor[m.end():]


def bloco_numeros(dados=None):
    dados = dados or NUMEROS_HOME
    itens = []
    for valor, rotulo, eh_placeholder in dados:
        cls = ' class="valor valor--placeholder"' if eh_placeholder else ' class="valor"'
        # Atributos para o contador. O valor final já está no HTML: sem JS,
        # ou com prefers-reduced-motion, o número aparece pronto.
        partes = None if eh_placeholder else _partes_numero(valor)
        extra = ""
        if partes:
            pre, num, suf = partes
            extra = (' data-conta="%d" data-prefixo="%s" data-sufixo="%s"'
                     % (num, pre, suf))
        itens.append('      <div class="numero-item">\n'
                     '        <span%s%s>%s</span>\n'
                     '        <span class="rotulo">%s</span>\n'
                     '      </div>' % (cls, extra, valor, rotulo))
    return """
    <!-- NÚMEROS DE OPERAÇÃO — todos CONFIRMADOS pelo cliente: 25 anos,
         +300 empresas, +600 CNPJs e ~20 mil vidas. Sem placeholder aqui. -->
    <div class="numeros">
%s
    </div>""" % "\n".join(itens)


def bloco_servicos(prof, titulo="Seis frentes, uma responsável só",
                   olho="Nossos serviços",
                   intro=("Cada serviço pode ser contratado separadamente — ou "
                          "todos juntos, com um único interlocutor."),
                   excluir=None, alt=False):
    excluir = excluir or []
    cards = []
    for s in SERVICOS:
        if s["chave"] in excluir:
            continue
        cards.append(
            '      <article class="card card-servico">\n'
            '        <span class="icone-caixa">%s</span>\n'
            '        <h3>%s</h3>\n'
            '        <p>%s</p>\n'
            '        <a class="link-seta" href="%s">Ver o serviço %s</a>\n'
            '      </article>' % (ico(s["icone"]), s["nome"], s["resumo"],
                                  u(prof, s["chave"]), ico("seta"))
        )
    classe = "secao secao--alt" if alt else "secao"
    return """
<section class="%s">
  <div class="container">
    <div class="secao-cabecalho secao-cabecalho--centro">
      <span class="olho">%s</span>
      <h2>%s</h2>
      <p class="lead">%s</p>
    </div>
    <!-- GRADE DE SERVIÇOS — bloco repetível. Cada card leva à página do
         serviço, onde o formulário já chega com o serviço pré-marcado
         (roteamento por intenção, seção 5.1). -->
    <div class="grade grade--3">
%s
    </div>
  </div>
</section>""" % (classe, olho, titulo, intro, "\n".join(cards))


def bloco_diferenciais(empilhado=False):
    """Os 4 diferenciais. `empilhado` os coloca em coluna única, para
    conviverem com uma arte ao lado."""
    itens = "\n".join(
        '      <div class="diferencial">\n'
        '        <span class="icone-caixa">%s</span>\n'
        '        <div>\n          <h3>%s</h3>\n          <p>%s</p>\n        </div>\n'
        '      </div>' % (ico(i), t, d)
        for i, t, d in DIFERENCIAIS
    )
    if empilhado:
        return itens
    return """
    <div class="grade grade--4">
%s
    </div>""" % itens


def bloco_cta_final(prof, titulo=None, texto=None):
    titulo = titulo or "Sua empresa está em dia com a SST?"
    texto = texto or ("Em poucos minutos a gente identifica o que está vencido, o "
                      "que falta e o que gera risco imediato de autuação.")
    return """
<section class="cta-final">
  <div class="container cta-final-inner">
    <div>
      <h2>%s</h2>
      <p>%s</p>
    </div>
    <div class="grupo-botoes">
      <a class="btn btn--claro" href="%s">Solicite um orçamento</a>
      <a class="btn btn--fantasma-claro" href="%s" target="_blank" rel="noopener">
        %s WhatsApp %s</a>
    </div>
  </div>
</section>""" % (titulo, texto, u(prof, "contato", "#orcamento"),
                 CONTATO["whats_comercial_href"], ico("whatsapp"),
                 CONTATO["whats_comercial"])


def trilha(prof, itens):
    """Breadcrumb. Marca o terreno para o schema BreadcrumbList no WordPress."""
    partes = ['      <li><a href="%s">Home</a></li>' % u(prof, "home")]
    for i, (rotulo, chave) in enumerate(itens):
        ultimo = i == len(itens) - 1
        if ultimo or chave is None:
            partes.append('      <li><span aria-current="page">%s</span></li>' % rotulo)
        else:
            partes.append('      <li><a href="%s">%s</a></li>' % (u(prof, chave), rotulo))
    return """    <nav class="trilha" aria-label="Você está aqui">
      <ol>
%s
      </ol>
    </nav>""" % "\n".join(partes)


# ============================================================================
# SCHEMA — terreno para SEO local (seção 5.4)
# ============================================================================
def schema_local():
    return """
<!-- SCHEMA LocalBusiness — só com dados CONFIRMADOS pelo cliente.
     Falta CNPJ e horário de funcionamento; completar na fase WordPress. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "%s",
  "description": "Medicina Ocupacional, Segurança do Trabalho, Treinamentos NRs e eSocial SST para empresas.",
  "foundingDate": "1999",
  "url": "https://%s",
  "email": "%s",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "%s — %s",
    "addressLocality": "%s",
    "addressRegion": "%s",
    "postalCode": "%s",
    "addressCountry": "BR"
  },
  "telephone": "+551147263150",
  "areaServed": "BR",
  "sameAs": ["%s", "%s", "%s"]
}
</script>""" % (EMPRESA, CONTATO["site"], CONTATO["email"],
                CONTATO["rua"], CONTATO["complemento"],
                CONTATO["cidade"], CONTATO["uf"], CONTATO["cep"],
                CONTATO["facebook"], CONTATO["instagram"], CONTATO["linkedin"])


# ============================================================================
# ESQUELETO DA PÁGINA
# ============================================================================
def documento(prof, chave, titulo_seo, meta, corpo, atual, schema="", nota_pagina=""):
    slug = "/" + PAGINAS[chave] if PAGINAS[chave] else "/"
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- ============================================================
     PÁGINA: %s
     SLUG (manter no WordPress): %s
     SEO title: %s
     SEO meta description: %s
     %s
     ============================================================ -->
<title>%s</title>
<meta name="description" content="%s">
<meta name="robots" content="noindex, nofollow"><!-- PROTÓTIPO: remover no site real -->

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%s">
%s
</head>
<body>

<a class="pular-para-conteudo" href="#conteudo">Pular para o conteúdo</a>

%s

<main id="conteudo">
%s
</main>

%s
%s

<!-- Único script do protótipo: anima os números da seção "em operação".
     É enfeite — o valor final já está no HTML, então sem JS nada se perde.
     No Elementor: widget Contador (gratuito). -->
<script src="%sassets/js/contadores.js" defer></script>

</body>
</html>
""" % (ROTULOS.get(chave, chave), slug, titulo_seo, meta, nota_pagina,
       titulo_seo, meta, css(prof), schema,
       cabecalho(prof, atual), corpo, rodape(prof), banner_lgpd(prof),
       "../" * prof)
