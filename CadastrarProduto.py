listaProdutos = []
#-----------Começo CadastrarProdutos--------------
def CadastrarProdutos(codigo):
    print('Bem vindo ao controle de estoque')
    print('O codigo do produti a ser cadastrado é: {}'.format(codigo))
    nome = input('Por favor digite o nome do produto: ')
    fabricante = input('Por favo digite o nome do fabricante do produto: ')
    valor = input('Por favor informe o valor do produto: ')
    dicionarioProduto = {'codigo'     :codigo,   #Dicionario lista o codigo, nome, fabricante e valor
                        'nome'        : nome,
                        'fabricante'  : fabricante,
                        'valor'       : valor}
    listaProdutos.append(dicionarioProduto.copy()) #Adciona uma cópia do dicionário
#------------ Fim cadastrarProduto--------------------

#------------ Começo consultarProdutos ---------------
def consultarProdutos():
    while True:
        try:
            print('Bem vindo a consulta de produtos!')
            opConsultar = int(input('Informe a opção desejada: \n1- Consultar todos os produtos\n2- Consultar produto por código:\n3- Consultar produto por fabricante:\n4- Retornar\n>> '))
            if opConsultar == 1:
                print('Você selecionou a opção - Consultar todos os produtos-')
                for produto in listaProdutos:
                    for key, Value in produto.items(): 
                        print('{}  :  {}'.format(key, Value))
            elif opConsultar == 2:
                print('Você selecionou a opção - Consultar produto por código-')
                entrada = int(input('Informe o código desejado: '))
                for produto in listaProdutos:
                    if (produto['codigo'] == entrada):
                        for key, value in produto.items():
                            print('{}  :  {}'.format(key, value))
            elif opConsultar == 3:
                print('Você selecionou a opção -Consultar produto por fabricante-')
                entrada = input('Informe o fabricante desejado:')
                for produto in listaProdutos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                break
            else:
                print('Número invalido. Digite a opção correta!')
                continue
        except ValueError:
            print('Pare de digitar que não são inteiros!')
#---------------Fim Consulta Produto--------------

#---------------Começo Remover Produto--------------
removerProduto():
print('Bem vindo a remover produtos')
entrada = int(input('Inform o código desejado: '))
for produto in listaProdutos:
    if (produto['codigo'] == entrada):
        listaProdutos.remove(produto)
#-------------Fim Lista de produtos----------------

#------------- Começo da Main--------------
print('Bem vindo ao controle de estoque')
registroProduto = 0
while True:
    try:
        opcao = int(input('Informe a opção desejada: \n1- Cadastrar produtos\n2- Consultar produtos por código\n3- Remover produtos\n4- Sair\n>>'))
        if opcao == 1:
            registroProduto = registroProduto + 1
        elif opcao == 2:
            registroProduto = registroProduto + 2
            consultarProdutos()
        elif opcao == 3:
            registroProduto = registroProduto + 3
            removerProduto()
        elif opcao == 4:
            registroProduto = registroProduto + 4
            print('Programa encerrado')
            break
        else:
            print('Número invalido. Digite a opção correta!!!')
            continue
    except ValueError:
        print('Pare de digitar valores que são incorretos!!!')
#------------- Fim da Main ----------------