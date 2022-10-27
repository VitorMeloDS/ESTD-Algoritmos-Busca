import timeit
import random

minimo = 0
maximo = 10000000

qtd_de_vezes_repete_teste = 25

def valor_aleatorio_a_procurar():
  return random.randint(minimo,maximo*1.25)

def busca_binaria(uma_lista, item_pesquisado):
    if len(uma_lista) == 0: return False
    else:
        meio = len(uma_lista)//2
  
        if uma_lista[meio] == item_pesquisado: return True
        else:
            if item_pesquisado < uma_lista[meio]: return busca_binaria(uma_lista[:meio],item_pesquisado)
            else: return busca_binaria(uma_lista[meio+1:],item_pesquisado)

lista = list(range(50))

def funcao_realiza_teste():

  valor = valor_aleatorio_a_procurar() 
  resultado = busca_binaria(lista, valor)  
  print(f'procurando o valor {valor} na lista de tamanho {len(lista)} resultado -> {resultado}')

tempo = timeit.timeit( stmt=funcao_realiza_teste, number=qtd_de_vezes_repete_teste)

print(f'teste repetido {qtd_de_vezes_repete_teste} vezes')
print(f'tempo de duração do teste: {tempo}')
print(f'tempo médio de duração do teste: {tempo/qtd_de_vezes_repete_teste}')
