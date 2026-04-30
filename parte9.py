import os
import time


os.system('cls')
print(10*"-", "Metades", 10*"-")

num1 = input("Mede um número para que possamos tirar a metade dele: ")

num1 = float(num1)

metade = num1/2

for i in range(3,0, -1):
        time.sleep(1)
        os.system('cls')
        print(f'calculando...{i}')


print("A metade do número que você me deu", num1 ,"é --->", metade)

print(10*"-", "Fim do programa", 10*"-")