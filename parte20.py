import os
import time


os.system('cls')
print(30*">", "Valor absoluto", 30*"<")

vb = input("Mede um número para calcular o valor absoluto: ")

vb = float(vb)

for i in range(5,0, -1):
        time.sleep(1)
        os.system('cls')
        print(f'calculando...{i}')

if vb < 0:
        vb1 = vb * -1
        print("Valor absoluto --->", vb1)

else:
    vb1 = vb * 1
    print("Valor absoluto --->", vb1)