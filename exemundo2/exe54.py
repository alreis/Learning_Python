print('\033[1;32mLeitor de Maioridade!\033[m')
cand = int(input('Insira o numero de candidatos para a analise: '))
cand0 = 0
tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0
for c in range(1, cand+1):
    cand0 = int(input('Ano de nascimento do {}° candidato: '.format(c)))
    if cand0 <= 2001 and cand0 > 1900:
        print('\033[1;32m{}° candidato é maior de idade!\033[m'.format(c))
        tot1 += 1

    elif cand0 >= 2020:
        print('\033[1;;41m{}° candidato ainda não nasceu!\033[m'.format(c))
        tot3 += 1

    elif cand0 <= 1900:
        print('\033[1;;45m{}° candidato é quase um fossil!\033[m'.format(c))
        tot4 += 1

    elif cand0 > 2001 and cand0 < 2019:
        print('\033[1;31m{}° candidato não é maior de idade!\033[m'.format(c))
        tot2 += 1

print('\033[1;34m{}\033[m\033[1;32m\n{} candidato(s) é/são maiores de idade!\033[m'.format('='*50 ,tot1))
print('\033[1;34m{}\033[m\033[1;31m\n{} candidato(s) é/são menores de idade!\033[m'.format('='*50, tot2))
print('\033[1;31m{}\033[m\033[1;31m\n{} não nascido(s)!\033[m'.format('='*50, tot3))
print('\033[1;35m{}\033[m\033[1;35m\n{} fosseis!\033[m'.format('='*50, tot4))