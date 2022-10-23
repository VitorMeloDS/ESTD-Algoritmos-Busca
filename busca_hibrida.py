def busca_hibrida(uma_lista, item_pesquisado):
    encontrou = False; tamanho_lista = len(uma_lista); inicio=0; fim = len(uma_lista)-1
    
    if tamanho_lista == 0: return 'Lista vazia'
    elif tamanho_lista < 128:
        for i in uma_lista:
            if i == item_pesquisado: encontrou = True; break
            elif i > item_pesquisado: encontrou = False; break
            
        if encontrou == True: return 'Valor foi encontrado usando a busca sequencial ordenada'
        else: return 'Valor não foi encontrado ao utilizar a busca sequencial ordenada'
        
    else:
        while inicio <= fim and not encontrou:
            meio = (inicio + fim)//2
            if uma_lista[meio] == item_pesquisado: encontrou = True
            else:
                if item_pesquisado < uma_lista[meio]: fim = meio-1
                else: inicio = meio + 1
                    
        if encontrou == True: return 'Valor foi encontrado usando a busca binária'
        else: return 'Valor não foi encontrado ao utilizar a busca binária'

lista_teste = [i for i in range(128)]
print(busca_hibrida(lista_teste, 65))
