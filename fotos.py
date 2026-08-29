# -*- coding: utf-8 -*-
"""
CURADORIA E PREPARO DAS FOTOS — Ágape
======================================
Baixa do Pexels as fotos escolhidas para cada posição do site, redimensiona e
salva em assets/fotos/.

SOBRE A LICENÇA
---------------
Todas vêm do Pexels, sob a Licença Pexels: uso comercial liberado, sem
necessidade de atribuição, sem custo. É por isso que não usei imagem de busca
genérica do Google — ali a maioria é protegida por direito autoral, e publicar
num site comercial criaria passivo justamente para uma empresa cujo argumento
de venda é conformidade legal.

Mesmo sem obrigação de crédito, CREDITOS.md registra a origem de cada arquivo:
se alguém questionar a procedência de uma imagem, a resposta está lá.

TRATAMENTO
----------
O guia da marca pede foto em P&B ou baixa saturação com sobreposição verde.
Isso NÃO é aplicado no arquivo — é feito por CSS, na classe .foto-tratada.
Assim o original fica intacto e o tratamento é ajustável sem rebaixar imagem.

Uso:  python fotos.py
      python fotos.py --forcar   (rebaixa tudo, ignorando o cache)
"""

import io
import os
import sys
import urllib.request

from PIL import Image

RAIZ = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(RAIZ, "assets", "fotos")

LARGURA = 1200          # o maior tamanho em que qualquer arte aparece no site
QUALIDADE = 82
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122 Safari/537.36")

# posição no site -> (id no Pexels, o que a foto mostra)
ESCOLHAS = {
    "hero":          (32845683, "Três profissionais de uniforme e capacete caminhando por uma planta industrial"),
    "diferenciais":  (8487720,  "Colaborador com colete refletivo segurando capacete, luvas e óculos de proteção"),
    "processo":      (36733315, "Reunião de trabalho em escritório, profissionais discutindo documentos"),
    "institucional": (9901861,  "Fachada envidraçada de edifício comercial vista de baixo"),
    "equipe":        (7876755,  "Equipe multidisciplinar reunida em volta de notebooks, em escritório iluminado"),
    "esporte":       (6203541,  "Partida de vôlei em quadra coberta"),
    "servicos":      (38070,    "Parede de capacetes de segurança de várias cores"),
    "medicina":      (4173251,  "Médica com estetoscópio em corredor de clínica"),
    "seguranca":     (2760241,  "Técnico de segurança avaliando equipamento industrial de grande porte"),
    "esocial":       (7652054,  "Equipe analisando dados em notebook, em escritório"),
    "treinamentos":  (7651804,  "Grupo em treinamento, reunido em volta de uma mesa de trabalho"),
    "ambulatorio":   (12955896, "Profissional de saúde de jaleco segurando estetoscópio"),
    "clinica":       (6627864,  "Recepção de clínica, atendente orientando um paciente"),
}


GERADAS = os.path.join(RAIZ, "fotos-geradas")


def baixar(pid):
    url = ("https://images.pexels.com/photos/%d/pexels-photo-%d.jpeg"
           "?auto=compress&cs=tinysrgb&w=1600" % (pid, pid))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=40).read()


def origem(slot, pid):
    """De onde vem a imagem daquela posição.

    Prioridade: o arquivo que você colocou em fotos-geradas/ ganha do Pexels.
    Assim dá para substituir posição por posição sem mexer em código — basta
    salvar o .jpg com o nome do slot e rodar este script de novo.
    """
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        local = os.path.join(GERADAS, slot + ext)
        if os.path.exists(local):
            with open(local, "rb") as f:
                return f.read(), "local"
    return baixar(pid), "pexels"


def main():
    forcar = "--forcar" in sys.argv
    os.makedirs(DESTINO, exist_ok=True)

    locais, baixadas, falhas = 0, 0, []
    antes = depois = 0

    for slot, (pid, _desc) in ESCOLHAS.items():
        destino = os.path.join(DESTINO, slot + ".jpg")
        try:
            bruto, de_onde = origem(slot, pid)
            antes += len(bruto)

            im = Image.open(io.BytesIO(bruto)).convert("RGB")
            if im.width > LARGURA:
                alt = round(im.height * LARGURA / im.width)
                im = im.resize((LARGURA, alt), Image.LANCZOS)
            im.save(destino, "JPEG", quality=QUALIDADE, optimize=True,
                    progressive=True)

            depois += os.path.getsize(destino)
            if de_onde == "local":
                locais += 1
            else:
                baixadas += 1
        except Exception as e:
            falhas.append("%s (%d): %s" % (slot, pid, e))

    creditos(os.path.join(DESTINO, "CREDITOS.md"))

    print("Fotos prontas em assets/fotos/")
    print("  de fotos-geradas/: %d | do Pexels: %d" % (locais, baixadas))
    print("  peso: %.1f MB  ->  %.1f MB" % (antes / 1048576, depois / 1048576))
    for f in falhas:
        print("  FALHOU: " + f)


def creditos(caminho):
    linhas = [
        "# Créditos das fotos",
        "",
        "Todas do **Pexels**, sob a [Licença Pexels]"
        "(https://www.pexels.com/pt-br/license/): uso comercial permitido,",
        "sem custo e sem exigência de atribuição. O crédito abaixo existe por",
        "rastreabilidade — para provar a procedência se alguém questionar.",
        "",
        "| Arquivo | Página de origem | Conteúdo |",
        "|---|---|---|",
    ]
    for slot, (pid, desc) in ESCOLHAS.items():
        linhas.append("| `%s.jpg` | https://www.pexels.com/photo/%d/ | %s |"
                      % (slot, pid, desc))
    linhas += [
        "",
        "## Para trocar uma foto",
        "",
        "Edite `ESCOLHAS` em `fotos.py` com o novo id do Pexels e rode",
        "`python fotos.py --forcar`. Ou simplesmente substitua o `.jpg` na",
        "pasta por outro arquivo com o mesmo nome.",
        "",
        "## Para voltar à arte vetorial",
        "",
        "Apague o `.jpg` correspondente e rode `python build.py`. O site volta",
        "sozinho a usar a arte gerada por `arte.py` naquela posição.",
    ]
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(linhas) + "\n")


if __name__ == "__main__":
    main()
