# for num in range (1000,10000):
#     menor = num % 100 #obtém os algarismos menos significativos | divisão resto
#     maior = num // 100 #aqui são os mais significativos | divisao inteira
#     raiz = menor +  maior
#
#     if(raiz * raiz) == num: #valida se a raiz gera o número testado
#         print(num)
#         print(menor)
#         print(maior)
#         print(raiz)
# print("Terminou")
# print('saiu ',  num)

for raiz in range (32,100):
    num = raiz * raiz
    menor = num % 100
    maior = num // 100

    if(raiz * raiz) == num: #valida se a raiz gera o número testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("Terminou")
print('saiu ',  num)




