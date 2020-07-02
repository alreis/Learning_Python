nome = input('Digite o nome de uma cidade: ').strip()
div = nome.split()

#print('O nome da cidade começa com "Santo" ?', 'SANTO' in div[0].upper())
if div[0].upper() == 'SANTO':
   print('O nome da cidade começa com a palavra "Santo" ! ')

else:
    print('O nome da cidade não começa com "Santo" ! ')
