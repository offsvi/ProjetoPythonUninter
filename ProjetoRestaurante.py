#Começo da função volumeFeijoada
def volumeFeijoada():
    while True:
        try:
            print('Menu volume da feijoada')
            volumeF = float(input('Informe a quantidae que deseja (ml):\n>> '))
            if 300 <= volumeF <= 5000:
                print('Pedido aceito!')
                return 25
            else:
                print('não aceitamos porções menores que 300ml ou maiores que 5L. Informe novamente!')
        except ValueError:
            print('Pare de digitar valores não numéricos!')
            continue

#Fim da função volumeFeijoada
#Começo da função opcaoFeijoada
def opcaoFeijoada():
    while True:
        print('Menu opção da feijoada')
        opcaoF = input('Escolha uma das opções: \nb- Básica (Feijão + Paiol + Costelinha)- \np- Premium (Feijão + Paiol + Costelinha + Partes do porco)- \ns- (Feijão + paiol + Costelinha + partes do porco + charque + calabresa + bacon)\n>> ')
        if opcaoF == 'b':
            return 1.0
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Você não digitou uma opção Valida. Digite novamente')
            continue
#Fim da função opcaoFeijoada
#Começo da função acompanhamentoFeijoada
acumulador = 0
def acompanhamentoFeijoada():
    while True:
        try:
            print('Menu acompanhamento da feijoada')
            acompF = input('deseja algum acompanhamento: \n 0- Não desejo mais acompanhamentos (encerrar pedido)\n1- 200g de arroz\n2- 150g de farofa especial\n3- 100g de couve cozida\n4- 1 laranja descascada\n>>')
            if acompF == '1':
                print('200g de arroz')
                return 5.0
            elif acompF == '2':
                print('150g de farofa especial')
                return 6.0
            elif acompF == '3':
                print('100g de couve cozida')
                return 7.0
            elif acompF == '4':
                print('1 laranja descascada')
                return 3.0
            elif  acompF == '0':
                print('Não desejo mais acompanhamentos (Encerrar pedido)')
                break
            else:
                print('Número não encontrado! Digite novamente')
                continue
        except ValueError:
            print('Pare de digitar valores não numéricos!')
            continue
#Fim da função acompanhamentoFeijoada
#COMEÇO DA MAIN
print('Seja bem vindo ao restaurante&rodizio Vitor Oliver')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total =  volume * opcao * acompanhamento
print('O valor a ser pago é de: R$ {:.2f}' .format(total))
#FIM DA MAIN