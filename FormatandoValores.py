#Formatando valores em python

#Truncar valores
numero1 = 10
numero2 = 3
div = numero1/ numero2
print(f'{div:.2f}')


"""
:s para dizer que é string
:d Inteiros
:f Float
:.(Numero)f para truncar os valores
:(caracter)(> ou < ou ^)(Quantodade)(Tipo -s,d ou f)
"""
#Dizendo que isso é uma string
nome = 'Meu Nome'
print(f'{nome:s}')

#Preenchimento automatico, terá 10 casas esse numero (> esquerda) (< direita) (^ centralizado)
print(f'{numero1:0^10}')

#Formatar numero int como float
print(f'{numero1:.2f}')

#tambem funciona com letra
print(f'{nome:*^50}')

