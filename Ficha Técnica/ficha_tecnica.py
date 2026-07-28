import sqlite3

conexao = sqlite3.connect('ficha_tecnica.db')

cursor = conexao.cursor()

# cursor.execute('''
# CREATE TABLE Ficha_Tecnica(
# ID INTEGER PRIMARY KEY,
# Ingrediente TEXT NOT NULL,
# Quantidade_Comprada INTEGER,
# Preco_Comprado REAL,
# Quantidade_Usada INTEGER,
# Unidade TEXT,
# Preco_Gasto REAL
# )
# ''')

# conexao.commit()

