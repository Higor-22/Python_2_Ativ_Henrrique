#Crie um dicionário vazio. Peça ao usuário para digitar seu nome, telefone e e-mail.
#Armazene esses dados no dicionário usando chaves adequadas e, por fim, imprima o
#dicionário completo.

pessoa = {}
pessoa["nome"] = input("Digite seu nome: ")
pessoa["telefone"] = input("Digite seu telefone: ")
pessoa["e-mail"] = input("Digite seu e-mail: ")

print("Dicionário completo:", pessoa)