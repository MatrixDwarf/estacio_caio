#Criando um dicionário com Chave e Valor:


dicionario = {
    'nome': 'Karl Marx',
    'idade': 50,
    'cidade': 'USSR'
}

# Acessando e imprimindo valores individuais pela sua chave:
nome = dicionario ['nome']
idade = dicionario ['idade']
cidade = dicionario ['cidade']
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Localidade: {cidade}')

#Adicionando uma nova Chave-Valor ao dicionário :
dicionario["profissao"] = 'Filosofo'
print(f'Consigo adicionar Chave-Valor completamente novo ao dicionário {dicionario}')

#Modificando o valor associado á uma chave existente:
print(f'Ih, mas na vdd ele não tem {idade} anos')
dicionario['idade'] = 64
print(f'Na verdade é 64, observe: {dicionario}')

#Deletando | Apagando um par de Chave-Valor
del dicionario['cidade']
print(f'Os capitalistas nos roubaram, então não há informação de localizaçao do Karlinho: {dicionario}')

#Acessando todas as chaves e valores do dicionário;
chaves = dicionario.keys()
valores = dicionario.values()

print(f'Chaves: {list(chaves)}')
print(f'Valores: {list(valores)}')

#Assim como em listas,
#também é possível Iterar sobre Dicionários:
print("Iteração sobre um dicionário:")
for chave , valor in dicionario.items():
    print(f'{chave} : {valor}')

#Verificando se existe uma chave no dicionário:
if 'nome' in dicionario:
    print(f'O nome no dicionario é: {dicionario["nome"]}')
else:
    print("Não há chave 'nome' no dicionário!!")

#Usando o método get() para acesso aos valores de forma seguro
profissao = dicionario.get('profissao', "desconhecido")
print(f'Profissão: {profissao}')

#Limpando todos os elementos de um dicionário:
dicionario.clear()
print(f'Dicionário após Limpar todos os elementos: {dicionario}')
