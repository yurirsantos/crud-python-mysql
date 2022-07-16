import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='teste'
)

cursor = conexao.cursor()

saida = int(input("Digite 0 para inserir um produto: "))

# READ


def read():
    comando = 'SELECT * FROM vendas'

    cursor.execute(comando)

    resultado = cursor.fetchall()

    print(resultado)

# CREATE


while saida != 1:
    produto = input("Informe o produto: ")
    preco = float(input("Informe o valor do produto: "))

    comando = f'INSERT INTO vendas (produto, preco) VALUES ("{produto}", {preco})'

    cursor.execute(comando)
    conexao.commit()

    print("Produtos atualizados: ")
    read()

    saida = int(input(
        "Digite '1' sem as aspas para sair: "))

# UPDATE


saida = int(input("Digite 0 para realizar um update: "))

while saida != 1:
    read()
    produto = input("Informe o ID do produto para update: ")
    preco = float(input("Informe o valor novo: "))

    comando = f'UPDATE vendas SET preco = {preco} WHERE produto = "{produto}" '

    cursor.execute(comando)
    conexao.commit()

    print("Produtos atualizados: ")
    read()

    saida = int(input("Digite '1' sem as aspas para sair: "))

# DELETE

saida = int(input("Digite 0 para realizar um delete: "))

while saida != 1:
    read()

    produto = input("Informe o produto para delete: ")

    comando = f'DELETE FROM vendas WHERE produto = "{produto}" '

    cursor.execute(comando)
    conexao.commit()

    print("Produtos atualizados: ")
    read()

    saida = int(input("Digite '1' sem as aspas para sair: "))

cursor.close()
conexao.close()
