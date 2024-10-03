# Tuplas:
#São o mais próximo que temos de Registros (Registry em Java) em Python

tupla_heterogenea = (1, "olá", 3.14, [10,20,300], {'chave': 'valor'})

# Acessando e imprimindo elementos individuais da Tupla:
print(f'Integer: {tupla_heterogenea[0]}')
print(f'String: {tupla_heterogenea[1]}')
print(f'Float: {tupla_heterogenea[2]}')
print(f'List: {tupla_heterogenea[3]}')
print(f'Dict: {tupla_heterogenea[4]}')

#Modificando a lista dentro da Tupla:
tupla_heterogenea[3].append(40)
print(f'Lista modificada: {tupla_heterogenea[3]}')

#Acessando um valor no dicionário dentro de uma tupla:
valor_dict = tupla_heterogenea[4]['chave']
print(f'Valor no dicionário: {valor_dict}')

#imprimindo os elementos da Tupla e indicando seus tipos:
for elemento in tupla_heterogenea:
    print(f'Elemento: {elemento}, Tipo de Dado: {type(elemento)}')