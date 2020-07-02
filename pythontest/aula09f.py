frase = str(input('Digite uma frase ! ')).strip()

print('Seu nome contem {} letras "A" ! '.format(frase.upper().count('A')))
print('A letra "A" aparece a primeira vez na {}° posição ! '.format(frase.upper().find('A')+1))
print('A letra "A" aparece a ultimas vez na {}° posição ! '.format(frase.upper().rfind('A')+1))