listaProdutos = [] #Essa lista é uma variavel global
#----------COMEÇO cadastrarProduto ----------
def cadastrarProduto(codigo):
    print ('Bem vindo ao controle de estoque da mercearia Vitor Oliveira')
    print('O codigo do produto a ser cadastrado é: {}'.format(codigo))
    nome = input('Por favor digite o nome do produto: ')
    fabricante = input('Por favor digite o fabricante do produto: ')
    valor = input('Por favor informe o valor do produto: ')
    dicionarioProduto = {'codigo'     : codigo,  #Dicionario lista o código, nome,fabricante, valor
                         'nome'       : nome,
                         'fabricante' : fabricante,
                         'valor'      : valor}
    listaProdutos.append(dicionarioProduto.copy()) #Adiciona uma cópia do dicionário
#----------FIM cadastrarProduto----------

#----------COMEÇO consultarProdutos----------
def consultarProdutos():
    while True:
        try: #Será protegido por qualquer erro de digitação
            print ('Bem-vindo a consulta de produtos')
            opConsultar = int(input('Informe a opção desejada:\n1- Consultar todos os produtos\n2- Consultar produto por código:\n3- Consultar produto por fabricante:\n4- Retornar\n>>'))
            if opConsultar == 1:
                print('Você selecionou a opção - consultar todos os produtos-')
                for produto in listaProdutos: #Selecionar cada dicionario da minha lista (Cada produto da lista de produtos)
                    for key, value in produto.items(): #Selecionar cada conjunto chave/valor do dicionario
                        print('{} : {}'.format(key,value))
            elif opConsultar == 2:
                print('Você selecionou a opção -consultar produto por código-')
                entrada = int(input('Informe o código desejado:'))
                for produto in listaProdutos:
                    if (produto['codigo'] == entrada):
                        for key, value in produto.items(): #Selecionar cada conjunto chave/valor do dicionario
                            print('{} : {}'.format(key, value))
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
            print('Pare de digitar valores que são inteiros!')
#----------FIM consultarProduto----------

#----------COMEÇO removerProduto----------
def removerProduto():
    print ('Bem-vindo a remover produtos')
    entrada = int(input('Informe o código desejado:'))
    for produto in listaProdutos:
        if (produto['codigo'] == entrada):
            listaProdutos.remove(produto)
#----------FIM removerProduto----------

#----------COMEÇO DA MAIN----------
print('Bem vindo ao controle de estoque da mercearia Vitor Oliveira')
registroProduto = 0 #Importante começar com 0 porque irá servir como acumulador
while True:
    try: #Será protegido por qualquer erro de digitação
        opcao = int(input('Informe a opção desejada: \n1- Cadastrar Produtos\n2- Consultar produto por código\n3- Remover produto\n4- Sair\n>>'))
        if opcao == 1:
            registroProduto = registroProduto + 1
            cadastrarProduto(registroProduto)
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
            print('Número invalido. Digite a opção correta!')
            continue
    except ValueError:
        print('Pare de digitar valores que são inteiros!')
#----------FIM DA MAIN----------
