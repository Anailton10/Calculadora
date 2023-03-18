class Calculadora:
    def __init__(self, a=0, b=0):
        self.n1 = a
        self.n2 = b
        self.__resp = None
    @property
    def soma(self):
        return self.n1 + self.n2

    @property
    def sub(self):
        return self.n1 - self.n2

    @property
    def mult(self):
        return self.n1 * self.n2

    @property
    def divi(self):
        try:
            d = self.n1 / self.n2
        except ZeroDivisionError:
            print('Não é possivel dividir um numero por Zero.')
        except (TypeError, ValueError):
            print('Problemas com os dados informados.')
        else:
            return d
