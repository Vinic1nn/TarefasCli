#! TarefasCli\commands\commands.py

from typer import Typer, Option, Exit, Argument, Context
from typing_extensions import Annotated
from rich import print, rule
from Dbconfig import addDb, removeDb, listDb, completeDb


app  = Typer()

__version__ = '0.1.0'

def version(arg):
  if arg:
    print(__version__)
    raise Exit(code=0)

#Callback do invocação sem comando e version
@app.callback(invoke_without_command=True)
def callback(
    ctx : Context,
    version: bool = Option(False,
        '-v', '--version', 
        callback= version,
        is_eager=True,
        is_flag=True,
        help="Fala a versão atual do programa.")):
    if ctx.invoked_subcommand:
        return
    print("""
                   Bem vindos ao [blink b reverse] TarefasCLI [/]
      Comand Line Interface desenvolvido por [red bold i] Vinic1nn [/] !!!
        """)
    
    print("                 [uu]Comandos disponíveis:[/uu]\n\n             [b]add[/] - [b]remove[/] - [b]list[/] - [b]complete[/] \n")
    print('                 [uu]Mais duvidas digite:[/uu]\n\n                       [green][b]--help[/][/green]\n ')
    
#Comando add
@app.command(name = 'add')
def addTarefa(tarefa: str = Argument(help= 'Adiciona uma tarefa.', metavar='"Limpar_Casa"')):
    addDb(tarefa)
    print(f'Tarefa adicionada: [green][b]{tarefa}[/b][/green] ')
    
 
       
#Comando remove
@app.command(name= 'remove')
def removeTarefa(id: str = Argument(help= 'Informe o ID de uma tarefa para ser removido', metavar= "1")):
    itemRemovido=removeDb(id)
    print(f'Tarefa removida: [red][b]{itemRemovido}[/b][/red] ')
    
#Comando list
@app.command(name= 'list')
def listTarefa(inco: Annotated[bool, Option(help="Mostra apenas as tarefas incompletas.")] = False,
               comp: Annotated[bool, Option(help="Mostra apenas as tarefas completas.")] = False,
               help= 'Mostra a lista de tarefas.'):
    
    if inco: 
        print('Tarefas incompletas')
    elif comp:
        print('Tarefas completas')
    else:
       listDb()
   
#Comando Complete 
@app.command(name='complete')
def completeTarefa(tarefa: int = Argument(help= 'Digite o número de ID da tarefa', metavar= "Id da tarefa")):
    completeDb(tarefa)




if __name__ == "__main__":
    app()