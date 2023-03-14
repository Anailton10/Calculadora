from Calculadora import Calculadora
from Calculadora import entrada, entrada_Inteiro
print('=' * 30)
print('CALCULADORA'.center(30))
print('=' * 30)
n1 = entrada('Primeiro Numero: ')
n2 = entrada('Segundo Numemro: ')
print('''[ 1 ] SOMA
[ 2 ] SUBTRÃO
[ 3 ] MULTIPLICAÇÃo
[ 4 ] DIVISÃO
[ 0 ] SAIR''')
resp = entrada_Inteiro('Escolha uma Opção:')
resul = Calculadora()
if resp == 0:
    print('Até Logo..')
    resul = '0.0'
elif resp == 1:
    resul = resul.soma(n1, n2)
elif resp == 2:
    resul = resul.divi(n1, n2)
elif resp == 3:
    resul = resul.mult(n1, n2)
elif resp == 4:
    resul = resul.divi(n1, n2)

print(f'Resultado: {resul}')


