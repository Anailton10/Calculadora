from Calculadora import Calculadora
print('=' * 30)
print('CALCULADORA'.center(30))
print('=' * 30)
while True:
    n1 = str(input('Primeiro Numero: ')).replace(',', '.').strip()
    if n1.isalpha() or '':
        print('Digite apenas numeros')
    else:
        n1 = float(n1)
        break

print('''[ + ] SOMA
[ - ] SUBTRÃO
[ * ] MULTIPLICAÇÃo
[ / ] DIVISÃO''')
resp = str(input('Escolha uma Opção:')).strip()
while True:
    n2 = str(input('Segundo Numero: ')).replace(',', '.').strip()
    if n2.isalpha() or '':
        print('Digite apenas numeros')
    else:
        n2 = float(n2)
        break

calculadora = Calculadora(n1, n2)
resul = 0
if resp == '+':
    resul = calculadora.soma
elif resp == '-':
    resul = calculadora.sub
elif resp == '*':
    resul = calculadora.mult
elif resp == '/':
    resul = calculadora.divi

print(f'Resultado: {resul}')


