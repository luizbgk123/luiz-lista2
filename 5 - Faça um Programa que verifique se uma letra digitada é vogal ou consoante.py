#5 - Faça um Programa que verifique se uma letra digitada é vogal ou
#consoante.

letra = input("Qual a letra que deseja saber: ")

if letra.lower() in ("a" , "e", "i", "o", "u"):
    print(f"A Letra {(letra)} é Vogal")
else:
    print(f"A Letra {(letra)} é conssoante")