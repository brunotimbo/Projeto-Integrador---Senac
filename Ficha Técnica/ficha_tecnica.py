# importações
import sqlite3
import tkinter as tk
from tkinter import ttk                                         # importar subbliboteca do tkinter para tabela
import tkinter.messagebox as messagebox                         # mensgens de aviso

# variáveis globais
entry_busca_ingrediente = None

# conexão com banco de dados
conexao = sqlite3.connect('ficha_tecnica.db')
cursor = conexao.cursor()

# cria tabela ficha técnica
cursor.execute('''CREATE TABLE IF NOT EXISTS fichas(
        id INTEGER PRIMARY KEY,
        ingrediente TEXT NOT NULL,
        quantidade_comprada INTEGER,
        valor_comprado REAL,
        quantidade_usada INTEGER,
        unidade_medida TEXT,
        valor_gasto REAL)
        ''')

# cria tabela ingredientes
cursor.execute('''CREATE TABLE IF NOT EXISTS ingredientes(
        id INTEGER PRIMARY KEY,
        ingrediente TEXT NOT NULL)
        ''')

conexao.commit()
conexao.close()

##########################   CRUDs   ##########################

#cadastrar ingrediente
def cadastrar_ingrediente():
    
    ingrediente = entry_busca_ingrediente.get()
    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO ingredientes (ingrediente) VALUES (?)", (ingrediente,))
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Ingrediente", "Ingrediente adicionado a lista.")

#buscar ingrediente
def buscar_ingrediente():
    global entry_busca_ingrediente

    ingrediente = entry_busca_ingrediente.get()
    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * From ingredientes WHERE ingrediente = ?", (ingrediente,))
    resultado = cursor.fetchall()    
    conexao.commit()
    conexao.close()
    print(resultado)
    janela_top = tk.Toplevel()
    janela_top.geometry("500x500")
    janela_top.title("Resultado Busca")
    janela_top.resizable(False, False)

    tabela = ttk.Treeview(janela_top,columns=("id", "ingrediente") , show="headings", )
    
    # largura das colunas
    tabela.column("id", width=5, anchor="w")  # Coluna 1 com 100 pixels
    tabela.column("ingrediente", width=250, anchor="w")  # Coluna 2 com 250 pixels

    # títulos das colunas
    tabela.heading("id", text="ID")
    tabela.heading("ingrediente", text="Ingredientes")

    # exibe a tabela
    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()
    cursor.execute( "SELECT * FROM ingredientes WHERE ingrediente LIKE ?", (f"%{ingrediente}%",))
    resultado = cursor.fetchall()

    for linha in resultado:
        tabela.insert('', tk.END, values=linha)


    
    return resultado

#atualizar ingrediente
def atualiza_ingrediente(ingrediente):
    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE ingredientes SET ingrediente = ?", (ingrediente))
    conexao.commit()
    conexao.close()

#deletar ingrediente
def deleta_ingrediente(ingrediente):
    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM ingredientes WHERE ingrediente = ?", (ingrediente))
    conexao.commit()
    conexao.close()

#cadastrar ficha
#buscar ficha
#atualizar ficha
#deletar ficha

# limpar janela
def limpar_janela():
      for widget in janela.winfo_children():
            widget.destroy()

def atualiza_tabela_ingredientes():

    # Limpa a tabela antes de carregar novos dados
    for item in tabela_ingredientes.get_children():
        tabela_ingredientes.delete(item)

    # Conecta ao banco de dados SQLite
    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()

    # Busca os dados na tabela do banco
    cursor.execute("SELECT id, nome, FROM ingredientes")
    linhas = cursor.fetchall()

  # Insere os dados na Treeview
    for linha in linhas:
        tabela_ingredientes.insert("", "end", values=linha)

    conexao.close()


# # Configuração da Janela Principal
#     app = tk.Tk()
#     app.title("Exibir SQLite no Tkinter")
#     app.geometry("400x300")

#     # Criação do Treeview (Tabela)
#     colunas = ("ID", "Nome", "Idade")
#     tree = ttk.Treeview(app, columns=colunas, show="headings")

#     # Definindo os cabeçalhos
#     for col in colunas:
#     tree.heading(col, text=col)
#     tree.column(col, width=100)

#     tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

##########################   INTERFACE   ##########################


##########################   FRAME PRINCIPAL   ##########################

def tela_ficha():
    limpar_janela()

    janela.title("Ficha Técnica de Preparo")
    janela.geometry("500x500")


