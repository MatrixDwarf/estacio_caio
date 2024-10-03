# FORmas - Forma de se usar o FOR

for item in range (2,9,3):
    print(item)


#nome = input("Entre com o seu nome: ")
#for letra in nome:
#    print(letra)

nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)


numeros = [1,2,3,4,5]
for numero in numeros:
    quadrado = numero ** 2
    print(f'O quadrado de {numero} é {quadrado}')


numeros = [1,2,3,4,5]
soma = 0
for numero in numeros:
    soma += numero
print(f'A soma de todos os números é {soma}')


texto = "programação"
letra_contando = "r"
contador = 0

for letra in texto:
    if letra == letra_contando:
        contador += 1

print(f'A letra "{letra_contando}" aparece {contador} vezes na palavra "{texto}"')
