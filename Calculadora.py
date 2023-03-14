class Calculadora:
    def __init__(self, a=0, b=0):
        self.n1 = a
        self.n2 = b

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def divi(self, a, b):
        try:
            d = a / b
        except ZeroDivisionError:
            print('Não é possivel dividir um numero por Zero.')
        except (TypeError, ValueError):
            print('Problemas com os dados informados.')
        else:
            print(f'O resultado:{d}')
def entrada(msg):
    while True:
        resp = str(input(msg)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print('Informe apenas Numeros')
            #print(f'ERRO \"{resp}\" é um preço inválido!')
        else:
            return float(resp)

def entrada_Inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite uma opção válida')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dado interromppida...')
            return 0
        else:
            return n