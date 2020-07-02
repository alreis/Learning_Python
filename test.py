import re

frases = input('Chat: ')

if re.search('Y', frases, re.IGNORECASE):
    print('@#ù%'.format(nome.upper().find('Y')+1))
else:
    print('Seu nome não tem a letra Y!')