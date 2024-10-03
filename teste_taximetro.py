def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1


    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia + km_rodado) + multiplicador
    return valor

dist = eval(input("Distancia á ser percorrida (Km): "))
pagamento = taximetro(dist)
print(f'O valor á ser pago é de R$ {pagamento}')








# def taximetro(distancia, multiplicador = 1):
#     largada = 3
#     km_rodados = 2
#     valor = (largada + distancia + km_rodados) * multiplicador
#     return valor
#
#
# pagamento = taximetro(3.5, 2)
# print(pagamento)
#
