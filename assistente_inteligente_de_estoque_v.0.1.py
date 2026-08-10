
import tkinter as tk
import io
from tkinter import filedialog

import google.generativeai as genai
import pandas as pd

def montagem_geral_estoque():
    estoque = {}
    while True:
        print(
            """

          Menu de informações:

    1 - Montar estoque de produtos.
    2 - Acrescentar novos produtos ao estoque.
    3 - Se deseja repor produtos ao estoque.
    4 - Dar baixa em produtos do estoque.
    5 - Sair
    """
        )
        try:
            comando_menu_informaçoes = int(input('Digite o numero da informação que deseja acessar: '))
        except ValueError:
            print('Erro: Por favor, digite apenas números!')
            continue

        if comando_menu_informaçoes == 1:
            print('Acessando montagem de estoque...')
            montando_lista = int(input('Digite a quantidade de produtos: '))
            if montando_lista >= 1:
                for lista in range(montando_lista):
                    nome_produto = str(input('Digite o nome do produto: '))
                    quantidade_produto = int(input('Digite a quantidade total do produto: '))
                    estoque[nome_produto] = quantidade_produto

        elif comando_menu_informaçoes == 2:
            print('Acessando acrescimo de produtos ao estoque...')
            acrescimo = str(input('Digite  o nome do produto que deseja acrescentar: '))
            acrescimo_quantidade = int(input('Digite a quantidade: '))
            estoque[acrescimo] = acrescimo_quantidade

        elif comando_menu_informaçoes == 3:
            print('Acessando reposição de estoque...')
            produto_desejado = input('Digite o nome do produto que deseja atualizar: ').strip()

            if produto_desejado in estoque:
                quantidade_reposiçao = int(input(f'Digite quantas unidades do produto {produto_desejado} deseja repor: '))
                estoque[produto_desejado] += quantidade_reposiçao
                print(f'Atualizado!! A nova quantidade de {produto_desejado}: {estoque[produto_desejado]} unidades')
            else:
                print('Erro!!! Produto não encontrado no estoque')

        elif comando_menu_informaçoes == 4:
            print('Acessando baixa em produtos do estoque...')
            baixa_produto = input('Digite o nome do produto que deseja dar baixa: ').strip()

            if baixa_produto in estoque:
                quantidade_baixa = int(input(f'Digite quantas unidades do produto {baixa_produto} deseja dar baixa: '))
                if estoque[baixa_produto] >= quantidade_baixa:
                    estoque[baixa_produto] -= quantidade_baixa
                    print(f'Atualizado!! A nova quantidade de {baixa_produto}: {estoque[baixa_produto]} unidades')
                else:
                    print(f'Erro!!! Não foi possivel realizar a baixa pois no estoque {baixa_produto}, possui {estoque[baixa_produto]} unidades')

        elif comando_menu_informaçoes == 5:
            print('Encerrando sistema...')
            exit()
        else:
            print('Erro,opção invalida!!')
        print(f'Estoque atualizado!!{estoque}')


while True:
    print(
        """  Seja Bem-Vindo ao nosso controle de estoque com AI!!

    Aqui controlamos tudo dentro do nosso estoque com a ajuda da AI!

    Bom, vamos lá...

          Menu de informações:

    1- Carregar um aquivo Excel para acompanhamento com AI.
    2- Montar estoque de produtos.

    """
    )

    try:
        escolha_inicial = int(input('Digite a opção que deseja iniciar: '))
    except ValueError:
        print("Opção inválida. Digite um numero correspondente.")
        continue

    if escolha_inicial == 1:
        root = tk.Tk()
        root.withdraw()

        caminho_arquivo = filedialog.askopenfilename(
          title = "Selecione seu arquivo Excel", filetypes=[('Arquivos Excel', "*.xlsx *.xls")]
        )

        if caminho_arquivo:
            df = pd.read_excel(caminho_arquivo)
            print('Arquivo carregado com sucesso!!')

            converter_para_ai = df.to_string(index = False)
            comando_ia = input('Digite o que deseja que a ia faça em sua planilha: ')

            prompt = (f'Atue como um leitor de dados. Leia esta planilha {converter_para_ai} e faça as modificações de acrescentar produtos a planilha, dar baixa em produtos da planilha, repor produtos da planilha que forem pedidos em {comando_ia} e depois devolva em formato csv somente isso, nenhuma palavra a mais !')

            genai.configure(api_key='GEMINI_KEY')
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(prompt)

            conteudo_limpo = (
                response.text.replace("```csv", "")
                .replace("```", "")
                .strip()
            )

            print(conteudo_limpo)

            gostou_salvar = input('Gostaria de salvar o arquivo? sim ou não')

            if gostou_salvar.lower() == 'sim':
              sobrescrever_novo = input('Gostaria de sobrescrever? ou de um novo arquivo?(sobrescrever/novo)')

              if sobrescrever_novo.lower() == 'sobrescrever':
                print('Sobrescrevendo...')
                df = pd.read_csv(io.StringIO(conteudo_limpo))
                df.to_excel(caminho_arquivo, index = False)

              elif sobrescrever_novo.lower() == 'novo':
                root = tk.Tk()
                root.withdraw()
                diretorio_arquivo = filedialog.asksaveasfilename(
                  title = 'Escolha onde salvar o arquivo Excel',
                  defaultextension=".xlsx",
                  filetypes=[
                  ("Arquivos do Excel", "*.xlsx"),
                  ("Todos os arquivos", "*.*")
                  ],
                )

                if diretorio_arquivo:
                    df = pd.read_csv(io.StringIO(conteudo_limpo))
                    df.to_excel(diretorio_arquivo, index = False)
                    print('Arquivo salvo com sucesso!!!')
                else:
                    print('Operação cancelada!')

            else:
              print('Operação cancelada com sucesso')
        else:
            print('Erro!! arquivo não encontrado. ')

    elif escolha_inicial == 2:
        print('Otimo, você optou por começar o seu estoque, então vamos lá...')
        montagem_geral_estoque()

    else:
        print('Opção invalida!!')
