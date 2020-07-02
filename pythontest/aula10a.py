import random
num = int(input('Descubra qual o numero selecionado entre 0 e 5 : '))
sel = random.randint(0, 5)

if sel == num :
    print('Você venceu !')

else:
    print('Você perdeu !')