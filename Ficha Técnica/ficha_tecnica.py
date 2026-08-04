# importações
import sqlite3
import tkinter as tk
from tkinter import ttk                                         #importar subbliboteca do tkinter para tabela

# conexão com banco de dados
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
        Preco_Gasto REAL)
        ''')

# cria tabela ingredientes
cursor.execute('''CREATE TABLE IF NOT EXISTS ingredientes(
        ID INTEGER PRIMARY KEY,
        nome_ingrediente TEXT NOT NULL)
        ''')

# cria tabela produtos
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(
        ID INTEGER PRIMARY KEY,
        nome_produto TEXT NOT NULL)
        ''')

conexao.commit()

# limpa tabela 
def limpa_tabela():

        for item in tabela.get_children():
                tabela.delete(item)

def busca_dados_tabela():

        cursor.execute("SELECT ID, nome_ingrediente FROM ingredientes")
        linhas = cursor.fetchall()

        for linha in linhas:
               tabela.insert("", "end", values=linha)

        conexao.close()

def exibir_menu():

        print("""\n====== TABELA INGREDIENTES ======\n
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

        cursor.execute('''SELECT COUNT(nome_ingrediente) FROM ingredientes WHERE nome_ingrediente IS'''" NOT NULL;")
        
        quantidade = cursor.fetchone()[0]

        if quantidade > 0:
                cursor.execute("SELECT nome_ingrediente FROM ingredientes")

                resultados = cursor.fetchall()

                for linha in resultados:

                        print(linha[0])

        else:
                print("\nNão há ingredientes cadastrados.")

        

        while True:

                opcao = input("\nDigite 0 para voltar: ")

                if opcao == '0':

                        exibir_menu()

                else:

                        print("\nOpção invalida.")

def cadastrar_ingrediente():

        while True:

                ingrediente = input("\nDigite o ingrediente a ser cadastrado (0 para voltar): ")

                if ingrediente != '0':

                        # Consulta com SELECT EXISTS e parâmetro seguro (?) para evitar SQL Injection
                        cursor.execute('''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
                        )

                        # Recupera o resultado da consulta
                        resultado = cursor.fetchone()

                        # Se o primeiro valor da tupla for 1, o item existe
                        if resultado[0] == 1:
                                print(f"O ingrediente '{ingrediente}' já está cadastrado.")
                        else:
                                cursor.execute('''INSERT INTO ingredientes (nome_ingrediente) VALUES (?)''', (ingrediente,))
                                
                                # Confirmar a transação
                                conexao.commit()
                                print(f"Ingrediente '{ingrediente}' cadastrado.")

                else:
                       break

def buscar_ingrediente():           

        while True:

                ingrediente = input("\nDigite o ingrediente a ser procurado (0 para voltar): ")

                if ingrediente != '0':

                        # Consulta com SELECT EXISTS e parâmetro seguro (?) para evitar SQL Injection
                        cursor.execute(
                               '''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
                        )

                        # Recupera o resultado da consulta
                        resultado = cursor.fetchone()

                        # Se o primeiro valor da tupla for 1, o item existe
                        if resultado[0] == 1:
                                print(f"O ingrediente '{ingrediente}' está cadastrado.")
                        else:
                                print(f"O ingrediente '{ingrediente}' não está cadastrado.")
                else:
                       break


def atualizar_ingrediente():

        while True:

                ingrediente = input("\nDigite o ingrediente a ser atualizado (0 para voltar): ")

                if ingrediente != '0':

                        # Consulta com SELECT EXISTS e parâmetro seguro (?) para evitar SQL Injection
                        cursor.execute(
                                '''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
                        )

                        # Recupera o resultado da consulta
                        resultado = cursor.fetchone()

                        # Se o primeiro valor da tupla for 1, o item existe
                        if resultado[0] == 1:

                                novo_ingrediente = input("\nDigite o novo nome do ingrediente: ")

                                cursor.execute(
                                       '''UPDATE ingredientes SET nome_ingrediente = ? WHERE nome_ingrediente d= ?''', (novo_ingrediente, ingrediente,)
                                )

                                conexao.commit()

                                print("\nIngrediente atualizado!")

                        else:
                                print(f"\nO ingrediente '{ingrediente}' não está cadastrado.")

                else:
                        break

def excluir_ingrediente():

        while True:

                ingrediente = input("\nDigite o ingrediente a ser deletado (0 para voltar): ")

                if ingrediente != '0':

                        cursor.execute(
                               '''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
                        )

                        resultado = cursor.fetchone()

                        if resultado[0] == 1:
                                cursor.execute(
                                        '''DELETE FROM ingredientes WHERE nome_ingrediente = ?''', (ingrediente,)
                                )
                                conexao.commit()
                                print(f"O ingrediente '{ingrediente}' foi excluido.")
                        else:
                                print(f"O ingrediente '{ingrediente}' não está cadastrado.")
                else:
                       break
# criação da janela
janela = tk.Tk()
janela.title("Ficha Técnica")
janela.geometry("400x400+100+100")
janela.resizable(False, False)

# label 1
label_1 = tk.Label(janela, text="Menu")
label_1.pack()

# tabela
colunas = ("ID", "Ingrediente")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

# cabeçalho da tabela
tabela.heading("ID", text="ID")
tabela.heading("Ingrediente", text="Ingrediente")
tabela.column("ID", width=10)
tabela.column("Ingrediente", width=200)

tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# exibe dados na tabela
busca_dados_tabela()

botao_listar = tk.Button(janela, text="Listar", command=listar_ingredientes)
botao_listar.pack()
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_ingrediente)
botao_cadastrar.pack()
botao_buscar = tk.Button(janela, text="Buscar", command=buscar_ingrediente)
botao_buscar.pack()
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_ingrediente)
botao_atualizar.pack()
botao_excluir = tk.Button(janela, text="Excluir", command=excluir_ingrediente)
botao_excluir.pack()

janela.mainloop()

while True:

        exibir_menu()
