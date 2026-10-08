import tkinter as tk
import io
from tkinter import filedialog
from tkinter import *
from google import genai
import pandas as pd



def opcoes_de_estoque():
    print('''
        
        Menu de informaçoẽs:

    1 - Montar estoque de produtos
    2 - Acrescentar novos produtos ao estoque
    3 - Repor produtos ao estoque
    4 - Dar baixa em produtos do estoque
    5 - Salvar arquivos em uma planilha
    6 - Sair
        '''
        )

        
    comando_menu_de_informacoes = input('Digite o numero da informação desejada: ').strip()

    if len (comando_menu_de_informacoes) != 1 or not comando_menu_de_informacoes.isdigit():
        print('Erro: Digite apenas um unico numero')
        
    return int(comando_menu_de_informacoes)

def montar_estoque_de_produtos(estoque):
        montando_lista = input ('Digite a quantidade de produtos que deseja no seu estoque.')

        if not montando_lista.isdecimal():
            print('Erro: Digite um número inteiro válido')
            return montando_lista
        
        lista = int(montando_lista)

        if lista >= 1:
            for listagem in range (lista):
                nome_produto = input('Digite o nome do produto:').strip()
                if nome_produto == '' or not all(c.isalpha() or c == ' ' for c in nome_produto):
                    print('Erro: Digite um nome valido (Somente Letras)')
                    continue

                quantidade = input(f'Digite a quantidade de {nome_produto}: ').strip()
            if not quantidade.isdecimal():
                estoque[nome_produto] = int(quantidade)
                print(f'{nome_produto} adicionado com {quantidade} unidades!')
            else:
                print('Erro: Digite uma quantidade inteira válida')
def acrescentar_novos_produtos(estoque):
    acrescimo = input('Digite  o nome do produto que deseja acrescentar: ').strip()
    if acrescimo.replace (" ", "").isalpha():
        acrescimo_quantidade = input('Digite a quantidade: ').strip()

        if acrescimo_quantidade.isdecimal():
            acrescimo_quantidade = int(acrescimo_quantidade)
            estoque[acrescimo] = acrescimo_quantidade
            print('Produto cadastrado com sucesso!!')
        else:
            print('Digite uma quantidade inteira maior do que zero!')
    else:
        print('Digite o nome com letras alfabeticas')
        

def repor_produto(estoque):

    produto_desejado = input('Digite o nome do produto que deseja atualizar: ').strip()
    if produto_desejado in estoque():
        quantidade_reposiçao = input(f'Digite quantas unidades do produto {produto_desejado} deseja repor: ').strip()
        if quantidade_reposiçao.isdecimal():
            quantidade_reposiçao = int(quantidade_reposiçao)
            estoque[produto_desejado] += quantidade_reposiçao
            print(f'Atualizado!! A nova quantidade de {produto_desejado}:' 
                  f'{estoque[produto_desejado]} unidades'
                  )
        else:
            print('Digite um número inteiro maior do que zero')
    else:
        print('Erro!!! Produto não encontrado no estoque')


def dar_baixa(estoque):
    baixa_produto = input('Digite o nome do produto que deseja dar baixa: ').strip()

    if baixa_produto in estoque:
        quantidade_baixa = input(f'Digite quantas unidades do produto {baixa_produto} deseja dar baixa: ').strip()
        if quantidade_baixa.isdecimal():
            quantidade_baixa = int(quantidade_baixa)
            if estoque[baixa_produto] >= quantidade_baixa:
                estoque[baixa_produto] -= quantidade_baixa
                print(f'Atualizado!! A nova quantidade de {baixa_produto}:'
                    f'{estoque[baixa_produto]} unidades'
                    )
            else:
                print(f'Erro!!! Não foi possivel realizar a baixa pois no estoque {baixa_produto},' 
                      f'possui {estoque[baixa_produto]} unidades'
                      )
        else:
            print('Digite um numero inteiro maior do que zero!!')
    else:
        print('O produto não se encontra no estoque!')

def salvar_arquivo(estoque):
    gostou_salvar = input('Gostaria de salvar o arquivo? sim ou não: ').strip().lower()
    if gostou_salvar.lower() == 'sim':
        root = tk.Tk()
        root.withdraw()
        try:
            diretorio_arquivo = filedialog.asksaveasfilename(
                title = 'Escolha onde salvar o arquivo Excel',
                defaultextension=".xlsx",
                filetypes=[
                ("Arquivos do Excel", "*.xlsx"),
                ("Todos os arquivos", "*.*")
                ],
            )
        finally:
            root.destroy()

        if diretorio_arquivo:
            df = pd.DataFrame([estoque])
            df.to_excel(diretorio_arquivo, index = False)
            print('Arquivo salvo com sucesso!!!')
        else:
            print('Operação cancelada!')
    elif gostou_salvar == ('não', 'nao'):
        print('operação cancelada')
    else:
        print('Operação cancelada com sucesso')

def menu_iniciar():
    print(
        """  Seja Bem-Vindo ao nosso controle de estoque com AI!!

    Aqui controlamos tudo dentro do nosso estoque com a ajuda da AI!

    Bom, vamos lá...

          Menu de informações:

    1- Carregar um aquivo Excel para acompanhamento com AI.
    2- Montar estoque de produtos.
    3- Sair.

    """
    )
    escolha_inicial = input ('Digite a opção que deseja inciar: ').strip()
    if escolha_inicial.isdecimal():
        return int(escolha_inicial)
    else:
        print('Digite o número de uma das opções')
        

def assistente_ia():

    root = tk.Tk()
    root.withdraw()

    try:
        caminho_arquivo = filedialog.askopenfilename(
            title = "Selecione seu arquivo Excel", filetypes=[('Arquivos Excel', "*.xlsx *.xls")]
        )
    finally:
        root.destroy()

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

        print('\n __Resposta da Ai___\n')

        print(conteudo_limpo)
    
        return conteudo_limpo,caminho_arquivo
    else:
        print('Operação cancelada')
        return None
    
def salvar_arquivo_ia(conteudo_limpo,caminho_arquivo):

    gostou_salvar = input('Gostaria de salvar o arquivo? sim ou não: ')

    if gostou_salvar.lower() == 'sim':
        sobrescrever_novo = input('Gostaria de sobrescrever? ou de um novo arquivo?(sobrescrever/novo): ')

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

def main():
    estoque = {}

    while True:

        menu = menu_iniciar()

        if menu == 1:
            assistente_ia()

        elif menu == 2:

            while True:

                opcoes = opcoes_de_estoque()

                if opcoes == 1:
                    print('Acessando montagem de estoque...')
                    montar_estoque_de_produtos(estoque)

                elif opcoes == 2:
                    print('Acessando acrescimo de produtos ao estoque...')
                    acrescentar_novos_produtos(estoque)

                elif opcoes == 3:
                    print('Acessando reposição de estoque...')
                    repor_produto(estoque)

                elif opcoes == 4:
                    print('Acessando o menu de baixa em produtos do estoque...')
                    dar_baixa(estoque)

                elif opcoes == 5:
                    print('Acessando menu de salvamento...')
                    salvar_arquivo(estoque)

                elif opcoes == 6:
                    print('Encerrando...')
                    break
                else:
                    print('Opção invalida...')
        elif menu == 3:
            print('Encerrando... o programa!')
            break

if __name__ == "__main__":
    main()