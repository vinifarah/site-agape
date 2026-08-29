# -*- coding: utf-8 -*-
"""
GERADOR DE ARTE VETORIAL — Ágape
=================================
Compõe as imagens do site em SVG, na linguagem do guia de identidade:
verde profundo como base, verde-limão como única ênfase, malha de losangos,
cantos discretamente arredondados.

POR QUE VETOR E NÃO FOTO
------------------------
Não há banco de fotos da Ágape, e foto genérica de banco de imagens
enfraquece um site institucional — é o tipo de imagem que o visitante já viu
em dez concorrentes. A arte vetorial aqui é autoral, escala sem perder
nitidez, pesa poucos KB e obedece à paleta sem tratamento.

Quando o cliente tiver as fotos reais, a troca é direta: o `<img>` sai e entra
a foto com a classe .foto-tratada, que já aplica o tratamento do guia
(P&B ou baixa saturação + sobreposição verde).

Uso:  python arte.py
Saída: assets/img/*.svg
"""

import os

from blocos import ICONES

RAIZ = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(RAIZ, "assets", "img")

PROFUNDO = "#112005"
ESCURO   = "#0B1703"
MEIO     = "#16290A"
INSTIT   = "#46B148"
INTER    = "#80C447"
LIMAO    = "#AFD745"


# ---------------------------------------------------------------------------
# Peças de composição
# ---------------------------------------------------------------------------
def losango(cx, cy, r, **at):
    """Losango centrado — a forma-base de toda a identidade."""
    d = "M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" % (
        cx, cy - r, cx + r, cy, cx, cy + r, cx - r, cy)
    return "<path d=\"%s\" %s/>" % (d, _at(at))


def _at(at):
    return " ".join('%s="%s"' % (k.replace("_", "-"), v) for k, v in at.items())


def _defs(w, h, glow_x, glow_y, giro):
    """Gradientes, malha e recorte do quadro — iguais em todas as artes."""
    return """  <defs>
    <linearGradient id="fundo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%%" stop-color="%s"/>
      <stop offset="55%%" stop-color="%s"/>
      <stop offset="100%%" stop-color="%s"/>
    </linearGradient>
    <radialGradient id="brilho">
      <stop offset="0%%" stop-color="%s" stop-opacity=".55"/>
      <stop offset="100%%" stop-color="%s" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="brilho2">
      <stop offset="0%%" stop-color="%s" stop-opacity=".30"/>
      <stop offset="100%%" stop-color="%s" stop-opacity="0"/>
    </radialGradient>
    <pattern id="malha" width="46" height="46" patternUnits="userSpaceOnUse"
             patternTransform="rotate(%d)">
      <path d="M0 0 H46 M0 0 V46" stroke="%s" stroke-opacity=".16" stroke-width="1" fill="none"/>
    </pattern>
    <clipPath id="quadro">
      <rect x="0" y="0" width="%d" height="%d" rx="18"/>
    </clipPath>
  </defs>
  <g clip-path="url(#quadro)">
    <rect width="%d" height="%d" fill="url(#fundo)"/>
    <rect width="%d" height="%d" fill="url(#malha)"/>
    <circle cx="%d" cy="%d" r="%d" fill="url(#brilho)"/>
    <circle cx="%d" cy="%d" r="%d" fill="url(#brilho2)"/>""" % (
        MEIO, PROFUNDO, ESCURO,
        INSTIT, INSTIT, LIMAO, LIMAO,
        giro, LIMAO,
        w, h, w, h, w, h,
        glow_x, glow_y, int(w * .46),
        int(w * .18), int(h * .88), int(w * .3))


# --- motivos centrais -------------------------------------------------------
def motivo_ninho(cx, cy, r):
    """Losangos concêntricos: o símbolo da marca, respirando."""
    p = []
    for i, k in enumerate([1, .74, .5, .28]):
        op = .16 + i * .16
        p.append(losango(cx, cy, r * k, fill="none", stroke=LIMAO,
                         stroke_opacity="%.2f" % op, stroke_width="2"))
    p.append(losango(cx, cy, r * .13, fill=LIMAO, fill_opacity=".9"))
    return "\n    ".join(p)


