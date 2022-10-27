import timeit
import random

minimo = 0
maximo = 10000000

qtd_de_vezes_repete_teste = 25

def valor_aleatorio_a_procurar():
  return random.randint(minimo,maximo*1.25)

def busca_sequencial(uma_lista, item_pesquisado):
    encontrou = False
    for i in uma_lista:
        if i == item_pesquisado: encontrou = True; break
        elif i > item_pesquisado: encontrou = False; break
  
    return encontrou
  
lista = list(range(maximo))

def funcao_realiza_teste():

  valor = valor_aleatorio_a_procurar() 
  resultado = busca_sequencial(lista, valor)  
  print(f'procurando o valor {valor} na lista de tamanho {len(lista)} resultado -> {resultado}')

tempo = timeit.timeit( stmt=funcao_realiza_teste, number=qtd_de_vezes_repete_teste)

print(f'teste repetido {qtd_de_vezes_repete_teste} vezes')
print(f'tempo de duração do teste: {tempo}')
print(f'tempo médio de duração do teste: {tempo/qtd_de_vezes_repete_teste}')