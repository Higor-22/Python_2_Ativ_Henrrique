#Crie um programa que defina uma senha secreta, por exemplo "python123". Use um
#laço while que continue pedindo a senha ao usuário. O programa só deve parar e
#imprimir "Acesso Liberado" quando o usuário acertar a senha.

senha = "python123"
while True:
    entrada = input("Digite a senha: ")
    if entrada == senha:
        print("Acesso Liberado")
        break
    else:
        print("Senha incorreta. Tente novamente.")