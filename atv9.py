#Peça ao usuário para digitar uma palavra. Crie uma lista vazia e use um laço for para
#verificar cada letra da palavra. Se a letra for uma vogal (a, e, i, o, u), adicione-a à lista.
#Ao final, imprima a lista de vogais encontradas.

palavra = input("Digite uma palavra: ")
vogais = []

for i in palavra:
    if i in "aeiouAEIOU":
      vogais.append (i)
print(vogais)