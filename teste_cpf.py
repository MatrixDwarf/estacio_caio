# Função que recebe um CPF
def validar_cpf(cpf):
    """Removendo caracteres não núméricos"""
    cpf = ''.join(filter(str.isdigit, cpf))

    """Verificação se há 11 dígitos"""
    if len(cpf) != 11:
        return False

    """Verificando se todos os dígitos são iguais (no caso do CPF, não existe e é inválido)"""
    if cpf ==cpf[0] * 11:
        return False


    """Calculando o primeiro digito verificador"""
    soma = sum(int(cpf[i]) * (10 - i) for i in range (9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    """Verificando o primeiro digito verificador"""
    if int(cpf[9]) != digito_verificador_1:
        return False

    """Calculando o segundo digito verificador"""
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto


    """Verificando o segundo digito verificador"""
    if int(cpf[10]) != digito_verificador_2:
        return False

    # CPF inválido
    return True

"""Testando a função"""
cpf = "123.456.789-10"
if validar_cpf(cpf):
    print(f'O CPF {cpf} é Válido!')
else:
    print(f'O CPF {cpf} é Inválido!!!')