def motivo_malha(cx, cy, r):
    """Quatro losangos em cruz, um deles aceso — a ideia de rede."""
    d = r * .52
    p = [losango(cx, cy, r, fill="none", stroke=LIMAO,
                 stroke_opacity=".22", stroke_width="2")]
    for i, (dx, dy) in enumerate([(0, -d), (d, 0), (0, d), (-d, 0)]):
        aceso = (i == 1)
        p.append(losango(cx + dx, cy + dy, r * .38,
                         fill=LIMAO if aceso else "none",
                         fill_opacity=".85" if aceso else "0",
                         stroke=LIMAO, stroke_opacity=".5" if aceso else ".3",
                         stroke_width="2"))
    return "\n    ".join(p)


def motivo_planos(cx, cy, r):
    """Planos translúcidos empilhados, como camadas de proteção."""
    p = []
    for i in range(4):
        o = i * r * .17
        p.append(losango(cx, cy - o, r - i * r * .07,
                         fill=LIMAO, fill_opacity="%.3f" % (.05 + i * .05),
                         stroke=LIMAO, stroke_opacity="%.2f" % (.14 + i * .13),
                         stroke_width="1.6"))
    return "\n    ".join(p)


def motivo_orbita(cx, cy, r):
    """Anéis abertos girando em torno de um núcleo aceso."""
    p = [
        '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-opacity=".2" '
        'stroke-width="2" stroke-dasharray="7 13"/>' % (cx, cy, int(r * 1.06), LIMAO),
        '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-opacity=".3" '
        'stroke-width="2" stroke-dasharray="30 18"/>' % (cx, cy, int(r * .78), INTER),
    ]
    p.append(losango(cx, cy, r * .42, fill="none", stroke=LIMAO,
                     stroke_opacity=".65", stroke_width="2.4"))
    p.append(losango(cx, cy, r * .17, fill=LIMAO, fill_opacity=".92"))
    return "\n    ".join(p)


MOTIVOS = [motivo_ninho, motivo_malha, motivo_planos, motivo_orbita]


def _poeira(w, h, semente):
    """Losangos soltos, para o fundo não ficar chapado."""
    pontos = [(.12, .22, 9), (.86, .34, 12), (.22, .8, 7),
              (.74, .84, 9), (.93, .68, 6), (.06, .55, 6)]
    p = []
    for i, (fx, fy, r) in enumerate(pontos):
        if (i + semente) % 3 == 0:
            continue
        p.append(losango(w * fx, h * fy, r, fill=LIMAO,
                         fill_opacity="%.2f" % (.14 + (i % 3) * .1)))
    return "\n    ".join(p)


# ---------------------------------------------------------------------------
# Composição
# ---------------------------------------------------------------------------
def compor(w, h, icone, motivo, glow=(.78, .2), giro=45, semente=0):
    """Monta uma arte completa. `icone` é a chave em blocos.ICONES."""
    cx, cy = w * .5, h * .5
    r = min(w, h) * .3

    # o ícone temático entra grande e apagado, como marca-d'água
    esc = min(w, h) / 24.0 * .78
    ix, iy = cx - 12 * esc, cy - 12 * esc
    svg_icone = ICONES[icone]
    svg_icone = svg_icone.replace(
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"',
        '<g transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" '
        'stroke-opacity=".13" stroke-width="1.7"' % (ix, iy, esc, LIMAO)
    ).replace(
        '<svg viewBox="0 0 24 24" fill="currentColor"',
        '<g transform="translate(%.1f %.1f) scale(%.3f)" fill="%s" fill-opacity=".12"'
        % (ix, iy, esc, LIMAO)
    ).replace("</svg>", "</g>").replace(' aria-hidden="true"', "")

    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"
     preserveAspectRatio="xMidYMid slice" role="presentation">
  <!-- Arte autoral gerada por arte.py, na linguagem do guia de identidade.
       Substituível por foto real: ver .foto-tratada no style.css -->
%s
    %s
    %s
    %s
  </g>
  <rect x=".75" y=".75" width="%.1f" height="%.1f" rx="17.5"
        fill="none" stroke="%s" stroke-opacity=".22" stroke-width="1.5"/>
