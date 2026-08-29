# -*- coding: utf-8 -*-
"""
CONTEÚDO DO PROTÓTIPO — Ágape Saúde e Segurança do Trabalho
============================================================
Todo o texto do site mora aqui, separado da montagem (build.py).

REGRA (seção 8 do CLAUDE.md): nada de dado inventado.
- Fatos declarados pelo cliente (fundação em 1999, 25+ anos, atendimento
  nacional, os 6 serviços) são usados como verdade.
- Conteúdo técnico de SST (NRs, PGR, PCMSO, eventos do eSocial) é
  descritivo do setor e serve como PLACEHOLDER REALISTA para o cliente
  ver o tom — precisa de revisão do responsável técnico antes de publicar.
- Números de operação, depoimentos e nomes de clientes ficam marcados
  entre colchetes, ex.: [DEPOIMENTO A COLETAR].
"""

# ============================================================================
# HOME
# ============================================================================
HOME = {
    "title": "Ágape SST | Medicina e Segurança do Trabalho para empresas",
    "meta": (
        "Há mais de 25 anos em Medicina Ocupacional, Segurança do Trabalho, "
        "Treinamentos NRs e eSocial. Laudos com validade jurídica, prazos "
        "cumpridos e atendimento humanizado em todo o Brasil."
    ),
    "h1_antes": "Saúde e Segurança do Trabalho ",
    "h1_destaque": "com excelência",
    "lead": (
        "Atuamos em todo o Brasil há mais de 25 anos com soluções completas em "
        "Medicina Ocupacional, Segurança do Trabalho, Treinamentos e eSocial. "
        "Garantimos laudos técnicos com validade jurídica, cumprimento de prazos "
        "e atendimento humanizado."
    ),
    "confianca": [
        ("calendario", "Desde 1999, em Mogi das Cruzes-SP"),
        ("globo", "Atendimento em todo o Brasil"),
        ("escudo", "Laudos com validade jurídica"),
    ],
    "hero_img": (
        "Foto principal",
        "Equipe da Ágape em atendimento — sugestão: profissional de saúde "
        "ocupacional com colaborador de empresa cliente.",
        "Profissional de saúde ocupacional da Ágape atendendo um colaborador",
    ),
    "hero_card": ("+300", "empresas atendidas e cerca de 20 mil vidas sob "
                          "o nosso cuidado"),
}

# Números de operação — todos CONFIRMADOS pelo cliente (portfólio institucional
# e complemento enviado depois). Não há mais placeholder nesta seção.
NUMEROS_HOME = [
    ("25", "anos de atuação, desde 1999", False),
    ("+300", "empresas atendidas", False),
    ("+600", "CNPJs atendidos", False),
    ("~20 mil", "vidas sob nosso cuidado", False),
]

# A carteira de clientes vive em clientes.py (96 empresas, com o slug do
# arquivo de logo de cada uma).

DIFERENCIAIS = [
    ("calendario", "25 anos de experiência",
     "Sede fundada em 1999, em Mogi das Cruzes. Mais de 300 empresas e cerca "
     "de 20 mil vidas sob o nosso cuidado."),
    ("usuarios", "Equipe multidisciplinar",
     "Medicina do trabalho, enfermagem, engenharia e segurança do trabalho na "
     "mesma casa."),
    ("raio", "Descomplicamos a SST",
     "Agilidade na resposta, orientação técnica contínua e desburocratização "
     "da relação entre a SST e o RH."),
    ("relogio", "Prazos e normas cumpridos",
     "Documentação entregue dentro do prazo legal e alinhada às Normas "
     "Regulamentadoras."),
]

PROCESSO = [
    ("Diagnóstico",
     "Levantamos o que a sua empresa já tem, o que está vencido e o que falta "
     "frente às obrigações legais."),
    ("Proposta",
     "Escopo e investimento definidos por serviço, sem pacote fechado que "
     "cobra o que você não precisa."),
    ("Implantação",
     "Documentos elaborados, exames agendados e eventos do eSocial "
     "regularizados, com cronograma acordado."),
    ("Rotina",
     "Acompanhamento contínuo: vencimentos controlados, revisões nos prazos "
     "e um canal direto com a Ágape."),
]

FAQ_HOME = [
    ("A Ágape atende empresas de qualquer porte e segmento?",
     "Sim. Atendemos empresas de todos os segmentos que precisam cumprir "
     "obrigações de Saúde e Segurança do Trabalho, do escritório com poucos "
     "colaboradores à indústria com múltiplos turnos. O escopo é dimensionado "
     "conforme o grau de risco e o número de colaboradores."),
    ("Minha empresa fica fora de Mogi das Cruzes. Vocês atendem?",
     "Sim. A Ágape atua em todo o Brasil, com atendimento na matriz, na "
     "empresa cliente ou por rede credenciada nas demais praças."),
    ("O que a empresa precisa ter para estar em dia com a SST?",
     "Em linhas gerais: PGR atualizado (NR-1), PCMSO com médico coordenador "
     "(NR-7), exames ocupacionais em dia, treinamentos das NRs aplicáveis e "
     "os eventos de SST enviados ao eSocial. O diagnóstico inicial da Ágape "
     "aponta exatamente o que falta na sua operação."),
    ("Vocês assumem uma empresa que já está com documentação vencida?",
     "Sim. Levantamos o passivo, priorizamos o que gera risco imediato de "
     "autuação e montamos um plano de regularização antes de assumir a rotina."),
    ("Como funciona o orçamento?",
     "Pelo formulário desta página. Retornamos com um escopo por serviço, "
     "sem compromisso. Também é possível falar direto pelo WhatsApp, mas o "
     "formulário garante que o time comercial receba os dados completos."),
]

