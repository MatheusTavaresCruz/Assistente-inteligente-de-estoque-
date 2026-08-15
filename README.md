# Assistente Inteligente de Estoque

Sistema de controle de estoque em Python, criado para resolver um problema real: substituir o controle manual (papel e caneta) de entrada e saída de produtos de uma geladeira de autoatendimento por um sistema com registro e relatórios automatizados, com apoio de IA (Gemini) para atualizar planilhas por comando em linguagem natural.

## Funcionalidades

O sistema oferece dois fluxos principais, via menu no terminal:

**1. Montar estoque do zero**
- Cadastrar produtos e quantidades iniciais
- Acrescentar novos produtos
- Repor quantidade de um produto existente
- Dar baixa (registrar saída) de um produto
- Salvar o estoque em uma planilha Excel

**2. Carregar planilha existente e editar com IA**
- Selecionar um arquivo Excel (`.xlsx`/`.xls`) já existente
- Descrever em linguagem natural o que deseja fazer (ex: "adicione 10 unidades de refrigerante e dê baixa em 3 chocolates")
- O Gemini interpreta o comando, aplica as alterações e devolve os dados atualizados
- Escolher entre sobrescrever o arquivo original ou salvar como um novo

## Tecnologias

- Python
- Pandas (leitura/escrita de planilhas Excel)
- Tkinter (seleção e salvamento de arquivos)
- Google Generative AI (Gemini)

## Pré-requisitos

- Python 3.10+
- Uma chave de API do [Google AI Studio](https://aistudio.google.com/app/apikey)

## Instalação

```bash
git clone https://github.com/MatheusTavaresCruz/Assistente-inteligente-de-estoque-.git
cd Assistente-inteligente-de-estoque-
pip install pandas google-generativeai
```

## Configuração

Defina sua chave de API como variável de ambiente em vez de deixá-la fixa no código:

```bash
export GEMINI_API_KEY="sua_chave_aqui"
```

E no script, carregue-a com:

```python
import os
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
```

## Uso

```bash
python assistente_inteligente_de_estoque_v.0.3.py
```

1. Escolha `1` para carregar uma planilha existente e editar com IA, ou `2` para montar um estoque novo pelo menu.
2. Siga as instruções exibidas no terminal.

## Versões

O repositório mantém o histórico de evolução do protótipo, da ideia inicial até a versão atual:

| Arquivo | Descrição |
|---|---|
| `estoque_trabalho_v.0.0.py` | Primeiro rascunho |
| `estoque_trabalho_v.0.0.1.py` | Ajustes iniciais |
| `assistente_inteligente_de_estoque_v.0.1.py` | Primeira versão com IA |
| `assistente_inteligente_de_estoque_v.0.2.py` | Iteração intermediária |
| `assistente_inteligente_de_estoque_v.0.3.py` | Versão mais recente |

## Melhorias futuras

- [ ] Interface gráfica (PySide6)
- [ ] Persistência em banco de dados em vez de Excel
- [ ] Validação e tratamento de erros mais robustos
- [ ] Testes automatizados

## Autor

**Matheus Tavares Cruz**
[GitHub](https://github.com/MatheusTavaresCruz)
