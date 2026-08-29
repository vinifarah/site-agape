# -*- coding: utf-8 -*-
"""
OTIMIZADOR DE LOGOS — Ágape
============================
Lê os originais de png-clientes/ (2000px, ~14 MB no total) e gera as versões
que o site carrega, em assets/logos/.

O que faz em cada arquivo:
  1. recorta a moldura vazia em volta do logo (os originais têm muita sobra);
  2. reduz para 200px de altura, que é o dobro do tamanho exibido — fica
     nítido em tela retina sem pesar;
  3. salva como PNG otimizado com transparência preservada.

Resultado: de ~14 MB para poucas centenas de KB no total, que é a diferença
entre uma faixa de logos que carrega e uma que trava a página.

Uso:  python otimizar_logos.py
"""

import os

from PIL import Image

from clientes import CLIENTES

RAIZ = os.path.dirname(os.path.abspath(__file__))
ORIGEM = os.path.join(RAIZ, "png-clientes")
DESTINO = os.path.join(RAIZ, "assets", "logos")

ALTURA = 168      # ~3x a altura de exibição (46px), nítido em tela retina
MARGEM = 6        # respiro em volta do logo depois do recorte

# Os originais são todos monocromáticos. Guardar em tons de cinza + alfa (LA)
# em vez de RGBA corta ~metade do peso sem diferença visível — e o site ainda
# dessatura tudo por CSS, então não há cor a perder.
MODO_SAIDA = "LA"


def recortar(im):
    """Remove a sobra transparente/branca em volta do logo."""
    alfa = im.getchannel("A")
    caixa = alfa.getbbox()
    if caixa is None:                       # imagem sem canal alfa útil
        fundo = Image.new("RGB", im.size, (255, 255, 255))
        cinza = Image.composite(im.convert("RGB"), fundo, alfa).convert("L")
        caixa = cinza.point(lambda p: 255 if p < 245 else 0).getbbox()
    return im.crop(caixa) if caixa else im


def main():
    if not os.path.isdir(ORIGEM):
        raise SystemExit("pasta png-clientes/ não encontrada")
    os.makedirs(DESTINO, exist_ok=True)

    # limpa placeholders antigos (nomeados por slug); os novos são numéricos
    for antigo in os.listdir(DESTINO):
        if antigo.endswith(".png") and not antigo[:-4].isdigit():
            os.remove(os.path.join(DESTINO, antigo))

    antes = depois = 0
    faltando = []

    for numero, nome, _setor in CLIENTES:
        origem = os.path.join(ORIGEM, "%d.png" % numero)
        if not os.path.exists(origem):
            faltando.append(numero)
            continue

        antes += os.path.getsize(origem)
        im = Image.open(origem).convert("RGBA")
        im = recortar(im)

        escala = ALTURA / im.height
        im = im.resize((max(1, round(im.width * escala)), ALTURA), Image.LANCZOS)

        tela = Image.new("RGBA", (im.width + MARGEM * 2, ALTURA + MARGEM * 2),
                         (0, 0, 0, 0))
        tela.paste(im, (MARGEM, MARGEM), im)

        destino = os.path.join(DESTINO, "%d.png" % numero)
        tela.convert(MODO_SAIDA).save(destino, "PNG", optimize=True)
        depois += os.path.getsize(destino)

    print("Logos otimizados em assets/logos/")
    print("  processados: %d de %d" % (len(CLIENTES) - len(faltando), len(CLIENTES)))
    print("  peso: %.1f MB  ->  %.0f KB" % (antes / 1048576, depois / 1024))
    if faltando:
        print("  AUSENTES em png-clientes/: %s" % faltando)


if __name__ == "__main__":
    main()
