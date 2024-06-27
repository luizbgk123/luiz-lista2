#9 - Faça um algoritmo que cadastre um usuário e uma senha em duas
#variáveis, o seu algoritmo deve validar para o usuário cadastrar somente
#senhas com mais de 8 caracteres, do contrário informar ao usuário do erro,
#usar função len para essa validação.

conta = input("\nCrie um Email: ")
senha = input("Digite uma senha numerica com 8 caracteres: ")
tamanhoSenha = len(senha)
print(tamanhoSenha)

if tamanhoSenha < 8:
    print("Sua senha não possui os caracteres necessarios")
else:
    print("td certo")