# ============================================================================
# OS 6 SERVIÇOS (seção 4 do CLAUDE.md)
# Todos com a MESMA estrutura de blocos — muda só o conteúdo.
# ============================================================================
SERVICOS = [

    # ----------------------------------------------------------------- 1
    {
        "chave": "medicina",
        "nome": "Medicina Ocupacional",
        "icone": "estetoscopio",
        "resumo": "Exames admissionais, periódicos e demissionais, ASO e PCMSO "
                  "conduzido por médico do trabalho responsável.",
        "title": "Medicina Ocupacional para Empresas | Ágape SST",
        "meta": "Exames ocupacionais, ASO e PCMSO para empresas. Médico do "
                "trabalho responsável, agenda organizada e integração com o "
                "eSocial. Atendimento em todo o Brasil.",
        "h1": "Medicina Ocupacional para empresas",
        "lead": "Do exame admissional ao demissional, com PCMSO conduzido por "
                "médico do trabalho responsável e ASO emitido no prazo.",
        "img_topo": ("Foto do serviço",
                     "Atendimento médico ocupacional — sala de exame ou "
                     "audiometria.",
                     "Médico do trabalho da Ágape realizando exame ocupacional"),
        "intro_titulo": "Saúde do trabalhador sob controle, do primeiro exame ao desligamento",
        "intro_paragrafos": [
            "A Medicina Ocupacional é a frente que garante que cada colaborador "
            "esteja apto para a função que exerce — e que a empresa consiga "
            "comprovar isso. Na Ágape, o PCMSO é conduzido por médico do trabalho "
            "responsável, alinhado aos riscos identificados no PGR, e os exames "
            "são organizados para não parar a operação.",
            "O atendimento acontece na matriz em Mogi das Cruzes, na rede "
            "credenciada em outras praças ou dentro da sua empresa, conforme o "
            "volume e a distribuição das equipes.",
        ],
        "intro_bullets": [
            "Exame admissional, periódico, de retorno ao trabalho, mudança de "
            "risco ocupacional e demissional",
            "Emissão do ASO — Atestado de Saúde Ocupacional",
            "PCMSO elaborado e assinado por médico do trabalho, conforme a NR-7",
            "Todos os exames complementares exigidos pela legislação",
            "Palestras, campanhas de saúde e ações preventivas alinhadas à "
            "realidade de cada empresa",
            "Atendimento na matriz, in company ou por clínicas credenciadas em "
            "todo o Brasil",
            "Integração com o eSocial: evento S-2220 gerado a partir do próprio ASO",
        ],
        "entregaveis": [
            ("PCMSO", "Programa de Controle Médico de Saúde Ocupacional elaborado "
                      "a partir dos riscos do seu PGR, com médico coordenador "
                      "identificado."),
            ("Exames ocupacionais", "Admissional, periódico, retorno ao trabalho, "
                                    "mudança de risco e demissional, com agenda "
                                    "organizada por unidade e turno."),
            ("Exames complementares", "Audiometria, espirometria, acuidade visual, "
                                      "exames laboratoriais e demais avaliações "
                                      "indicadas pelo risco da função."),
            ("ASO", "Atestado de Saúde Ocupacional emitido no atendimento, com via "
                    "para a empresa e para o colaborador."),
            ("Relatório anual", "Análise do período, indicadores de saúde do grupo "
                                "e plano de ação para o ano seguinte."),
            ("Palestras e campanhas", "Palestras, campanhas de saúde e ações "
                                      "preventivas desenhadas para a realidade "
                                      "da sua operação."),
        ],
        "porque": [
            ("Médico do trabalho responsável",
             "O PCMSO não é documento genérico: tem coordenador identificado, que "
             "responde tecnicamente pelo programa."),
            ("Agenda que respeita a operação",
             "Exames organizados por lote, unidade e turno, reduzindo o tempo de "
             "afastamento do posto de trabalho."),
            ("Documentação pronta para fiscalização",
             "ASO, prontuários e relatórios arquivados e recuperáveis quando a "
             "fiscalização ou o jurídico solicitar."),
        ],
        "faq": [
            ("Com que frequência o exame periódico precisa ser feito?",
             "Depende do risco da função e da faixa etária do trabalhador. O PCMSO "
             "da sua empresa fixa o intervalo de cada função, dentro do que a NR-7 "
             "determina. [REDAÇÃO A VALIDAR com o responsável técnico]"),
            ("A Ágape atende fora de Mogi das Cruzes?",
             "Sim. Atendemos em todo o Brasil, por rede credenciada, além do "
             "atendimento na matriz e dentro da empresa cliente."),
            ("O ASO substitui o envio ao eSocial?",
             "Não. O ASO é o documento do exame; o eSocial exige o evento S-2220 "
             "correspondente. Na Ágape, o envio parte do próprio atendimento."),
            ("Quem responde tecnicamente pelo PCMSO?",
             "Um médico do trabalho coordenador, identificado no programa e "
             "responsável pelas condutas adotadas."),
        ],
    },

    # ----------------------------------------------------------------- 2
    {
        "chave": "seguranca",
        "nome": "Segurança do Trabalho",
        "icone": "capacete",
        "resumo": "PGR, GRO, laudos técnicos e gestão de riscos elaborados por "
                  "profissionais habilitados.",
        "title": "Segurança do Trabalho para Empresas | Ágape SST",
        "meta": "PGR, GRO, LTCAT, laudos de insalubridade e periculosidade e "
                "análise ergonômica. Levantamento em campo e plano de ação com "
                "prazo e responsável.",
        "h1": "Segurança do Trabalho para empresas",
        "lead": "Identificar, avaliar e controlar os riscos da sua operação — com "
                "o PGR e os laudos que a fiscalização e o jurídico vão pedir.",
        "img_topo": ("Foto do serviço",
                     "Técnico de segurança em levantamento de campo dentro de "
                     "uma planta industrial.",
                     "Técnico de segurança do trabalho da Ágape avaliando riscos "
                     "em ambiente industrial"),
        "intro_titulo": "Do inventário de riscos ao plano de ação que sai do papel",
        "intro_paragrafos": [
            "Com a NR-1, a obrigação deixou de ser apenas manter um documento: é "
            "preciso gerenciar riscos. A Ágape faz o levantamento em campo, monta "
            "o inventário de riscos, avalia as exposições e entrega o PGR com "
            "plano de ação priorizado — com prazos, responsáveis e acompanhamento.",
            "Os laudos técnicos são elaborados por profissionais legalmente "
            "habilitados, para que tenham validade jurídica em fiscalização, "
            "perícia e processo trabalhista.",
        ],
        "intro_bullets": [
            "PGR e GRO conforme a NR-1, com inventário de riscos e plano de ação",
            "LTCAT para fins previdenciários e subsídio ao PPP",
            "Laudos de insalubridade (NR-15) e de periculosidade (NR-16)",
            "AET — Análise Ergonômica do Trabalho (NR-17)",
            "Avaliações quantitativas de ruído, calor e agentes químicos e biológicos",
        ],
        "entregaveis": [
            ("PGR", "Programa de Gerenciamento de Riscos com inventário, avaliação "
                    "e plano de ação, revisado nos prazos da NR-1."),
            ("LTCAT", "Laudo Técnico das Condições Ambientais do Trabalho, base "
                      "para aposentadoria especial e para o PPP."),
            ("Insalubridade e periculosidade", "Laudos com fundamentação técnica "
                                               "para decisão sobre adicional e "
                                               "para defesa trabalhista."),
            ("Ergonomia (AET)", "Análise Ergonômica do Trabalho com recomendações "
                                "aplicáveis ao posto e ao processo."),
            ("Avaliações quantitativas", "Medições de ruído, calor, poeiras, "
                                         "vapores e agentes biológicos com "
                                         "instrumentos calibrados."),
            ("Apoio a CIPA e SESMT", "Suporte na constituição, no dimensionamento "
                                     "e na condução dos trabalhos previstos nas "
                                     "NR-4 e NR-5."),
        ],
        "porque": [
            ("Levantamento em campo, não por telefone",
             "Técnico presente na sua planta: risco que não é visto não é gerenciado."),
            ("Laudo que sustenta perícia",
             "Fundamentação técnica e responsável habilitado — documento feito "
             "para ser questionado e resistir."),
            ("Plano de ação com dono e prazo",
             "O PGR já é entregue com responsáveis e datas, pronto para virar "
             "rotina de gestão."),
        ],
        "faq": [
            ("O PPRA ainda existe?",
             "Não. O PPRA foi substituído pelo PGR, dentro do Gerenciamento de "
             "Riscos Ocupacionais (GRO) da NR-1. Empresas que ainda mantêm apenas "
             "o PPRA estão com documentação desatualizada."),
            ("De quanto em quanto tempo o PGR precisa ser revisado?",
             "A NR-1 estabelece revisão periódica e, além dela, revisão sempre que "
             "houver mudança de processo, acidente ou identificação de "
             "inadequação. [PERIODICIDADE A CONFIRMAR na redação final]"),
            ("Empresas pequenas também precisam de PGR?",
             "O enquadramento varia conforme porte e grau de risco, e há formatos "
             "simplificados previstos na norma. A Ágape avalia o enquadramento "
             "antes de propor o escopo."),
            ("O laudo tem validade jurídica?",
             "Sim, quando elaborado e assinado por profissional legalmente "
             "habilitado — que é o padrão de entrega da Ágape."),
        ],
    },

    # ----------------------------------------------------------------- 3
    {
        "chave": "esocial",
        "nome": "eSocial SST",
        "icone": "sistema",
        "resumo": "Envio e monitoramento dos eventos S-2210, S-2220 e S-2240, "
                  "com tratamento de pendências.",
        "title": "eSocial SST para Empresas | Ágape SST",
        "meta": "Envio dos eventos de SST ao eSocial: S-2210 (CAT), S-2220 (ASO) "
                "e S-2240 (agentes nocivos). Prazos monitorados e inconsistências "
                "tratadas.",
        "h1": "eSocial SST para empresas",
        "lead": "Seus eventos de SST enviados ao eSocial no prazo, com "
                "acompanhamento dos retornos e correção de pendências.",
        "img_topo": ("Foto do serviço",
                     "Profissional acompanhando envios e retornos do eSocial em "
                     "tela de sistema.",
                     "Analista da Ágape monitorando o envio de eventos de SST ao "
                     "eSocial"),
        "intro_titulo": "O evento certo, no prazo certo — antes que vire autuação",
        "intro_paragrafos": [
            "Os eventos de SST do eSocial não perdoam atraso. A Ágape assume o "
            "envio, acompanha o retorno do ambiente nacional e trata as "
            "ocorrências antes que se transformem em multa.",
            "Como a Ágape também produz os documentos de origem — ASO, PGR, LTCAT "
            "— o dado enviado nasce consistente. Não é digitação de informação "
            "produzida por terceiro.",
        ],
        "intro_bullets": [
            "S-2210 — Comunicação de Acidente de Trabalho (CAT)",
            "S-2220 — Monitoramento da Saúde do Trabalhador (ASO)",
            "S-2240 — Condições Ambientais do Trabalho e agentes nocivos",
            "Acompanhamento dos retornos e tratamento de inconsistências",
            "Relatório periódico de conformidade para o RH",
        ],
        "entregaveis": [
            ("Envio dos eventos", "S-2210, S-2220 e S-2240 transmitidos a partir "
                                  "dos documentos que a própria Ágape emite."),
            ("Monitoramento de prazos", "Controle de vencimentos por evento e por "
                                        "colaborador, com alerta antes do prazo "
                                        "vencer."),
            ("Tratamento de rejeições", "Análise do retorno do eSocial, correção e "
                                        "reenvio, sem o RH precisar interpretar "
                                        "código de erro."),
            ("Retificação e exclusão", "Ajuste de eventos já transmitidos quando "
                                       "há correção de dado ou desligamento."),
            ("Relatório de conformidade", "Panorama do que foi enviado, do que "
                                          "está pendente e do que depende de ação "
                                          "do RH."),
            ("Apoio em fiscalização", "Recuperação do histórico transmitido e dos "
                                      "documentos de origem quando solicitado."),
        ],
        "porque": [
            ("O dado nasce na própria Ágape",
             "Exame, laudo e evento saem da mesma casa — sem retrabalho de "
             "digitação e sem divergência entre documento e transmissão."),
            ("Prazo monitorado, não lembrado",
             "O controle de vencimento é rotina do processo, não depende de "
             "alguém lembrar."),
            ("Passivo tratado antes da rotina",
             "Diagnóstico do que ficou para trás e plano de regularização antes "
             "de assumir o dia a dia."),
        ],
        "faq": [
            ("Qual o prazo do S-2210?",
             "A CAT tem prazo legal curto, contado a partir do acidente, com regra "
             "específica em caso de óbito. A Ágape trata o evento como "
             "prioritário. [PRAZO EXATO A CONFIRMAR na redação final]"),
            ("Quem é responsável pelo envio: a empresa ou o prestador?",
             "A obrigação legal é do empregador. A Ágape executa o envio como "
             "prestadora e entrega relatório de tudo que foi transmitido, para "
             "que a empresa mantenha o controle."),
            ("Já temos sistema de folha. Isso conflita?",
             "Não. Os eventos de SST são independentes dos eventos de folha. "
             "Alinhamos com o seu sistema para evitar duplicidade. "
             "[INTEGRAÇÕES SUPORTADAS A CONFIRMAR]"),
            ("E os eventos atrasados de antes da contratação?",
             "Fazemos o diagnóstico do passivo e um plano de regularização antes "
             "de assumir a rotina de envio."),
        ],
    },

    # ----------------------------------------------------------------- 4
    {
        "chave": "treinamentos",
        "nome": "Treinamentos NR’s",
        "icone": "formacao",
        "resumo": "Treinamentos normativos com instrutor qualificado, certificado "
                  "e controle de reciclagem.",
        "title": "Treinamentos NRs para Empresas | Ágape SST",
        "meta": "Treinamentos das Normas Regulamentadoras: NR-35, NR-33, NR-10, "
                "NR-12, NR-5 e outras. Na sua empresa ou na Ágape, com "
                "certificado e controle de validade.",
        "h1": "Treinamentos das NRs para empresas",
        "lead": "Treinamentos normativos conduzidos por instrutores qualificados, "
                "com registro, certificado e controle de reciclagem.",
        "img_topo": ("Foto do serviço",
                     "Turma em treinamento normativo — sala ou prática de campo "
                     "(ex.: trabalho em altura).",
                     "Turma de colaboradores em treinamento de norma "
                     "regulamentadora conduzido pela Ágape"),
        "intro_titulo": "Treinamento que cumpre a norma e que o time realmente usa",
        "intro_paragrafos": [
            "Treinamento de NR não é palestra: a norma define carga horária, "
            "conteúdo programático, qualificação do instrutor e registro. A Ágape "
            "entrega tudo isso — e ainda controla quando cada turma vence, para a "
            "empresa não descobrir o vencimento durante uma fiscalização.",
            "Realizamos os treinamentos previstos nas Normas Regulamentadoras, da "
            "NR-1 à NR-35, com abordagem clara e aplicada à realidade da empresa. "
            "As turmas podem acontecer na sua planta, na estrutura da Ágape ou em "
            "formato híbrido, quando a norma permite.",
        ],
        "intro_bullets": [
            "Treinamentos da NR-1 à NR-35, conforme o risco da operação",
            "Turmas na sua empresa, na Ágape ou em formato híbrido, quando a NR permite",
            "Instrutor qualificado e conteúdo programático conforme cada norma",
            "Lista de presença, avaliação e certificado por participante",
            "Controle de validade e convocação para reciclagem",
        ],
        "entregaveis": [
            ("NR-35 — Trabalho em altura", "Formação e reciclagem para atividades "
                                           "acima de dois metros, com parte prática."),
            ("NR-33 — Espaço confinado", "Capacitação de trabalhador autorizado, "
                                         "vigia e supervisor de entrada."),
            ("NR-5 — CIPA", "Treinamento de membros eleitos e designados, na "
                            "constituição e na renovação da comissão."),
            ("Primeiros Socorros", "Capacitação da equipe para o primeiro "
                                   "atendimento dentro da empresa."),
            ("Brigada de Incêndio e AVCB", "Formação de brigada e apoio às "
                                           "exigências do Auto de Vistoria do "
                                           "Corpo de Bombeiros."),
            ("SIPAT e campanhas", "Organização da Semana Interna de Prevenção de "
                                  "Acidentes e capacitações específicas conforme "
                                  "a necessidade operacional."),
        ],
        "porque": [
            ("Instrutor qualificado e comprovado",
             "Cada norma exige um perfil específico de instrutor. A comprovação "
             "acompanha o certificado."),
            ("Turma sem parar a operação",
             "Horários e turnos combinados com a produção, inclusive fora do "
             "horário comercial."),
            ("Reciclagem antes do vencimento",
             "Controlamos a validade de cada certificado e avisamos antes de "
             "virar não conformidade."),
        ],
        "faq": [
            ("O treinamento pode ser feito a distância?",
             "Depende da norma. Algumas admitem formato a distância ou "
             "semipresencial dentro de limites definidos; outras exigem parte "
             "prática presencial. Avaliamos norma a norma antes de propor o formato."),
            ("Qual a validade dos certificados?",
             "Varia conforme a norma. Ao final de cada turma entregamos um quadro "
             "com a validade de cada treinamento realizado."),
            ("Vocês treinam dentro da nossa planta?",
             "Sim, inclusive a parte prática, quando a estrutura do local permite."),
            ("O certificado é aceito em fiscalização?",
             "Sim: certificado com conteúdo, carga horária, data e identificação "
             "do instrutor, com lista de presença arquivada."),
        ],
    },

    # ----------------------------------------------------------------- 5
    {
        "chave": "ambulatorio",
        "nome": "Gestão de Ambulatório",
        "icone": "predio",
        "resumo": "Equipe, protocolos e indicadores do ambulatório dentro da sua "
                  "empresa, sob gestão da Ágape.",
        "title": "Gestão de Ambulatório para Empresas | Ágape SST",
        "meta": "Terceirização e gestão do ambulatório dentro da sua empresa: "
                "equipe dimensionada, cobertura de escala, protocolos e "
                "indicadores mensais.",
        "h1": "Gestão de Ambulatório dentro da sua empresa",
        "lead": "A Ágape assume a operação do ambulatório na sua planta: equipe, "
                "protocolos, insumos e indicadores.",
        "img_topo": ("Foto do serviço",
                     "Ambulatório dentro de empresa cliente — sala de "
                     "atendimento com equipe de enfermagem.",
                     "Equipe de enfermagem do trabalho em ambulatório dentro de "
                     "empresa cliente da Ágape"),
        "intro_titulo": "Ambulatório dentro da empresa, operado por quem faz SST",
        "intro_paragrafos": [
            "Atuamos na gestão de ambulatórios ocupacionais para empresas que "
            "necessitam de um SESMT próprio, estruturando e administrando a gestão "
            "de saúde corporativa de forma integrada. A Ágape assume a operação — "
            "seleção e gestão da equipe, protocolos assistenciais, controle de "
            "insumos e indicadores mensais.",
            "Esse modelo já é aplicado em empresas como Elgin, Fame, Rinnai e "
            "Vipol, com foco em eficiência operacional, padronização de processos "
            "e segurança técnica, sustentado por mais de duas décadas de "
            "experiência.",
        ],
        "intro_bullets": [
            "Dimensionamento da equipe conforme efetivo, turnos e risco",
            "Cobertura de escala, férias e afastamentos sem lacuna de atendimento",
            "Protocolos de atendimento e de emergência escritos e treinados",
            "Gestão de insumos, materiais e validade de medicamentos",
            "Indicadores mensais de atendimento, absenteísmo e retorno ao trabalho",
        ],
        "entregaveis": [
            ("Equipe dedicada", "Técnicos de enfermagem, enfermeiro do trabalho e "
                                "médico do trabalho conforme o dimensionamento "
                                "acordado."),
            ("Gestão de escala", "Cobertura de turnos, férias e faltas sob "
                                 "responsabilidade da Ágape, não do seu RH."),
            ("Protocolos assistenciais", "Condutas padronizadas para primeiro "
                                         "atendimento, emergência e encaminhamento."),
            ("Controle de insumos", "Reposição, validade e rastreio de materiais e "
                                    "medicamentos do ambulatório."),
            ("Integração com o PCMSO", "Exames, restrições e retorno ao trabalho "
                                       "tratados dentro do mesmo programa."),
            ("Indicadores mensais", "Relatório de atendimentos, absenteísmo, "
                                    "acidentes e tendências para a gestão."),
        ],
        "porque": [
            ("Uma responsável só",
             "Ambulatório, PCMSO, PGR e eSocial na mesma casa: sem empurra-empurra "
             "entre fornecedores."),
            ("Escala é problema nosso",
             "Falta, férias e desligamento de profissional são cobertos pela Ágape."),
            ("Gestão por indicador",
             "Relatório mensal que mostra onde o adoecimento e o afastamento "
             "estão concentrados."),
        ],
        "faq": [
            ("A partir de quantos colaboradores compensa?",
             "Depende mais do risco e da distribuição de turnos do que do número "
             "puro. Fazemos o dimensionamento antes de propor. "
             "[CRITÉRIO A VALIDAR com o cliente]"),
            ("A equipe é contratada pela Ágape?",
             "Sim. A gestão do vínculo, da escala e das substituições fica com a "
             "Ágape."),
            ("Funciona em mais de uma unidade?",
             "Sim, com padronização de protocolo e de indicadores entre as unidades."),
            ("E o ambulatório que já existe hoje?",
             "Assumimos a operação existente, com diagnóstico inicial de "
             "estrutura, equipe e protocolos."),
        ],
    },

    # ----------------------------------------------------------------- 6
    {
        "chave": "clinica",
        "nome": "Clínica Credenciada",
        "icone": "rede",
        "resumo": "Rede credenciada para atender suas unidades em todo o Brasil, "
                  "com padrão único de documentação.",
        "title": "Clínica Credenciada | Rede Ágape SST",
        "meta": "Rede de clínicas credenciadas para atender as unidades da sua "
                "empresa em todo o Brasil, com padrão único de documento, agenda "
                "e faturamento.",
        "h1": "Clínica Credenciada",
        "lead": "Cobertura nacional através de clínicas credenciadas, com o mesmo "
                "padrão de atendimento e de documentação da matriz.",
        "img_topo": ("Foto do serviço",
                     "Recepção de clínica credenciada ou mapa de cobertura "
                     "nacional.",
                     "Recepção de clínica da rede credenciada Ágape"),
        "nota_escopo": "O portfólio do cliente confirma o uso da rede credenciada "
                       "para atender empresas em todo o Brasil — esse é o público "
                       "principal da página, e a estrutura abaixo já reflete isso. "
                       "FALTA DEFINIR se a página também deve captar CLÍNICAS que "
                       "queiram se credenciar. Se não for o caso, os trechos "
                       "voltados a clínicas saem e a página encolhe.",
        "intro_titulo": "Uma rede para atender onde a sua empresa estiver",
        "intro_paragrafos": [
            "Empresas com filiais, obras ou equipes espalhadas não podem depender "
            "de um único endereço. A Ágape mantém rede credenciada para realizar "
            "exames e atendimentos em outras praças, mantendo padronização de "
            "documento, prazo e prontuário.",
            "Para as clínicas, o credenciamento é a porta de entrada na rede: "
            "demanda das empresas atendidas pela Ágape, padrão de documentação "
            "definido e fluxo de faturamento organizado.",
        ],
        "intro_bullets": [
            "Atendimento em outras praças sem trocar de fornecedor de SST",
            "Padronização de ASO, prontuário e prazo em toda a rede",
            "Agendamento e faturamento centralizados na Ágape",
            "Um único ponto de contato para todas as unidades",
            "Para clínicas: entrada na rede com demanda já existente",
        ],
        "entregaveis": [
            ("Cobertura nacional", "Atendimento das suas unidades por clínicas "
                                   "credenciadas, com o padrão Ágape de "
                                   "documentação."),
            ("Agenda centralizada", "Solicitação, agendamento e acompanhamento por "
                                    "um único canal, mesmo com várias praças."),
            ("Padrão de documento", "ASO, exames complementares e prontuário no "
                                    "mesmo formato em toda a rede."),
            ("Faturamento unificado", "Uma cobrança consolidada, em vez de contrato "
                                      "com cada clínica local."),
            ("Credenciamento de clínicas", "Processo de entrada na rede, com "
                                           "critérios técnicos e de estrutura "
                                           "definidos. [CRITÉRIOS A LEVANTAR]"),
            ("Acompanhamento de qualidade", "Monitoramento do padrão de atendimento "
                                            "das credenciadas. [ESCOPO A CONFIRMAR]"),
        ],
        "porque": [
            ("Um contrato, várias praças",
             "A sua empresa negocia com a Ágape; a Ágape responde pela rede."),
            ("Mesmo padrão em todo lugar",
             "O documento que chega de outra cidade tem o mesmo formato do da matriz."),
            ("Sem retrabalho para o RH",
             "Agendamento e cobrança concentrados, sem seu time gerenciando "
             "clínica por clínica."),
        ],
        "faq": [
            ("Em quais cidades a rede atende?",
             "[LISTA DE PRAÇAS A LEVANTAR com o cliente. Hoje a comunicação "
             "informa apenas atendimento em todo o Brasil.]"),
            ("Como uma clínica se credencia?",
             "Pelo formulário desta página. A Ágape avalia estrutura, habilitação "
             "e capacidade de atendimento antes de concluir o credenciamento. "
             "[FLUXO A CONFIRMAR]"),
            ("O padrão de documento muda de cidade para cidade?",
             "Não. O modelo de ASO e o fluxo de envio ao eSocial são os mesmos em "
             "toda a rede."),
            ("Quem responde tecnicamente pelo atendimento na credenciada?",
             "A responsabilidade técnica local é da clínica credenciada, dentro do "
             "padrão e da coordenação definidos pela Ágape. "
             "[REDAÇÃO A VALIDAR com o responsável técnico]"),
        ],
    },
]

