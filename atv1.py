#EXERCÍCIO 1 Verificador de Números Conceitos: Condicional Crie um programa que peça um número inteiro ao usuário. O programa deve imprimir se o número é par ou ímpar.
#Dica: use o operador de módulo %.

n = int(input("Digite um numero:"))
if n % 2 == 0:
    print("Numero Par")
else:
    print("Numero Impar")
