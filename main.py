from os import system, name, _exit
from time import sleep

if __name__ == '__main__':

  clear = lambda: system('cls' if name == 'nt' else 'clear')
  clear()

  def apresentacao() -> bool:
    inicializador = input('\nPara iniciar o processo digite "start" e exit para encerrar: ')
    if inicializador == 'start':
      return True
    elif inicializador == 'search':
      print('\nNão há candidatos para procurar!'); sleep(2); clear(); apresentacao()
    elif inicializador == 'exit':
      return False
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!'); sleep(2); clear(); apresentacao()
      return True

  def search():
    pass
  

  def entradaDado():
    try:
      while True:
        nome = input('\nDigite o nome que deseja procurar: ').lower().strip()
        if nome == 'exit':
          _exit(0)
    except Exception as e:
      if e:
        print(e)
      print('\nComando não reconhecido, digite uns dos comando expecificados!')
      sleep(2); clear(); entradaDado()

  def main():
    try:
      if apresentacao():
        entradaDado()
    except Exception as e:
      print(e)

main()  
