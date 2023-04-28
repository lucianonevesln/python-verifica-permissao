class Calcular():

    def __init__(self, idade):
        self.idade = idade

    def calculo(self):
        if self.idade <= 17:
            permissao = "\nNÃO ATENDE\n"
        elif self.idade > 17 and self.idade <= 23:
            permissao = "\nATENDE PARCIALMENTE\n"
        else:
            permissao = "\nATENDE PLENAMENTE\n"
        return permissao


if (__name__ == "__main__"):

    valor = int("10")
    cliente1 = Calcular(valor)
    print(cliente1.calculo())

    valor = int("22")
    cliente1 = Calcular(valor)
    print(cliente1.calculo())

    valor = int("25")
    cliente1 = Calcular(valor)
    print(cliente1.calculo())
