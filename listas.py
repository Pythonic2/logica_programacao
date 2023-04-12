# mias sobre listas



#nome_da_lista = [      ['banana','manga','goiaba'],        [10,20,30,40,89,[2,4,6]  ],        [1.7]       ]

# concatenar = unir +
#
# lista2 = ['tatiane']
#
# lista3 = nome_da_lista + lista2
#### metodos de listas ####

lista = [2,4,6,8,10]

print(lista)
lista.append(0) # adiciona o valor ao ultimo item da lista

lista.insert(4, 5) # insert(position, value) position é onde eu quero inserir , value
print(lista)

lista.pop()#remove o ultimo item da lista
print(lista)
lista.append(2)

lista.remove(6) # remove o valor da lista
print(lista)

print(lista.count(2)) # quantas ocorrencias do numero aparece na lista
chamar = sorted(lista)
print(chamar)

