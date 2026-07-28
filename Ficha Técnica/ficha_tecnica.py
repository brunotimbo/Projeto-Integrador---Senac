import sqlite3

conexao = sqlite3.connect('ficha_tecnica.db')

cursor = conexao.cursor()

# cria tabela ficha técnica
cursor.execute('''CREATE TABLE IF NOT EXISTS Ficha_Tecnica(
        ID INTEGER PRIMARY KEY,
        Ingredientes TEXT NOT NULL,
        Quantidade_Comprada INTEGER,
        Preco_Comprado REAL,
        Quantidade_Usada INTEGER,
        Unidade TEXT,
        Preco_Gasto REAL
        )
        ''')

#cria tabela ingredientes
cursor.execute('''CREATE TABLE IF NOT EXISTS ingredientes(
        ID INTEGER PRIMARY KEY,
        nome_ingrediente TEXT NOT NULL )
        ''')

#cria tabela produtos
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(
        ID INTEGER PRIMARY KEY,
        nome_produto TEXT NOT NULL
        )
        ''')
conexao.commit()

# Inserir dados na tabela ingredientes
def inserir_dados(ingrediente):

        cursor.execute('''INSERT INTO ingredientes (nome_ingrediente)
        VALUES (?)''', (ingrediente,))

        # Confirmar a transação
        conexao.commit()


while True:

        ingrediente = input("Digite o ingrediente (0 para sair): ")
        inserir_dados(ingrediente)

        if ingrediente == '0':
                break
        else:
                inserir_dados(ingrediente)

                

        



