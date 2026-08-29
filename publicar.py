# -*- coding: utf-8 -*-
"""
EMPACOTADOR PARA ENTREGA — Ágape
=================================
Monta em _publicar/ apenas o que o navegador precisa, e um .zip do mesmo
conteúdo.

Por que existe: a pasta do projeto tem ~60 MB de coisas que o cliente não
deve receber — os .py que geram o site, os PNGs originais dos logos, as
imagens brutas do Gemini, folhas de contato. Subir tudo isso num serviço de
hospedagem (ou mandar por e-mail) é lento, confuso e expõe o código-fonte
sem necessidade.

O que vai: HTML, CSS, JS, imagens e logos. Nada mais.

Uso:  python publicar.py
Saída: _publicar/ (pasta pronta para arrastar) e agape-prototipo.zip
"""

import os
import shutil
import zipfile

RAIZ = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(RAIZ, "_publicar")
ZIP = os.path.join(RAIZ, "agape-prototipo.zip")

# Só isto entra. Lista explícita em vez de lista de exclusão: se amanhã
# alguém criar uma pasta nova com material interno, ela não vaza por descuido.
INCLUIR_PASTAS = ["assets"]
INCLUIR_ARQUIVOS = ["index.html"]

# subpastas de slug (cada uma com seu index.html)
SLUGS = [
    "sobre-nos", "servicos", "medicina-ocupacional-empresas",
    "seguranca-trabalho-empresas", "esocial-sst-empresas",
    "treinamentos-nrs-empresas", "gestao-ambulatorio-empresas",
    "clinica-credenciada", "contato", "politica-de-privacidade",
]

# dentro de assets/, o que não serve ao navegador
IGNORAR = shutil.ignore_patterns("*.md", "__pycache__", ".DS_Store", "Thumbs.db")


def main():
    if os.path.exists(SAIDA):
        shutil.rmtree(SAIDA)
    os.makedirs(SAIDA)

    for pasta in INCLUIR_PASTAS:
        origem = os.path.join(RAIZ, pasta)
        if os.path.isdir(origem):
            shutil.copytree(origem, os.path.join(SAIDA, pasta), ignore=IGNORAR)

    for arq in INCLUIR_ARQUIVOS:
        if os.path.exists(os.path.join(RAIZ, arq)):
            shutil.copy2(os.path.join(RAIZ, arq), SAIDA)

    paginas = 1
    for slug in SLUGS:
        origem = os.path.join(RAIZ, slug, "index.html")
        if os.path.exists(origem):
            destino = os.path.join(SAIDA, slug)
            os.makedirs(destino, exist_ok=True)
            shutil.copy2(origem, destino)
            paginas += 1

    # Netlify/Vercel/Cloudflare: garante que /sobre-nos/ resolva certo e que
    # o protótipo não seja indexado por buscador nenhum.
    with open(os.path.join(SAIDA, "robots.txt"), "w", encoding="utf-8",
              newline="\n") as f:
        f.write("User-agent: *\nDisallow: /\n")

    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for base, _dirs, arqs in os.walk(SAIDA):
            for a in arqs:
                caminho = os.path.join(base, a)
                z.write(caminho, os.path.relpath(caminho, SAIDA))

    peso = sum(os.path.getsize(os.path.join(b, a))
               for b, _d, arqs in os.walk(SAIDA) for a in arqs)

    print("Pacote pronto.")
    print("  _publicar/            %d páginas, %.1f MB" % (paginas, peso / 1048576))
    print("  agape-prototipo.zip   %.1f MB" % (os.path.getsize(ZIP) / 1048576))
    print()
    print("Para publicar: arraste a pasta _publicar/ em https://app.netlify.com/drop")
    print("Para mandar por e-mail/WhatsApp: use o .zip")


if __name__ == "__main__":
    main()
