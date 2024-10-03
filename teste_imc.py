
def calcula_imc (peso, altura):
    return peso * 100 / (altura * 2)

peso = eval(input("Digite o seu Peso (Kg): "))
altura = eval(input("Digite a Altura (Cm): "))

calcula_imc(peso, altura)
imc = calcula_imc(peso, altura)
print("Indice de Massa Corpórea de : ", imc)











