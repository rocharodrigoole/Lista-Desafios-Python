# ATIVIDADE 01
num1 = input (int('Digite o primeiro numero: ')) 
num2 = input (int('Digite o segundo numero: '))

resultado = num2 / num1

if num1 !=0 and num2 !=0 and resultado > 10 and resultado < 100 :
    print(f'{num1} / {num2} = {resultado}')
else:
    print("Invalido!")
