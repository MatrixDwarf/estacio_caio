"""Contagem Regressiva: Forma de se usar Funções Recursivas
(Função que chama outra função)"""

def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x -1)
    else:
        print('acabou')
regressiva(10)


"""Não Recursiva ↓ 
(não é uma função, só um algoritmo)"""

for i in range(10, -1, -1):
    print(i)
print("acabou")