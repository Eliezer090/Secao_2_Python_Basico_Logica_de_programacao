condicao = True
i = 0
# While
while condicao:
    nome = ''#input('Insirra seu nome: ')
    print(nome)
    i += 1
    if i == 2:
        condicao = False

i=0
while i < 5:
    i += 1
    if i==3:
        break
    print(i)


x = 0
y = 0
while x < 10:
    x += 1
    y = 0
    while y < 5:
        y += 1
        print(f'X vale: {x}, e Y vale: {y}')

#While com else

x = 0
y = 0
while x < 10:
    print(x)
    if x > 5:
        #Sew cair aqui nao executa o else
        break
    x += 1

else:
    print('Acabou')
print('fim')

#Percorrer a string
frase= 'a roupa roeu o rei de roma com ropa do rato'
tamanho_frase = len(frase)
i=0
while i < tamanho_frase:
    print(frase[i])
    i += 1

#FOR
for letra in frase:
    print(letra)

for numero in range(10):
    print(numero)

for numero in range(5,10):
    print(numero)
print('pula')
for numero in range(5,20, 2):
    print(numero)
print('Negativo')
for numero in range(10,5,-1):
    print(numero)

for letra in frase:
    if letra == 't':
        continue
    elif letra == 'd':
        break
    print(letra)
