
!pip install emoji
print('\n📦Seja Bem-Vindo ao nosso Estoque!📦')


cadastro = int(input('Digite a quantidade de produtos que deseja cadastrar: '))

def cadastrar (nome,quantidade):
  return nome , quantidade

produtos = []


for repetir in range(cadastro):

  nome_produto = input('Nome do produto: ')
  quantidade_produto = int(input('Quantidade do produto: '))
  nome_qtd = cadastrar(nome_produto,quantidade_produto)
  produtos.append(nome_qtd)

  print()


if cadastro > 0:
    print('Produtos Cadastrados com Sucesso')


print()
print('\n(1)Adicionar um produto.')
print('\n(2)Remover um produto.')
print('\n(3)Listar itens do estoque:')

desejo = int(input('\nO que deseja fazer:'))

if desejo == 1:
  fazer = int(input('Quantidade de produtos á adicionar: '))
  quantidade_produto += fazer
  print(f'Estoque atualizado: {produtos['quantidade_produtos',1]} unidades')
elif desejo == 2:
  diminuir = int(input('Quantidade de produtos vendidos: '))
  produto -= diminuir
  print(f'Estoque atualizado: {lista['quantidade']}')
elif desejo == 3:
  print(f'Aqui Está a lista de produtos e quantidade que temos no estoque:')
  for lista in produtos:
      print(lista)
elif desejo >= produto:
  print('ERRO! Quantidade insuficiente!!')
else:
  print('Outra função')
