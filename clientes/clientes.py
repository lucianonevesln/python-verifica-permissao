class Clientes():

    def __init__(self, nome_razao_social, cpf_cnpj, idade):
        self.nome_razao_social = nome_razao_social
        self.cpf_cnpj = cpf_cnpj
        self.idade = idade

    def retorno_nome_razao_social(self):
        return self.nome_razao_social

    def retorno_cpf_cnpj(self):
        return self.cpf_cnpj

    def retorno_idade(self):
        return self.idade


if (__name__ == "__main__"):

    lista1 = ["Joao Pereira", "33333333333", "10"]
    cliente1 = Clientes(lista1[0], lista1[1], lista1[2])
    print(cliente1.retorno_nome_razao_social())
    print(cliente1.retorno_cpf_cnpj())
    print(cliente1.retorno_idade())

    lista2 = ["Luciano Neves", "11111111111", "22"]
    cliente2 = Clientes(lista2[0], lista2[1], lista2[2])
    print(cliente2.retorno_nome_razao_social())
    print(cliente2.retorno_cpf_cnpj())
    print(cliente2.retorno_idade())

    lista3 = ["Maria Silva", "22222222222", "25"]
    cliente3 = Clientes(lista3[0], lista3[1], lista3[2])
    print(cliente3.retorno_nome_razao_social())
    print(cliente3.retorno_cpf_cnpj())
    print(cliente3.retorno_idade())
