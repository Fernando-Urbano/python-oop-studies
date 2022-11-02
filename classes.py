"""
Classes
Data: 24/01/2022

"""
from datetime import datetime

# Uma classe sempre é feita com letras maísculas
class BasePessoa:
    pass

p1 = BasePessoa()
p2 = BasePessoa()

print(p1) # É um objeto da classe BasePessoa. Estamos utilizando um "molde"
print(p2)

p1.nome = 'Luiz'

try:
    print(p2.nome) # Não tem esse atributo
except AttributeError as error:
    print("Erro:")
    print(error)

# Colocando atributos nas classes ----
# Um método é uma função que pertence a uma classe
class BasePessoa:
    def falar(self):
        # O self serve para saber de qual instância eu estou falando
        print("Pessoa está falando...")

p1 = BasePessoa()

p1.falar() # Executa a função

# Colocando atributos... ----
class BasePessoa:
    def __init__(self, nome, idade, brasileiro=True, homem=False):
        # O primeiro parametro irá ser sempre self
        # Ele pode ter o nome que você desejar
        # Mas por convenção utilizamos self
        # Ele irá ser enviado automaticamente
        # Se um parametro não tiver um default, é obrigatório passar esse parametro
        pass

p1 = BasePessoa(nome='Fernando', idade=22, homem=True)

p1.nome = 'Bruno'
print(p1.nome)

# Mesma ideia, mas atribuindo o self:
class BasePessoa:
    def __init__(self, nome, idade, brasileiro=True, homem=False):
        self.ano_nascimento = None
        self.nome = nome
        self.idade = idade
        self.brasileiro = brasileiro
        self.homem = homem
        # O self é utilizado para conseguirmos utilizarmos aquelas variáveis em outras partes da classe
        # Se não fizermos isso, os parametros passados não poderão ser utilizados em outra

        # Por exemplo, a variável abaixo não estar disponível para outros métodos
        codigo_pessoa = 1
        # Para que o código possa ser usado sem o self, ele deve ser definido antes do __init__
        if self.homem == True:
            print(f'{self.nome} criado com sucesso.')
        else:
            print(f'{self.nome} criada com sucesso.')

    def alterar_idade(self, idade):
        if idade == self.idade:
            print("A nova idade é igual a anterior.")
        else:
            self.idade = idade
            print("Idade alterada.")

    def mostrar_pessoa(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Brasileiro: {'Sim' if self.brasileiro == True else 'Não'}")
        print(f"Genero: {'Masculino' if self.homem == True else 'Feminino'}")

    def gerar_ano_nascimento(self):
        ano_atual = int(datetime.strftime(datetime.now(), "%Y"))
        self.ano_nascimento = ano_atual - self.idade  # O ideal é fazer um None na base da classe,
        # caso ele não exista previamente
        return self.ano_nascimento


p1 = BasePessoa(nome='Fernando', idade=22, homem=True)
p2 = BasePessoa(nome='Ana Luísa', idade=20)
p3 = BasePessoa(nome='Alex Binn', idade=22, brasileiro=False)
p4 = BasePessoa(nome='Marjolaine', idade=22, brasileiro=False, homem=False)

p2.alterar_idade(20)
print(p2.idade)

p2.mostrar_pessoa()
p2.gerar_ano_nascimento()

