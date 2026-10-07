#EXERCÍCIO 2 Contagem Regressiva
#Conceitos: Loop while
#Escreva um programa que use um laço while para imprimir uma contagem regressiva
#de 10 até 1. Ao final, imprima "Fogo!".

while contador >= 1:
        contador -= 1
        print(contador);
        
        if contador == 1:
            print("Fogo");
            break