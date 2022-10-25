def busca_hibrida(uma_lista, item_pesquisado):
    encontrou = False; tamanho_lista = len(uma_lista); inicio=0; fim = len(uma_lista)-1
    
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

lista_teste = [i for i in range(128)]
print(busca_hibrida(lista_teste, 65))
