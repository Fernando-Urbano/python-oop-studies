"""
Class Composition
Data: 25/01/2022

Relação entre classes:
- Composição: relação mais forte entre classes.
Uma classe é dona de objetos de outra classe. Quando isso acontece, caso a classe for apagada, todos os objetos
daquela classe também serão apagados

"""
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []  # Irei utilizar uma classe somente para criar endereços

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) # A classe endereço entra dentro do self.endereco

    def lista_enderecos(self):
        print(f'Endereços de {self.nome}:')
        for endereco in self.enderecos:
            print(endereco.cidade + ", " + endereco.estado)
        print()

    def __del__(self):
        print(f'{self.nome} apagado(a).')
        # A parte de __del__ serve para apagar parte do código depois que ele finaliza de ser executado


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}, {self.estado} foi apagado(a).')
        # A parte de __del__ serve para apagar parte do código depois que ele finaliza de ser executado


# No caso, nós estamos usando Endereco para compor Cliente
# Quando o cliente é apagado, o endereço também é apagado
cliente1 = Cliente('Fernando', 22)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
cliente1.lista_enderecos()

del cliente1  # Os endereços referentes ao cliente são apagados também
# Se todos os clientes forem apagados, o garbage collector não precisará apagar nada no final
# porque os respectivos endereços também serão apagados

cliente2 = Cliente('Eliott', 21)
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
cliente2.lista_enderecos()

cliente3 = Cliente('Marcelo', 22)
cliente3.inserir_endereco('São Paulo', 'SP')
cliente3.lista_enderecos()

print("##### Fim do Código #####\n")