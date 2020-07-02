import math
cao = float(input('Tamanho do cateto oposto ? '))
caa = float(input('Tamanho cateto adjacente ? '))
hipo = ((cao*cao) + (caa*caa))
hipo1 = math.sqrt(hipo)
print('A hipotenusa é : {:.2f}'.format(hipo1))