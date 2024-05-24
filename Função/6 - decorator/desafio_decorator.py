'''
Crie um decorator que irá pegar a função que for passado para ele e imprimir o horário atual antes da executar a função e depois imprimir o horário após ter finalizado a execução da função
- Dica: você terá que usar o módulo datetime 
'''
from datetime import datetime
from time import sleep
import os


def monitorar_horario(funcao):
    def atendimento():
        print("Inicio de atendimento: ",
              datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
        funcao()
        sleep(30)
        print("Finalização de atendimento: ",
              datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    return atendimento


@monitorar_horario
def suporte_atendimento():
    print('Bem vindo ao Suporte Pythonista.' +
          os.linesep + 'Em que posso ajudá-lo(a)?')


suporte_atendimento()
