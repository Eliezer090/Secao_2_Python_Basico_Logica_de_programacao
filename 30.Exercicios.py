numero = input('Digite um numero inteiro: ')

try:
    if numero.isdigit():
        numero = int(numero)
        if numero % 2 == 0:
            print('Par')
        else:
            print('Impar')
    else:
        print('Não é numero')

except:
    print('Não é um numero inteiro ')


hora = input('Digite a hora atual: ')

try:
    hora = int(hora)
    if hora <= 11:
        print('Bom Dia')
    elif hora <= 17:
        print('Tarde')
    elif hora <= 23:
        print('Noite')
    else:
        print('Hora invalida')
except:
    print('Hora invalida')


nome = input('Seu nome ae parça: ')

try:
    len_nome = len(nome)
    if len_nome <= 4:
        print('Nome Curto')
    elif 5 >= len_nome or len_nome <= 6:
        print('Normal')
    else:
        print('Nome grande pacas em.')
except:
    print('Aii deu erro')





