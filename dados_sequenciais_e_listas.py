# Lista com Alguns Elementos
lista = [10, 20, 30, 40, 50]

# Separando os elementos pelo seu índice
primeiro_elemento = lista[0]
segundo_elemento = lista[1]

# Imprimindo o seu conteudo dentro da lista, baseado em indice
print(f'O primeiro elemento da lista acima é o {primeiro_elemento}')
print(f'O segundo elemento da lista acima é o {segundo_elemento}')

# Adicionando um ítem á lista
print(f'Essa é a lista normal: {lista}')
lista.append(60)
print(f'Agora essa é a lista DEPOIS de usar o append: {lista}')

# Inserindo elemento em uma posição determinada e especificada pelo dev:
print(f'Aqui vai a lista: {lista}')
lista.insert(2, 25) #Aqui estarei inserindo no indice 2, o objeto 25
print(f'Agora veja essa laquera, usando o .insert: {lista}')

#Removendo um elemento de uma lista:
print(f'Vou fazer uma mágica: olha o número sumindo {lista}')
lista.remove(40)
print(f'Avada Kedabra sinsalabim CHUPIDAH: {lista} ta daaaaaa, que mágica coisa nenhuma, usei foi .remove')

#Removendo o ULTIMO elemento de uma lista:
print(f'Agora vou estar remocendo o último ítem dessa lista > {lista}')
lista.pop()
print(f'confere? {lista}')


#Acessando subgrupo | fatiamento de lista
sub_lista = lista [1:4]
print(f'Vamo fatiar essa lista: {lista}  | {sub_lista}')

#ordenação de lista:
lista.sort()
print(f'Bom, eu sei que já tá ordenada mas vai aqui a lista{lista}, devidamente ordenada')


# Iterando sobre os elementos da Lista:
print(f'Agora vou iterar sobre cada elemento da Lista, um á um > {lista}')
for elemento in lista:
    print(elemento)