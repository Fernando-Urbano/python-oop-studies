'''
SQLite - sqlite3

'''
import sqlite3

# Essa variável vai receber uma conexão com uma base de dados
conexao = sqlite3.connect('database.db')  # Esse é o nome do arquivo. A extensão não é necessária, mas é
# bom ter ela para que as pessoas saibam que estamos tratando de base de dados
cursor = conexao.cursor()
# O objeto de cursor é necessário para fazer o que queremos
# É uma boa prática de programação que nós feichemos o programa após finalizar de utilizá-lo
# Para criar uma tabela, é importante utilizar o execute.
cursor.execute(
    'CREATE TABLE IF NOT EXISTS pessoas ('  # O comando somente executará isso se a tabela não existir
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # É importante especificar o tipo de cada coluna (id é uma
    # coluna). Além disso, PRIMARY KEY se refere ao fato de id ser a base pela qual vamos relacionar essa tabela
    # com outras tabelas. O AUTOINCREMENT serve para que não precisemos nos preocupar...
    # a primeira linha será 1, a segunda 2, etc... de forma automatica.
    'nome TEXT'  # TEXT é string
    'peso REAL'  # REAL é float
    ')'
)

# Inserindo um registro nessa tabela
cursor.execute(  # Não é necessário colocar o id
    'INSERT INTO pessoas (nome) VALUES ("Fernando")'
)
conexao.commit()  # Isso faz com que a conexão salve a nova base de dados

cursor.execute('SELECT * FROM pessoas')  # * significa all
# É necessário colocar o fetchall para que ele me mostre os valores que ele buscou
for linha in cursor.fetchall():
    print(linha)

# Outra possibilidade
cursor.execute('SELECT * FROM pessoas')  # * significa all
# É necessário colocar o fetchall para que ele me mostre os valores que ele buscou
for linha in cursor.fetchall():
    identificador, nome = linha  # Estamos desempacotando a linha
    print(f'{identificador}. {nome}')

print('\n' * 5)
# No entanto, fazer isso dessa forma é perigoso. A melhor forma de fazer isso
# é através de sql injection.
# É melhor fazer assim:
# cursor.execute(
#     'INSERT INTO pessoas (nome) VALUES (?)', ('Joana')
# )
# Se for mais de um valor, deve ser dentro de uma tupla
# Outra forma também mais segura de fazer:
cursor.execute(
    'INSERT INTO pessoas (nome) VALUES (:nome)',
    {'nome': 'Joana'}  # Utilizamos o dicionário ao invés
)
conexao.commit()

# Como ler e manipular os valores ----
# Por exemplo, mudar o id
cursor.execute(
    'UPDATE pessoas SET nome =:nome WHERE id=:id',
    {'nome': 'Ana', 'id': 2}  # Irá mudar o nome
)

# Retirar um valor
cursor.execute(
    'DELETE FROM pessoas WHERE id=:id',
    {id: 4}  # Retira aquele id em consideração
)

cursor.close()
conexao.close()
