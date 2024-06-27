#8 - Faça um programa que peça o email e a senha para o usuário, o programa
#irá verificar se o usuário é igual a admin e a senha igual a 123, se sim mostrar
#usuário logado, se não informar se o usuário ou senha ou ambos estão
#incorretos.

conta = input("\nCrie um Email: ")
senha = int(input("Digite uma senha numerica: "))

EmailLogin = input("\nDigite seu Email: ")
SenhaLogin = int(input("Digite sua senha: "))

if EmailLogin == conta and SenhaLogin == senha:
    print("\nVocê está logado")

elif EmailLogin != conta and SenhaLogin != senha:
    print("\nAmbos estão incorretos")

elif EmailLogin != conta:
    print("\nOs Email estão incorretos")

elif SenhaLogin != senha:
    print("\nAs Senhas estão incorretos")
