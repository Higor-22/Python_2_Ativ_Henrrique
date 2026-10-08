#Crie um programa que gerencie as notas de alunos combinando todos os conceitos
#estudados:
#• Crie um dicionário vazio chamado boletim.
#• Use um laço while para perguntar se o usuário deseja adicionar um aluno. Se sim,
#peça o nome do aluno e sua nota, armazenando no dicionário (nome como chave, nota
#como valor). Se não, encerre o laço.
#• Depois, use um laço for para percorrer o dicionário e imprimir uma mensagem
#dizendo se cada aluno está "Aprovado" (nota ≥ 6.0) ou "Reprovado" (nota < 6.0).


boletim = {}
lista_boletim = []

desejaadicionaraluno = input("Deseja adicionar alunos? S/N?")

while desejaadicionaraluno == "N" or "n":
    break

while desejaadicionaraluno == "S" or "s":
    
    Nome = input("Qual o nome do aluno que deseja adicionar? ")
    Nota = float(input("Qual a nota do aluno? "))
    
    boletim ["Nome"] = Nome
    boletim ["Nota"] = Nota
    
    for aluno in boletim:
     if aluno == "Nota":
      if boletim[aluno] >= 6.0:
        print("Aprovado")
   
      else:
        print("Reprovado")  
    
      lista_boletim.append(boletim.copy())
        
    sair = input("Deseja sair? S/N: ")
    if sair == "S" or "s":
      break 


for registro in lista_boletim:
    print(f"Aluno: {registro['Nome']} | Nota: {registro['Nota']}")