SERVICOS_POR_CHAVE = {s["chave"]: s for s in SERVICOS}

# ============================================================================
# SOBRE NÓS
# ============================================================================
SOBRE = {
    "title": "Sobre a Ágape | 25 anos em Saúde e Segurança do Trabalho",
    "meta": "Fundada em 1999 em Mogi das Cruzes-SP, a Ágape atua em todo o Brasil "
            "com Medicina Ocupacional, Segurança do Trabalho, Treinamentos e "
            "eSocial.",
    "h1": "Mais de 25 anos descomplicando a Saúde e Segurança do Trabalho",
    "lead": "A Ágape nasceu em 1999, em Mogi das Cruzes-SP, e hoje atende empresas "
            "de todos os segmentos em todo o Brasil.",
    "historia_titulo": "Uma trajetória pautada por responsabilidade técnica",
    "historia": [
        "Atuamos há 25 anos no mercado de Saúde e Segurança do Trabalho. Nossa "
        "sede foi fundada em 1999, em Mogi das Cruzes, onde iniciamos uma "
        "trajetória pautada por responsabilidade técnica e compromisso com a "
        "gestão corporativa.",
        "Atualmente, mais de 300 empresas e aproximadamente 20.000 vidas estão "
        "sob o nosso cuidado, refletindo a confiança construída ao longo de mais "
        "de duas décadas.",
        "Nesse período acompanhamos a evolução da legislação brasileira de SST — "
        "da consolidação das Normas Regulamentadoras à chegada do eSocial e à "
        "substituição do PPRA pelo PGR. Em cada mudança, o trabalho foi o mesmo: "
        "traduzir a obrigação legal em rotina possível dentro da empresa cliente.",
        "[PARÁGRAFO OPCIONAL A COMPLETAR: marcos da empresa, mudança de sede, "
        "certificações. Levantar com o cliente.]",
    ],
    "consultoria_titulo": "Consultoria personalizada",
    "consultoria": [
        "Oferecemos um modelo de consultoria personalizada, desenvolvendo "
        "soluções sob medida conforme a realidade, o porte e as necessidades de "
        "cada empresa.",
        "Nosso modelo é preventivo, próximo e acessível, combinando agilidade na "
        "resposta, orientação técnica contínua e desburocratização da relação "
        "entre a Saúde e Segurança do Trabalho e o RH.",
    ],
    "pericias_titulo": "Perícias Médicas",
    "pericias": [
        "Em casos de processos trabalhistas, a Ágape conta com um setor "
        "especializado em Perícias Médicas, preparado para atuar de forma "
        "técnica, ética e criteriosa. Essa área faz parte da nossa estrutura há "
        "mais de duas décadas, oferecendo suporte qualificado em demandas "
        "judiciais e administrativas.",
    ],
    "pericias_nota": "DECISÃO DE ARQUITETURA PENDENTE. Perícias Médicas aparece no "
                     "portfólio como frente consolidada, mas não está entre os 6 "
                     "serviços definidos no escopo do site. Por ora entra aqui, "
                     "como parte da estrutura da empresa. Definir: vira a 7ª "
                     "página de serviço (slug novo), vira bloco dentro de "
                     "Segurança do Trabalho, ou fica só nesta menção?",
    "esporte_titulo": "Apoio ao esporte",
    "esporte": "O Suzano Vôlei é um dos clubes mais tradicionais do voleibol "
               "brasileiro. Apoiamos o Suzano com o nosso serviço médico, "
               "reconhecendo trajetórias de excelência que refletem os mesmos "
               "valores que orientam a nossa atuação corporativa.",
    "valores": [
        ("escudo", "Conformidade",
         "Documento tecnicamente correto, assinado por profissional habilitado e "
         "pronto para ser questionado."),
        ("coracao", "Atendimento humanizado",
         "Linguagem clara com o RH e respeito com o colaborador que passa pelo "
         "atendimento."),
        ("relogio", "Prazo",
         "Cumprir data acordada é parte do serviço, não um diferencial "
         "extraordinário."),
        ("usuarios", "Equipe multidisciplinar",
         "Medicina, enfermagem, engenharia e segurança do trabalho conversando "
         "entre si."),
    ],
    "valores_nota": "MISSÃO, VISÃO E VALORES: o conjunto acima é uma proposta "
                    "redigida a partir do posicionamento declarado pelo cliente. "
                    "Precisa ser validado ou substituído pelo texto oficial da "
                    "Ágape, se existir.",
    "equipe_titulo": "Equipe multidisciplinar",
    "equipe_texto": "As frentes de saúde e de segurança não funcionam separadas: o "
                    "PCMSO depende do que o PGR identificou, e o eSocial depende "
                    "dos dois. Por isso a Ágape reúne as especialidades na mesma "
                    "estrutura.",
    "equipe": [
        "Médicos do trabalho",
        "Enfermeiros e técnicos de enfermagem do trabalho",
        "Engenheiros de segurança do trabalho",
        "Técnicos de segurança do trabalho",
        "Equipe administrativa e de atendimento",
        "[COMPOSIÇÃO A CONFIRMAR com o cliente]",
    ],
}

