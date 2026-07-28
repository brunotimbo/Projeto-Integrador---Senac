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

def exibir_menu():

        print("""\n====== MENU ======\n
O que deseja fazer?\n
1. Listar
2. Cadastrar
3. Buscar
4. Atualizar
5. Excluir""")

        opcao = (input("\nEscolha a opção: "))

        if opcao == '1':
            listar_ingredientes()
            
        elif opcao == '2':
            cadastrar_ingrediente()

        elif opcao == '3':
            buscar_ingrediente()            

        elif opcao == '4': 
            atualizar_ingrediente()

        elif opcao == '5':
            excluir_ingrediente()
        else:
            print("Opção inválida!") 

# Inserir dados na tabela ingredientes

def listar_ingredientes():
        cursor.execute('''SELECT ingrediente FROM ingredientes''')

def cadastrar_ingrediente(ingrediente):

        cursor.execute('''INSERT INTO ingredientes (nome_ingrediente)
        VALUES (?)''', (ingrediente,))

        # Confirmar a transação
        conexao.commit()
        print(f"\nIngrediente {ingrediente} inserido.")


def buscar_ingrediente():           
        pass

def atualizar_ingrediente():
        pass

def excluir_ingrediente():
        pass

while True:

        ingrediente = input("Digite o ingrediente (0 para sair): ")

        if ingrediente == '0':
                break
        else:
                cadastrar_ingrediente(ingrediente)

                

        



