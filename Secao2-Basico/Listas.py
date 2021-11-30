texto = 'valor'
lista = [1,2,3,4,'B','C']
lista2 = [3,7,8,12,33]
#Pulando valores
print(lista[::2])

#append
print(lista2)
lista2.append(22)
print(lista2)

#insert, inserrir em uma posição especifica
lista.insert(0,'asc')
print(lista)

#remover um elemento da lista
print(lista)
lista.pop(0)
print(lista)
del(lista[0:2])
print(lista)

#Criar uma lista
#O list interage em um list
l2 = list(range(1,10))
print(l2)