def tela_ingredientes():

    global entry_busca_ingrediente

    limpar_janela()

    # frame da tela ingredientes
    frame_ingredientes = tk.Frame(janela, borderwidth=1, relief="raised", bg="#FDC180")
    frame_ingredientes.pack(fill="both", expand=True)

    # título da tela ingredientes
    label_titulo = tk.Label(frame_ingredientes, text=" 🍴 Ingredientes 👨‍🍳", font=("Arial", 24), bg="#FDC180")
    label_titulo.pack(pady=10)

    frame_busca = tk.Frame(frame_ingredientes, borderwidth=1, relief="raised")
    frame_busca.pack(pady=10)

    entry_busca_ingrediente = tk.Entry(frame_busca)
    entry_busca_ingrediente.pack(side="left", padx=10, pady=5)

    botao_atualizar_tabela_ingredientes = tk.Button(frame_busca, text="Atualizar Lista")
    botao_atualizar_tabela_ingredientes.pack(side="right", padx=10, pady=5) 

    botao_cadastrar = tk.Button(frame_busca, text="Adicionar", command=cadastrar_ingrediente)
    botao_cadastrar.pack(side="right", padx=10, pady=5)

    botao_pesquisar = tk.Button(frame_busca, text="Pesquisar", command=buscar_ingrediente)
    botao_pesquisar.pack(side="right", padx=10, pady=5)


    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#004c94", foreground="#f7941d")
    estilo.configure("Treeview", rowheight=28, font=("Arial", 10))


    # cria tabela
    tabela = ttk.Treeview(frame_ingredientes,columns=("id", "ingrediente") , show="headings", )

    # largura das colunas
    tabela.column("id", width=5, anchor="w")  # Coluna 1 com 100 pixels
    tabela.column("ingrediente", width=250, anchor="w")  # Coluna 2 com 250 pixels

    # títulos das colunas
    tabela.heading("id", text="ID")
    tabela.heading("ingrediente", text="Ingredientes")

    # exibe a tabela
    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    conexao = sqlite3.connect("ficha_tecnica.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ingredientes")
    resultado = cursor.fetchall()

    for linha in resultado:
        tabela.insert('', tk.END, values=linha)

    # Seleciona as colunas id e ingrediente da tabela
    cursor.execute("SELECT id, ingrediente FROM ingredientes")

    conexao.close()

def tela_resultado_busca():
    limpar_janela()

    janela.title("Resultado da Busca")
    janela.geometry("500x500")
        

# cria a janela principal
janela = tk.Tk()
janela.title("Maedu")
janela.geometry("500x500")
janela.resizable(False, False)

tela_ingredientes()

# exibe dados na tabela
#busca_dados_tabela()

janela.mainloop()


##########################   FRAME INGREDIENTES   ##########################



##########################   FRAME BUSCA   ##########################





# def busca_dados_tabela():
#         conexao = sqlite3.connect('ficha_tecnica.db')
#         cursor = conexao.cursor()
#         cursor.execute("SELECT ID, ingrediente FROM ingredientes")
#         linhas = cursor.fetchall()

#         for linha in linhas:
#                tabela.insert("", "end", values=linha)

#         conexao.close()

# def exibir_menu():

#         print("""\n====== TABELA INGREDIENTES ======\n
# 1. Listar
# 2. Cadastrar
# 3. Buscar
# 4. Atualizar
# 5. Excluir""")

#         opcao = (input("\nEscolha a opção: "))
#         if opcao == '1':
#             listar_ingredientes()            
#         elif opcao == '2':
#             cadastrar_ingrediente()
#         elif opcao == '3':
#             buscar_ingrediente()
#         elif opcao == '4': 
#             atualizar_ingrediente()
#         elif opcao == '5':
#             excluir_ingrediente()
#         else:
#             print("Opção inválida!") 

# # Inserir dados na tabela ingredientes

# def listar_ingredientes():
#         cursor.execute('''SELECT COUNT(nome_ingrediente) FROM ingredientes WHERE nome_ingrediente IS'''" NOT NULL;")        
#         quantidade = cursor.fetchone()[0]
#         if quantidade > 0:
#                 cursor.execute("SELECT nome_ingrediente FROM ingredientes")
#                 resultados = cursor.fetchall()
#                 for linha in resultados:
#                         print(linha[0])
#         else:
#                 print("\nNão há ingredientes cadastrados.") 
#         while True:
#                 opcao = input("\nDigite 0 para voltar: ")
#                 if opcao == '0':
#                         exibir_menu()
#                 else:
#                         print("\nOpção invalida.")

