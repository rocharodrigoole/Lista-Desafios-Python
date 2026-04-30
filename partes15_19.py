import os
import time
# Atividade 15: Produto e Desconto
num1 = input ("Digite o preço de um produto e iremos aplicar um desconto sobre ele: ")
num1 = float(num1)
resultado = num1 - (num1 * 0.1)

print (f'O seu preço era {num1} e com desconto seria: {resultado}')
time.sleep(2)
os.system('cls')
# Atividade 16: Taxa de Juros
cap = input (float("Bem vindo ao cálculo de Juros. Insira seu capital: "))
tax = input (float("Insira o valor da taxa de juros cobrada: "))
temp = input (int("Insire, em meses, o valor de tempo cobrado"))

resultado = cap + (tax * temp)

print (f'Você tem um montante de :', {resultado})
time.sleep(2)
os.system('cls')
# Atividade 17: Metros
meh = input (float("Bem vindo ao cálculo de metros. Insire quantos metros: "))

cmk = meh / 100
mml = meh / 10
kmd = meh * 100

print (f'Você inseriu: , {meh}, em cm seria {cmk}, em milímetros seria {mml} e em quilômetros seria {kmd}')
time.sleep(2)
os.system('cls')

# Atividade 18: Horas
hrs = input (int("Insire uma quantidade de horas e iremos transforma-las: "))
mins = hrs / 60

print (f'Temos: , {hrs}, e agora temos que seria {mins}')

# Atividade 19: Gasolina
gas = input (float("Insire a distância percorrida, na forma de combustível gasto, e iremos calcular a média de energia do veículo: "))
