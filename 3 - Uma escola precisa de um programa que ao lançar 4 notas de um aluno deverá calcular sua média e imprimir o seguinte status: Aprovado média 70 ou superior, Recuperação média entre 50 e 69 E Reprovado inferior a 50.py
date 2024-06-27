#3 - Uma escola precisa de um programa que ao lançar 4 notas de um aluno
#deverá calcular sua média e imprimir o seguinte status: Aprovado média 70
#ou superior, Recuperação média entre 50 e 69 E Reprovado inferior a 50.

nota1 = int(input("\nQual sua primeira nota: "))
nota2 = int(input("Qual sua segunda nota: "))
nota3 = int(input("Qual sua terceira nota: "))
nota4 = int(input("Qual sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print (f"{media}")

if media >= 70:
    print("Aprovado")
if media == 50 and media <= 69:
    print("Você está de recuperação")
elif media < 50:
    print("Reprovado")
