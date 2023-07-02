import sqlite3
from rich import print, table

conexao = sqlite3.connect('TAREFAS.db')
cursor = conexao.cursor()
comando = 'CREATE TABLE TAREFAS (ID INTEGER PRIMARY KEY, TAREFA TEXT VARCHAR(50), ESTADO VARCHAR(50))'


def addDb(tarefa):
    conexao = sqlite3.connect('TAREFAS.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT MAX(ID) FROM TAREFAS")
    resultado = cursor.fetchone()
    ultimo_id = resultado[0] if resultado[0] else 0
    novo_id = ultimo_id + 1
    
    comando = f"INSERT INTO TAREFAS VALUES({novo_id}, '{tarefa}', 'Não finalizada')"
    cursor.execute(comando)

    conexao.commit()
    conexao.close()
    
def removeDb(id):
    conexao = sqlite3.connect('TAREFAS.db')
    cursor = conexao.cursor()
    comando = f"SELECT TAREFA FROM TAREFAS WHERE ID = {id}"
    cursor.execute(comando)
    resultado = cursor.fetchone()
    tarefa_removida = resultado[0] if resultado else None

   
    comando = f"DELETE FROM Tarefas WHERE ID = {id}"
    cursor.execute(comando)

    conexao.commit()
    conexao.close()

    return tarefa_removida

def listDb():
    conexao = sqlite3.connect('TAREFAS.db')
    cursor = conexao.cursor()
    
    comando = "SELECT * FROM TAREFAS"
    cursor.execute(comando)
    tarefas = cursor.fetchall()

    tabela = table.Table(title= 'Tarefas', show_lines=True, row_styles=['none'], expand=True)
    tabela.add_column("ID", justify='center', style='cyan', no_wrap=True)
    tabela.add_column("Nome", justify='center', style='blue3')
    tabela.add_column("Estado", justify='center', style='yellow2')

    if tarefas:
        for tarefa in tarefas:
            tabela.add_row(f"{tarefa[0]}", f"{tarefa[1]}", f"{tarefa[2]}")  
    else:
        print("Não há tarefas a serem exibidas.")
    print(tabela)

    conexao.close()
   
def completeDb(id):
    conexao = sqlite3.connect('Tarefas.db')
    cursor = conexao.cursor()
    comando = f"SELECT * FROM Tarefas WHERE ID = {id} AND ESTADO = 'Não finalizada'"
    cursor.execute(comando)
    tarefa = cursor.fetchone()
    tarefaConcluida = tarefa[1] if tarefa else None
    if tarefa:
        comando = f"UPDATE TAREFAS SET ESTADO = 'Finalizada' WHERE ID = {id}"
        cursor.execute(comando)
        print(f"Estado da tarefa [blue bold uu]{tarefaConcluida}[/] alterado para 'Finalizada'.")
    else:
        print(f"Não foi possível encontrar a tarefa com o ID fornecido ou ela já está finalizada.")
    return tarefaConcluida
