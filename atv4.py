#Dada a lista numeros = [3, 8, 15, 22, 27, 34, 41, 50], use um laço for e uma
#estrutura condicional para criar uma nova lista contendo apenas os números pares.
#Imprima a nova lista ao final.


numeros = [3, 8, 15, 22, 27, 34, 41, 50]
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(numeros_pares)
    