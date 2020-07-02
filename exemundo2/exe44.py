print('=='*20)
preco = float(input('Qual o preço do produto ? '))
cond = str(input('Escolha entre as formas de pagamento !\n{}\nDinheiro/Cheque:\nCartão de Credito/Debito:\n{}\n'.format('=='*20, '=='*20)))
par = ""

if cond.upper() == 'DINHEIRO' or cond.upper() == 'CHEQUE':
    print('Você tera 10% de desconto e pagara: {:.2f} Reais'.format(preco-(preco*0.1)))

elif cond.upper() == 'CARTAO DE DEBITO' or cond.upper() == 'DEBITO':
    print('Você tera 5% de desconto e pagara: {:.2f} Reais'.format(preco-(preco*0.05)))

if cond.upper() == 'CARTAO DE CREDITO' or cond.upper() == 'CREDITO':
    par = int(input('Em quantas parcelas ? '))

if par == 1:
    print('Você tera 5% de desconto e pagara: {:.2f} Reais'.format(preco-(preco*0.05)))

if par == 2:
    print('Sem juros ou descontos !')
    print('Valor: {:.2f} Reais\nCada parcela sera de: {:.2f} Reais'.format(preco, preco/2))

if par == 3:
    print('20% de Juros !')
    print('Valor: {:.2f} Reais\nCada parcela sera de: {:.2f} Reais'.format(preco+(preco*0.20), (preco+(preco*0.20))/3))

else:
    print('\33[1;31m{}\nErro na forma de pagamento !\nFovar reiniciar o programa !\n{:}\33[m'.format('=='*20, '=='*20))


