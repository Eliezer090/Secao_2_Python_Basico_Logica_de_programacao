
texto = 'O brasil é o , pais bom, sem corrupção'
split = texto.split(',')
print(len(split))


join = ','.join(split)
print(join)

for indice, valor in enumerate(split):
    print(indice, valor)

lista = [
    [0,'maria'],
    [1,'joao'],
    [5,'alguem']
]
#sem o enumerate o valor numerico ele assume como indice
for indice,nome in lista:
    print(indice,nome)

lista2 = ['luiz','maria']

n1,n2=lista2

print(n1)

print('---------Desempacotando--------')
#Desempacotando listas
listaD = ['luiz','maria','eduardo']

for lista in listaD:
    print(lista)

print('-----Ultimo(s) valor----')
*lista, ultimo_valor = listaD

print(lista,ultimo_valor)

#*_ nao querro esses valores nao me interessa
*_, n2,n3 = listaD
print(n2,n3)