#Peça ao usuário para digitar um número de 1 a 10. Use um laço for para imprimir a
#tabuada desse número, multiplicando-o de 1 a 10.


num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')