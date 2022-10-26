from os import system, name, _exit
from time import sleep


if __name__ == '__main__':

  clear = lambda: system('cls' if name == 'nt' else 'clear')
  clear()

  def apresentacao() -> bool:
    inicializador = input('\nPara iniciar o processo digite "start", para sair digite "exit": ').lower().strip()
    print('\nVerificar se um número está em uma lista ordenada.')
    if inicializador == 'start':
      return True
    elif inicializador == 'exit':
      return False
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!'); sleep(2); clear(); apresentacao()
      return True

  def busca_hibrida(uma_lista, item_pesquisado):
    encontrou = False; tamanho_lista = len(uma_lista)
    
    if tamanho_lista == 0: return 'Lista vazia'
    elif tamanho_lista < 128:
        for i in uma_lista:
            if i == item_pesquisado: encontrou = True; break
            elif i > item_pesquisado: encontrou = False; break
    
        return encontrou

    else:
        if len(uma_lista) == 0: return False
        else:
            meio = len(uma_lista)//2
            if uma_lista[meio] == item_pesquisado: return True
            else:
                if item_pesquisado < uma_lista[meio]: return busca_hibrida(uma_lista[:meio],item_pesquisado)
                else: return busca_hibrida(uma_lista[meio+1:],item_pesquisado)

  def entradaDado():
    try:
      while True:
        entrada = input('\nInfome o tamanho da lista e o elemento procurado respectivamente (separado por espaço): ').strip()
        if entrada == 'exit': _exit(0)
        else:
            entrada = entrada.split()
            if len(entrada) < 2 or len(entrada) > 2:
                print('\nValor inválido')
                sleep(2); clear(); entradaDado()
            else:
                qtd_lista = int(entrada[0])
                item_procurado = int(entrada[1])
                lista = [i for i in range(qtd_lista)]
                if busca_hibrida(lista, item_procurado): print('Valor encontrado')
                else: print('Valor não encontrado')
                
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
