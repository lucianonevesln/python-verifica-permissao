from clientes.clientes import Clientes
from calculo.calculo import Calcular


def executar_app():

    def calcular_permissao(cliente_idade):
        permissao = Calcular(cliente_idade)
        permissao = permissao.calculo()
        print(permissao)

    def converte_string_em_objeto():
        dados_cliente = [
            input("Digite um nome ou razão social: "),
            input("Digite um CPF ou CNPJ: "),
            input("Digite a idade ou tempo de existência da empresa: "),
        ]
        cliente = Clientes(dados_cliente[0], dados_cliente[1], int(dados_cliente[2]))
        cliente_idade = cliente.retorno_idade()
        return calcular_permissao(cliente_idade)

    converte_string_em_objeto()


if (__name__ == '__main__'):
    executar_app()
