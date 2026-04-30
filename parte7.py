import os

os.system('cls')

print(30*"=","Verificação", 30*"=" )

num1 = input("Mede um número para a verificação: ")
num2 = input("Mede um segundo número para a verificação: ")

num1 = float(num1)
num2 = float(num2)

os.system('cls')
if num2 < num1:
    print("Dado correto, autorizado!")
    print("Número 2 e menor que o primeiro")

else:
    print("Dado incorreto, não autorizado!")
    print("Número 2 e maior que o primeiro")

print(30*"=", "Fim da verificação", 30*"=")