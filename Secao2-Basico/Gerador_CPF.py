from random import randint

def gera_primeiro_dig(n_range,cpf):
    soma = 0
    for p, n in enumerate(range(n_range, 1, -1)):
        soma += int(cpf[p]) * n

    gerado = 11 - (soma % 11)
    return gerado if gerado <= 9 else 0

#Gera 9 numeros aleatórios e depois só gera os 2 faltantes que vai ser um CPF valido
numero = str(randint(100000000,999999999))

novo_cpf = numero
primeiro = gera_primeiro_dig(10,novo_cpf)
novo_cpf += str(primeiro)
segundo = gera_primeiro_dig(11,novo_cpf)
novo_cpf += str(segundo)
print(novo_cpf)