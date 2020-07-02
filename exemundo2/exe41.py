ano = int(input('Ano de nascimento : '))

if 2019 - ano <= 9:
    print('Categoria \33[1;36mMirim\33[m !')

elif 9 < 2019 - ano <= 14:
    print('Categoria \33[1;34mInfantil\33[m !')

elif 14 < 2019 - ano <= 19:
    print('Categoria \33[1;33mJunior\33[m !')

elif 2019 - ano == 20:
    print('Categoria \33[1;35mSênior\33[m !')

else:
    print('Categoria \33[1;31mMaster\33[m !')