</svg>
""" % (w, h, _defs(w, h, int(w * glow[0]), int(h * glow[1]), giro),
       svg_icone, MOTIVOS[motivo](cx, cy, r), _poeira(w, h, semente),
       w - 1.5, h - 1.5, LIMAO)


# ---------------------------------------------------------------------------
# HERO — composição própria, mais gráfica e sem texto nenhum
# ---------------------------------------------------------------------------
def hero():
    w, h = 760, 620
    cx, cy = 380, 300

    camadas = []
    # escudo em camadas: losangos alongados, um sobre o outro
    for i, k in enumerate([1.0, .82, .64, .46, .28]):
        camadas.append(
            '<path d="M%.0f %.0f L%.0f %.0f L%.0f %.0f L%.0f %.0f Z" '
            'fill="%s" fill-opacity="%.3f" stroke="%s" stroke-opacity="%.2f" '
            'stroke-width="1.8"/>' % (
                cx, cy - 250 * k, cx + 190 * k, cy - 40 * k,
                cx, cy + 250 * k, cx - 190 * k, cy - 40 * k,
                LIMAO, .035 + i * .045, LIMAO, .16 + i * .13))

    # núcleo aceso
    camadas.append(losango(cx, cy - 40, 34, fill=LIMAO, fill_opacity=".95"))
    camadas.append(losango(cx, cy - 40, 62, fill="none", stroke=LIMAO,
                           stroke_opacity=".45", stroke_width="2"))

    # órbita quebrada em volta
    camadas.append(
        '<circle cx="%d" cy="%d" r="228" fill="none" stroke="%s" '
        'stroke-opacity=".16" stroke-width="2" stroke-dasharray="4 16"/>'
        % (cx, cy - 40, LIMAO))

    # satélites
    for fx, fy, r, op in [(.14, .26, 13, .5), (.88, .4, 17, .38),
                          (.78, .82, 11, .3), (.2, .78, 9, .34),
                          (.5, .06, 8, .28)]:
        camadas.append(losango(w * fx, h * fy, r, fill=LIMAO, fill_opacity="%.2f" % op))

    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="presentation">
  <!-- ARTE PRINCIPAL DO HERO — composição autoral.
       Escudo construído em camadas a partir do losango da marca: a ideia é
       proteção que se acumula, não uma cena literal de trabalho.
       Sem texto: quem carrega a mensagem é a headline ao lado. -->
%s
    %s
  </g>
</svg>
""" % (w, h, _defs(w, h, int(w * .5), int(h * .34), 45), "\n    ".join(camadas))


# ---------------------------------------------------------------------------
# Catálogo: cada arte do site
# ---------------------------------------------------------------------------
# arquivo -> (largura, altura, ícone, motivo, glow, giro, semente)
ARTES = {
    "hero":            None,     # tratado à parte
    "medicina":        (720, 540, "estetoscopio", 0, (.76, .2),  45, 0),
    "seguranca":       (720, 540, "capacete",     2, (.24, .24), 45, 1),
    "esocial":         (720, 540, "sistema",      3, (.8, .3),   45, 2),
    "treinamentos":    (720, 540, "formacao",     1, (.3, .18),  45, 0),
    "ambulatorio":     (720, 540, "predio",       2, (.72, .78), 45, 1),
    "clinica":         (720, 540, "rede",         1, (.5, .18),  45, 2),
    "servicos":        (720, 540, "alvo",         3, (.78, .24), 45, 1),
    "equipe":          (720, 540, "usuarios",     0, (.26, .3),  45, 2),
    "institucional":   (720, 540, "escudo",       2, (.74, .22), 45, 0),
    "esporte":         (960, 540, "coracao",      1, (.18, .26), 45, 1),
    "diferenciais":    (720, 620, "raio",         3, (.62, .2),  45, 2),
    "processo":        (720, 480, "relogio",      0, (.8, .26),  45, 0),
    "mapa":            (960, 412, "mapa",         1, (.5, .5),   45, 1),
}


def main():
    os.makedirs(DESTINO, exist_ok=True)

    caminho = os.path.join(DESTINO, "hero.svg")
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(hero())
    gerados = ["hero.svg"]

    for nome, cfg in ARTES.items():
        if cfg is None:
            continue
        w, h, ic, mot, glow, giro, sem = cfg
        with open(os.path.join(DESTINO, nome + ".svg"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(compor(w, h, ic, mot, glow, giro, sem))
        gerados.append(nome + ".svg")

    total = sum(os.path.getsize(os.path.join(DESTINO, g)) for g in gerados)
    print("Artes geradas em assets/img/ — %d arquivos, %.0f KB no total"
          % (len(gerados), total / 1024))
    for g in gerados:
        print("  " + g)


if __name__ == "__main__":
    main()
