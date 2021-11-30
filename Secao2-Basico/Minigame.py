secreta = 'perfume'
restante = 10
digitadas=[]
while restante > 0 :
    letra = input(f'Digite uma letra, tentativas restantes {restante}: ')
    digitadas.append(letra)
    if letra in secreta:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} não existe na palavra secreta')
        digitadas.pop()
    secreto_temporario=''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
    restante -= 1
    if secreto_temporario == secreta:
        print('Parabéns voce acertou a palavra secreta!!')
        break
    elif restante == 0:
        print('Que pena voce perdeu!!')