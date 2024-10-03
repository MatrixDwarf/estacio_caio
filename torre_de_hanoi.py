# Usando Recursividade para montar uma Torre de Hanoi
from turtledemo.minimal_hanoi import hanoi


def mover_disco(origem, destino):
    disco = origem.pop()
    destino.append(disco)

def monta_torres(torre_A, torre_B, torre_C):
    print('A: ', torre_A)
    print('B: ', torre_B)
    print('C: ', torre_C)
    print()

# Aqui vou montar a parte recursiva do mesmo código acima

def hanoi_recursivo(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        mover_disco(origem, destino)
        monta_torres(torre_A, torre_B, torre_C)
    else:
        hanoi_recursivo(num_discos - 1, origem, auxiliar, destino)
        mover_disco(origem, destino)
        monta_torres(torre_A, torre_B, torre_C)
        hanoi_recursivo(num_discos - 1, auxiliar, destino, origem)


# Resolvendo o problema recursivamente
num_discos = 3
# Inicializando a torre e os discos
torre_A = list(range(num_discos, 0, -1))
torre_B = []
torre_C = []

# Mostrando o estado inicial
monta_torres(torre_A, torre_B, torre_C)
hanoi_recursivo(num_discos, torre_A,torre_C, torre_B)