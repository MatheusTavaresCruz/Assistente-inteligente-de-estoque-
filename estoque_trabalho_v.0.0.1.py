import google.generativeai as genai
import pandas as pd
import io

<<<<<<< HEAD
genai.configure(api_key='GEMINI_KEY')
=======
genai.configure(api_key='GEMINAI_KEY')
>>>>>>> 2483304 (Retirei os pips do codigo)
model = genai.GenerativeModel('gemini-2.5-flash')



estoque = {}

print("""

    Seja Bem-Vindo ao nosso controle de estoque com AI!!

Aqui controlamos tudo dentro do nosso estoque com a ajuda da AI!

Bom, vamos ao primeiro passo...

      Menu de informações:

1 - Montar estoque de produtos.
2 - Acrescentar produtos ao estoque.
3 - Se deseja repor produtos ao estoque.
4 - Dar baixa em produtos do estoque.
5 - Sair
""")

comando_menu_informaçoes = int(input('Digite o numero da informação que deseja acessar: '))

if comando_menu_informaçoes == 1:
  print('Acessando montagem de estoque...')
  montando_lista = int(input('Digite a quantidade de produtos: '))
  if montando_lista >= 1:
        for lista in range (montando_lista):
            nome_produto = str(input('Digite o nome do produto: '))
            quantidade_produto = int(input('Digite a quantidade total do produto: '))
            estoque [nome_produto] = quantidade_produto
            prompt = (f'Atue como um organizador de dados. Pegue esta lista de dados: {estoque},organize em colunas de "produto", "quantidade" e me devolva estritamente em formato csv,sem nenhuma palavra a mais.')

elif comando_menu_informaçoes == 2:
  print('Acessando acrescimo de produtos ao estoque...')
  acrescimo = str(input('Digite  o nome do produto que deseja acrescentar: '))
  acrescimo_quantidade = int(input('Digite a quantidade: '))
  estoque [acrescimo] = acrescimo_quantidade

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

  if baixa_produto in estoque and baixa_produto > 0:
    quantidade_baixa = int(input(f'Digite quantas unidades do produto {baixa_produto} deseja repor: '))
    if estoque[baixa_produto] >= quantidade_baixa:
      estoque[baixa_produto] -= quantidade_baixa
      print(f'Atualizado!! A nova quantidade de {baixa_produto}: {estoque[baixa_produto]} unidades')
  else:
    print('Erro!!! Produto não encontrado no estoque')
elif comando_menu_informaçoes == 5:
  print('Encerrando sistema...')
  exit()
else:
  print('Erro,opção invalida!!')

print(f'Estoque atualizado!!',estoque)


response = model.generate_content(prompt)
print(response)
