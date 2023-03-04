acumulador = 0 #Importante estar em 0 para somar um valor a mais que for solicitado
print('----------------------Seja bem vindo à Pizzaria Italian Pizzas---------------------')
print('****************************| Sabores e valores |*****************************')
print('*   Código   |      Sabores       |   Tamanho M  |  tamanho G 30%(mais caro) *')
print('*     10     |     Toscana        |    R$ 23.00  |   R$ 29.90                *')
print('*     20     |     Portuguesa     |    R$ 22.00  |   R$ 26.60                *')
print('*     30     |     Napolitana     |    R$ 35.00  |   R$ 45.50                *')
print('*     40     |     Calabresa      |    R$ 34.00  |   R$ 44.20                *')
print('*     50     |     Quatro-queijo  |    R$ 32.00  |   R$ 41.60                *')
print('***************************************&**************************************')
while True:
#Escolha do tamanho da pizza desejado m ou g | --digitar em minusculo!--
    tam = input('Escolha o tamanho da pizza m/g: ')
    if tam == 'm'or tam =='g':
        print('Tamanho selecionado') 
    else:#se o tamanho for diferente de m ou g cair nesse else
        print('Tamanho invalido. Informe o tamanho correto!')
        continue
#Se o cliente escolher pizza do tamanho 'm' irá entrar nesse if
    codigo = input('Informe o código da pizza: ')

#Escolha de tamanho 'm'
    if tam == 'm' and codigo == '10':
        acumulador = acumulador + 23 #Acumulador guarda o valor final dos das pizzas solicitadas
        print('Você escolhe o sabor toscana')
        print('Pedido realizado com sucesso!')
    elif tam == 'm' and codigo == '20':
        acumulador = acumulador + 22
        print('Você escolheu o sabor Portuguesa')
        print('Pedido realizado com sucesso!')
    elif tam == 'm' and codigo == '30':
        acumulador =acumulador + 35
        print('Você escolheu o sabor Napolitana')
        print('Pedido realizado com sucesso!')
    elif tam == 'm' and codigo == '40':
        acumulador =acumulador + 34
        print('Você escolheu o sabor Calabresa')
        print('Pedido realizado com sucesso!')
    elif tam == 'm' and codigo == '50':
        acumulador =acumulador + 32
        print('Você escolheu o sabor Quatro-queijo')
        print('Pedido realizado com sucesso!')

# Se o cliente escolher pizza do tamanho 'g' irá entrar nesse elif 30% mais caro
    elif codigo == '10' and tam == 'g':
        acumulador = acumulador + 29.90
        print('Você escolhe o sabor toscana')
        print('Pedido realizado com sucesso!')
    elif codigo == '20' and tam == 'g':
        acumulador = acumulador + 26.60
        print('Você escolheu o sabor Portuguesa')
        print('Pedido realizado com sucesso!')
    elif codigo == '30' and tam == 'g':
        acumulador = acumulador + 45.50
        print('Você escolheu o sabor Napolitana')
        print('Pedido realizado com sucesso!')
    elif codigo == '40' and tam == 'g':
        acumulador = acumulador + 44.20
        print('Você escolheu o sabor Calabresa')
        print('Pedido realizado com sucesso!')
    elif codigo == '50' and tam == 'g':
        acumulador = acumulador + 41.60
        print('Você escolheu o sabor Quatro-queijo')
        print('Pedido realizado com sucesso!')
#Se o código for digitado diferente de '10,20,30,40 e 50' cair nesse else
    else:
        print('Código invalido. Por favor digite novamente')
        continue
#Pergunta ao cliente se deseja algo a mais ---digitar 's' ou 'n' em minusculo
    resp = input('Deseja fazer mais algum pedido? (s/n)')
    if resp == 's':
        print('>> SIM')
        continue
#Caso o cliente não queira mais nada ira cair nesse else e encerrar o programa
    else:
        print('>>NÂO')
        print('Conta encerrada!')
        print('Pedido realizado com sucesso!!!')
        print('O total a ser pago é de: {:.2f}'.format(acumulador))
        break