# def cadastrar_ingrediente():
#         while True:
#                 ingrediente = input("\nDigite o ingrediente a ser cadastrado (0 para voltar): ")
#                 if ingrediente != '0':
#                         # Consulta com SELECT EXISTS e parâmetro seguro (?) para evitar SQL Injection
#                         cursor.execute('''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
#                         )
#                         # Recupera o resultado da consulta
#                         resultado = cursor.fetchone()
#                         # Se o primeiro valor da tupla for 1, o item existe
#                         if resultado[0] == 1:
#                                 print(f"O ingrediente '{ingrediente}' já está cadastrado.")
#                         else:
#                                 cursor.execute('''INSERT INTO ingredientes (nome_ingrediente) VALUES (?)''', (ingrediente,))
#                                 # Confirmar a transação
#                                 conexao.commit()
#                                 print(f"Ingrediente '{ingrediente}' cadastrado.")

#                 else:
#                        break
# def buscar_ingrediente():           

#         while True:
#                 ingrediente = input("\nDigite o ingrediente a ser procurado (0 para voltar): ")
#                 if ingrediente != '0':
#                         # Consulta com SELECT EXISTS e parâmetro seguro (?) para evitar SQL Injection
#                         cursor.execute(
#                                '''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
#                         )
#                         # Recupera o resultado da consulta
#                         resultado = cursor.fetchone()
#                         # Se o primeiro valor da tupla for 1, o item existe
#                         if resultado[0] == 1:
#                                 print(f"O ingrediente '{ingrediente}' está cadastrado.")
#                         else:
#                                 print(f"O ingrediente '{ingrediente}' não está cadastrado.")
#                 else:
#                        break


# def atualizar_ingrediente():

#         while True:

#                 ingrediente = input("\nDigite o ingrediente a ser atualizado (0 para voltar): ")
#                 if ingrediente != '0':
#                         # Consulta com SELECT EXISTS e parâmetro seguro (?) para evitar SQL Injection
#                         cursor.execute(
#                                 '''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
#                         )
#                         # Recupera o resultado da consulta
#                         resultado = cursor.fetchone()
#                         # Se o primeiro valor da tupla for 1, o item existe
#                         if resultado[0] == 1:
#                                 novo_ingrediente = input("\nDigite o novo nome do ingrediente: ")
#                                 cursor.execute(
#                                        '''UPDATE ingredientes SET nome_ingrediente = ? WHERE nome_ingrediente d= ?''', (novo_ingrediente, ingrediente,)
#                                 )
#                                 conexao.commit()
#                                 print("\nIngrediente atualizado!")
#                         else:
#                                 print(f"\nO ingrediente '{ingrediente}' não está cadastrado.")
#                 else:
#                         break

# def excluir_ingrediente():
#         while True:
#                 ingrediente = input("\nDigite o ingrediente a ser deletado (0 para voltar): ")
#                 if ingrediente != '0':
#                         cursor.execute(
#                                '''SELECT EXISTS(SELECT 1 FROM ingredientes WHERE nome_ingrediente = ? LIMIT 1)''', (ingrediente,)
#                         )
#                         resultado = cursor.fetchone()
#                         if resultado[0] == 1:
#                                 cursor.execute(
#                                         '''DELETE FROM ingredientes WHERE nome_ingrediente = ?''', (ingrediente,)
#                                 )
#                                 conexao.commit()
#                                 print(f"O ingrediente '{ingrediente}' foi excluido.")
#                         else:
#                                 print(f"O ingrediente '{ingrediente}' não está cadastrado.")
#                 else:
#                        break

# # criação da janela
# janela = tk.Tk()
# janela.title("Ficha Técnica")
# janela.geometry("400x400+100+100")
# janela.resizable(False, False)

# # frame
# frame_titulo = tk.Frame(janela)

# # label 1
# label_1 = tk.Label(janela, text="Ficha Técnica")
# label_1.pack()

# # tabela
# colunas = ("ID", "Ingrediente")
# tabela = ttk.Treeview(janela, columns=colunas, show="headings")

# # cabeçalho da tabela
# tabela.heading("ID", text="ID")
# tabela.heading("Ingrediente", text="Ingrediente")
# tabela.column("ID", width=10)
# tabela.column("Ingrediente", width=200)
# tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# # exibe dados na tabela
# busca_dados_tabela()

# botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_ingrediente)
# botao_cadastrar.pack()

# botao_buscar = tk.Button(janela, text="Buscar", command=buscar_ingrediente)
# botao_buscar.pack()

# botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_ingrediente)
# botao_atualizar.pack()

# botao_excluir = tk.Button(janela, text="Excluir", command=excluir_ingrediente)
# botao_excluir.pack()

# janela.mainloop()

# while True:

#         exibir_menu()


        
