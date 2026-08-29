# -*- coding: utf-8 -*-
"""
CARTEIRA DE CLIENTES — Ágape Saúde e Segurança do Trabalho
===========================================================
Os logos vieram na pasta png-clientes/, numerados de 1 a 107.

- 1 a 8   → composições (várias marcas numa imagem só). NÃO entram como logo
            individual; ficam de fora da carteira.
- 9 a 107 → um logo por arquivo. São os 99 usados no site.

Cada item abaixo é (arquivo, nome, setor). O `nome` vira o texto ALT da
imagem — é o que leitor de tela e Google leem.

Os arquivos originais têm 2000px e somam ~14 MB. otimizar_logos.py gera as
versões web em assets/logos/, que são as que o site carrega.
"""

# (numero do arquivo em png-clientes/, nome, setor)
CLIENTES = [
    # --- Indústria ----------------------------------------------------------
    (9,   "Elgin",                      "industria"),
    (10,  "FAME",                       "industria"),
    (11,  "Rinnai",                     "industria"),
    (21,  "Metalúrgica JAM",            "industria"),
    (22,  "EDDF Indústria e Comércio",  "industria"),
    (23,  "Cobral",                     "industria"),
    (25,  "SBR Brasil",                 "industria"),
    (26,  "Refrio Elgin",               "industria"),
    (27,  "Quali Bags",                 "industria"),
    (28,  "Savasa",                     "industria"),
    (29,  "Reciclatec",                 "industria"),
    (30,  "Rottotanques",               "industria"),
    (44,  "Índice Malhas",              "industria"),
    (45,  "Mogiaço",                    "industria"),
    (46,  "Mogi Telhas",                "industria"),
    (47,  "Mogi Lumi",                  "industria"),

    # --- Postos e redes de combustível -------------------------------------
    (12,  "Rede Duque",                 "postos"),
    (13,  "Posto's Vale+",              "postos"),
    (14,  "Rede 28",                    "postos"),
    (15,  "Postos Volt",                "postos"),
    (16,  "Tigre do Vale",              "postos"),
    (17,  "Rede Totality",              "postos"),
    (18,  "Postos Quality",             "postos"),
    (19,  "Auto Posto Liberty",         "postos"),
    (20,  "Auto Posto Vipam",           "postos"),
    (63,  "Distribuidora de Bebidas Gouveia", "postos"),

    # --- Construção e engenharia -------------------------------------------
    (24,  "Gabco",                      "construcao"),
    (31,  "MSI Engenharia",             "construcao"),
    (32,  "Adhkon Construtora",         "construcao"),
    (33,  "Grupo Jatobá Madeiras",      "construcao"),
    (34,  "Oceannia",                   "construcao"),
    (42,  "Fixar Soluções",             "construcao"),
    (105, "Arrumando a Casa",           "construcao"),

    # --- Segurança patrimonial e facilities --------------------------------
    (35,  "Grupo Dimensão",             "seguranca"),
    (36,  "MC Segurança",               "seguranca"),
    (37,  "Grupo Líder",                "seguranca"),
    (38,  "Zelo Segurança",             "seguranca"),
    (39,  "Prisma",                     "seguranca"),
    (40,  "FRX",                        "seguranca"),
    (41,  "Grupo Alliança",             "seguranca"),
    (43,  "Assibraff",                  "seguranca"),
    (53,  "Oliveira Uniformes",         "seguranca"),

    # --- Alimentação e varejo -----------------------------------------------
    (54,  "Supermercados Alabarce",     "varejo"),
    (55,  "Da Praça Supermercados",     "varejo"),
    (56,  "Jolie Padaria",              "varejo"),
    (57,  "Tita Padaria",               "varejo"),
    (58,  "Jafet Padaria",              "varejo"),
    (59,  "Padoca da Beth",             "varejo"),
    (60,  "Urakami Cogumelos",          "varejo"),
    (61,  "Sítio Hiromi",               "varejo"),
    (62,  "Due Grani",                  "varejo"),
    (64,  "Kaishi Sushi",               "varejo"),
    (65,  "Hioki Sushi",                "varejo"),
    (66,  "Reiwa Sushi",                "varejo"),
    (67,  "Bistecão Casa de Carnes",    "varejo"),
    (68,  "Mega Boi Carnes",            "varejo"),
    (69,  "Costelão Paulista",          "varejo"),
    (70,  "Jolie Grill",                "varejo"),
    (71,  "Tita Petit",                 "varejo"),
    (72,  "Predileto Restaurante",      "varejo"),
    (73,  "Bar do Alemão",              "varejo"),

    # --- Transporte e logística ---------------------------------------------
    (74,  "Grupo Faberge",              "logistica"),
    (75,  "Pontal Autos",               "logistica"),
    (76,  "MD Express",                 "logistica"),
    (77,  "StartLog",                   "logistica"),
    (78,  "OK Brazil",                  "logistica"),
    (79,  "Suzuki Faberge Motos",       "logistica"),
    (80,  "Vipol Transportes",          "logistica"),

    # --- Saúde e diagnóstico ------------------------------------------------
    (84,  "Saint Nicholas Medical",     "saude"),
    (85,  "Cliente Ágape",              "saude"),
    (86,  "Saint Nicholas Odontologia", "saude"),
    (87,  "MedQuest",                   "saude"),
    (88,  "Instituto Saint Nicholas Care", "saude"),
    (89,  "Clínica São Vito",           "saude"),
    (90,  "Suzanclin",                  "saude"),
    (91,  "Totall Check-up",            "saude"),
    (92,  "Lombardi Pupo Diagnósticos", "saude"),
    (93,  "Cardioclin Mogi",            "saude"),
    (94,  "São Francisco",              "saude"),
    (95,  "Casalab",                    "saude"),
    (96,  "Tamara Sandoval",            "saude"),
    (97,  "Brasimed",                   "saude"),

    # --- Serviços, tecnologia, seguros e ótica ------------------------------
    (48,  "EletroBidu",                 "servicos"),
    (49,  "TeraCorp",                   "servicos"),
    (50,  "Mogi Fibra",                 "servicos"),
    (52,  "UPIX",                       "servicos"),
    (81,  "Galeão Corretora de Seguros", "servicos"),
    (82,  "Sponda Seguros",             "servicos"),
    (83,  "Jukar",                      "servicos"),
    (98,  "Óculos Mania",               "servicos"),
    (99,  "GoldenMix Ótica",            "servicos"),
    (100, "Ótica Indaiá",               "servicos"),

    # --- Educação e institucional -------------------------------------------
    (51,  "Microcamp",                  "institucional"),
    (101, "Clube de Campo de Mogi das Cruzes", "institucional"),
    (102, "Objetivo Mogi das Cruzes",   "institucional"),
    (103, "Colégio Millenium Construtivo", "institucional"),
    (104, "Colégio Cristão Leão de Judá", "institucional"),
    (106, "Cáritas Diocesana de Mogi das Cruzes", "institucional"),
    (107, "Suzano Vôlei",               "institucional"),
]

# O arquivo 85 é uma marca em forma de "A" com barras diagonais que não deu
# para nomear com certeza a partir da imagem. Ficou com ALT genérico em vez
# de entrar com um nome chutado — corrigir quando o cliente confirmar.
ALT_PENDENTE = [85]

SETORES = {
    "industria":     "Indústria",
    "postos":        "Postos e redes de combustível",
    "construcao":    "Construção e engenharia",
    "seguranca":     "Segurança patrimonial e facilities",
    "varejo":        "Alimentação e varejo",
    "logistica":     "Transporte e logística",
    "saude":         "Saúde e diagnóstico",
    "servicos":      "Serviços, tecnologia e seguros",
    "institucional": "Educação e institucional",
}


def por_setor(*setores):
    """Clientes de um ou mais setores, na ordem da lista."""
    alvo = set(setores)
    return [c for c in CLIENTES if c[2] in alvo]


TOTAL = len(CLIENTES)