# ============================================================================
# SERVIÇOS (página índice)
# ============================================================================
SERVICOS_INDICE = {
    "title": "Serviços de SST para Empresas | Ágape",
    "meta": "Medicina Ocupacional, Segurança do Trabalho, eSocial SST, "
            "Treinamentos NRs, Gestão de Ambulatório e Clínica Credenciada. "
            "Conheça as seis frentes da Ágape.",
    "h1": "Serviços de Saúde e Segurança do Trabalho",
    "lead": "Seis frentes que cobrem a obrigação legal da sua empresa de ponta a "
            "ponta — contratadas juntas ou separadamente.",
}

# ============================================================================
# CONTATO
# ============================================================================
CONTATO_PAGINA = {
    "title": "Contato e Orçamento | Ágape SST",
    "meta": "Solicite um orçamento de Saúde e Segurança do Trabalho ou envie seu "
            "currículo para a Ágape. Mogi das Cruzes-SP, com atendimento em todo "
            "o Brasil.",
    "h1": "Fale com a Ágape",
    "lead": "Escolha abaixo o que você precisa: um orçamento para a sua empresa ou "
            "enviar seu currículo para o nosso time.",
}

# ============================================================================
# POLÍTICA DE PRIVACIDADE / LGPD
# ============================================================================
PRIVACIDADE = {
    "title": "Política de Privacidade | Ágape SST",
    "meta": "Como a Ágape Saúde e Segurança do Trabalho coleta, usa e protege "
            "dados pessoais, conforme a Lei Geral de Proteção de Dados.",
    "h1": "Política de Privacidade",
    "lead": "Como a Ágape trata os dados pessoais coletados neste site e na "
            "prestação dos seus serviços.",
    "aviso": "TEXTO JURÍDICO A VALIDAR. A estrutura abaixo cobre os pontos que a "
             "LGPD exige, mas o conteúdo final precisa de revisão jurídica antes "
             "de publicar. Hoje a Ágape disponibiliza um PDF solto — esta página "
             "substitui o PDF.",
    "secoes": [
        ("Quem é o controlador dos dados",
         ["A Ágape Saúde e Segurança do Trabalho é a controladora dos dados "
          "pessoais coletados neste site, conforme a Lei nº 13.709/2018 (LGPD).",
          "[INCLUIR: razão social completa, CNPJ e canal do encarregado de dados "
          "(DPO). Dados a levantar com o cliente.]"]),
        ("Quais dados coletamos",
         ["Dados informados voluntariamente nos formulários do site: nome, "
          "empresa, telefone, e-mail e serviço de interesse.",
          "No formulário de candidatura: os dados do currículo enviado.",
          "Dados de navegação coletados por cookies, quando autorizados."]),
        ("Para que usamos esses dados",
         ["Responder a solicitações de orçamento e de contato comercial.",
          "Conduzir processos de seleção, no caso de currículos.",
          "Cumprir obrigações legais e regulatórias relacionadas à prestação de "
          "serviços de Saúde e Segurança do Trabalho.",
          "[REVISAR: dados de saúde coletados em exames ocupacionais têm regime "
          "próprio, com base legal distinta. Esta seção precisa de redação "
          "jurídica específica.]"]),
        ("Com quem compartilhamos",
         ["Com prestadores necessários à execução do serviço, como clínicas "
          "credenciadas e sistemas de gestão.",
          "Com órgãos públicos, quando houver obrigação legal — como no envio de "
          "eventos ao eSocial.",
          "Não vendemos dados pessoais."]),
        ("Por quanto tempo guardamos",
         ["Pelo prazo necessário à finalidade da coleta e pelos prazos legais "
          "aplicáveis à documentação de SST.",
          "[DEFINIR prazos de retenção por tipo de dado, com apoio jurídico.]"]),
        ("Seus direitos",
         ["Confirmar a existência de tratamento e acessar seus dados.",
          "Corrigir dados incompletos, inexatos ou desatualizados.",
          "Solicitar anonimização, bloqueio ou eliminação de dados desnecessários.",
          "Revogar consentimento, quando o tratamento se basear nele.",
          "Para exercer esses direitos, entre em contato pelos canais informados "
          "nesta página."]),
        ("Cookies",
         ["Este site utiliza cookies para funcionamento e medição de audiência.",
          "O banner de consentimento permite aceitar ou recusar os cookies não "
          "essenciais.",
          "[NO PROTÓTIPO o banner é apenas visual. No WordPress, será um plugin "
          "de consentimento que registra a escolha do visitante.]"]),
    ],
}
