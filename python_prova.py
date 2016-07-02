print('Ciao, Django girls!')
if 3>2:
    print("funziona!")
if 5>2:
    print('5 è infatti maggiore di 2')
else:
    print('5 non è maggiore di 2')
def ciao():
    print('Ciao!')
    print('Come stai?')
ciao()
def ciao(nome):
    if nome == 'Ola':
        print('ciao Ola!')
    elif nome == 'Sonja':
        print('ciao Sonia!')
    else:
         print ('ciao Anonimo!')
ciao('Paola')
def ciao(nome):
    print('Ciao '+ nome +'!')
ragazze =  ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Daniela']
for nome in ragazze:
    ciao(nome)
    print('Prossima ragazza')
