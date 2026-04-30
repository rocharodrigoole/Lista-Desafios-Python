import time
import os


print(20*"=", "Nomes", 20*"=")

nome1 = input("Mede o seu primeiro nome: ")
sobre1 = input("Mede agora o sobrenome deste primeiro nome: ")

print("Ok, prosequimos")

nome2 = input("Mede um primeiro nome de outro individuo: ")
sobre2 = input("Mede o sbrenome deste outro nome: ")

for i in range(5,0, -1):
        time.sleep(1)
        os.system('cls')
        print(f'contagem regressiva...{i}')

print("Novos nomes-->", nome1, sobre2, " e", nome2, sobre1)

print(20*"=", "Fim do programa", 20*"=")