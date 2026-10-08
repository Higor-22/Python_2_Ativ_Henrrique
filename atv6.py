#Dado o dicionário notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}, use um laço for #para calcular a média geral da turma e imprimi-la.

notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}
soma = 0 

for alunos in notas:
    soma = soma + notas [alunos]
    media = soma/4
print(f"a média geral é {media}")