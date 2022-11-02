'''
Override Members

A herança pode ser multipla ou simples.


'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def relacao_empresa(self):  # Valido também para as classes que herdam
        print(f'{self.nome} é {self.nomeclasse}')


class Aluno(Pessoa):  # A classe aluno "herda" os atributos da classe pessoa
    def estudar(self):  # Estudar é um atributo especifico da classe aluno
        print(f'{self.nomeclasse} estudando...')


class Cliente(Pessoa):  # A classe cliente "herda" os atributos da classe pessoa
    def comprar(self):  # Comprar é um atributo especifico da classe aluno
        print(f'{self.nomeclasse} comprando...')


# Posso reescrever um mesmo método para outra classe. Por exemplo, se a compra do cliente VIP for com desconto,
# ele irá sobrepor o método anterior
class ClienteVip(Cliente):
    def comprar(self):   # Comprar é um método especifico da classe aluno
        print(f'{self.nomeclasse} comprando com desconto...')
        # Isso se chama sobreposição ou override


# Isso vale para o consultor também, por exemplo, se eu colocar outro init na classe,
# a definição da classe irá ter que colocar automaticamente novos atributos
class ClienteVip(Cliente):
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.nomeclasse = self.__class__.__name__

# E caso eu queira que ele execute o atributo da classe superior a classe em questão e mais algo:
class ClienteVip(Cliente):
    def comprar(self):
        super().comprar()  # Executa aquilo da classe superior
        print(f'Desconto aplicado!')

cliente1 = ClienteVip('Fernando', 31)
cliente1.comprar()

# Outra forma de fazer isso:
class ClienteVip(Cliente):
    def relacao_empresa(self):
        Pessoa.relacao_empresa(self)  # Dessa forma, consigo especificar o método de qual classe eu estou utilizando
        print(f'        Cliente Prioritário')
        # No caso de método de outra instância, é necessário colocar os parametros necessários para aquele método
        # Isso pode se tornar complexo dependendo do nível de hierárquia

cliente1 = ClienteVip('Fernando', 31)
cliente1.relacao_empresa()

# Se no cliente VIP quisermos adicionar mais um atributo
class ClienteVip(Cliente):
    def __init__(self, nome, idade, banker):
        Pessoa.__init__(self, nome, idade)  # Já irá executar tudo que está dentro da classe base
        # Poderia ser feito com super() também
        self.banker = banker


cliente1 = ClienteVip('Fernando', 31, 'Evandro')
# O nome não está sendo criado dentro de ClienteVIP, mas sim dentro de Pessoa

