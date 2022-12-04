#Introdução
print('**********| Comércio em Atacado Vitor Oliver |***********')
print('<< Seja bem vindo ao maior centro de atacado do Brasil >>')
print('')

#Escolha do cliente
valorUnidade = float (input('informe qual o valor unitário do produto: '))
print('O valor do produto informado foi: R${:.2f} '.format(valorUnidade))
qtdProduto = int (input('Informe a quantidade desejada: '))
print('A quantidade do produto informada foi: {} Unidades '.format(qtdProduto))
total = valorUnidade * qtdProduto

#condições de descontos dos cliente
if total < 4: #Quantidade menor que 4 não se aplica desconto
    valorFinal = total
#valor com 3% de desconto
elif 5 <= total < 19:
    valorFinal = total - total * 0.03
    desconto = 3
#valor com 6% de desconto
elif 20 <= total < 99:
    valorFinal = total - total * 0.06
    desconto = 6
#se o valor for acima de 100 produtos entrar direto nesse else
else:
    valorFinal = total - total * 0.10 #desconto de 10%
    desconto = 10
#Valaor final com e sem desconto
print('O total da compra sem desconto é de: R${:.2f}'.format(total))
print('O total da compra com descoonto é de: R${:.2f}. Com desconto aplicado de: {}%'.format(valorFinal,desconto))
