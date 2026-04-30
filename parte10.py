import time
import os

os.system('cls')

print(30*">", "Área do retangulo", 30*"<")

num1 = input("Mede a largura do retangulo para que possamos calcular o seu retangulo, ou o lado maior: ")
num2 = input("Mede agora o seu comprimento para finalizar o calculo, ou o lado menor: ")

num1 = float(num1)
num2 = float(num2)


for i in range(3,0, -1):
        time.sleep(1)
        os.system('cls')
        print(f'processando...{i}')


if num1 > num2:
        print("Esta forma é um retangulo")
        r = num1 * num2
        print("O resultado, logo a área do retângulo é --->", r)

else:
    print("Esta forma não e um retangulo")