# Fotos geradas por IA — pasta de entrada

Salve aqui as imagens que o Gemini gerar. **Use exatamente estes nomes de
arquivo** — é assim que o site sabe qual imagem vai em qual lugar.

Formato: JPG ou PNG, mínimo 1400px no lado maior. Não precisa tratar cor nem
redimensionar: o `otimizar_fotos.py` cuida disso (recorta na proporção certa,
reduz o peso e aplica o tratamento do guia — baixa saturação com sobreposição
verde).

| Arquivo | Onde entra | Proporção |
|---|---|---|
| `hero.jpg` | imagem principal da Home | 4:3 |
| `diferenciais.jpg` | "Descomplicamos a SST" (Home) | 4:3 |
| `processo.jpg` | "Do primeiro contato à rotina" (Home) | 4:3 |
| `institucional.jpg` | topo de Sobre Nós | 4:3 |
| `equipe.jpg` | "Equipe multidisciplinar" (Sobre Nós) | 4:3 |
| `esporte.jpg` | apoio ao Suzano Vôlei (Sobre Nós) | 16:9 |
| `servicos.jpg` | topo da página Serviços | 4:3 |
| `medicina.jpg` | Medicina Ocupacional | 4:3 |
| `seguranca.jpg` | Segurança do Trabalho | 4:3 |
| `esocial.jpg` | eSocial SST | 4:3 |
| `treinamentos.jpg` | Treinamentos NRs | 4:3 |
| `ambulatorio.jpg` | Gestão de Ambulatório | 4:3 |
| `clinica.jpg` | Clínica Credenciada | 4:3 |

Não precisa mandar todas de uma vez. O script processa o que encontrar e
mantém a arte vetorial nos lugares que ainda não têm foto — o site nunca fica
com buraco.

## Depois de salvar os arquivos

```
python otimizar_fotos.py
python build.py
```

## O que NÃO gerar

- **Mapa da matriz** (página de Contato): ali vai o Google Maps incorporado,
  não uma imagem.
- **Qualquer coisa com texto, logo ou marca visível.** O Gemini erra texto em
  imagem, e logo inventado num site institucional é problema. Se aparecer
  crachá, uniforme com marca ou placa escrita, gere de novo.
- **Rostos em close identificável.** Foto de pessoa real precisa de
  autorização de uso de imagem; imagem de IA que pareça uma pessoa específica
  cria o mesmo problema. Prefira enquadramentos de trás, de lado, de mãos, ou
  com o rosto parcialmente fora de quadro.
