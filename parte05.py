# ATVIDADE 05
nome = input("Digite o seu nome:")

string = str
inteiro = int
float = float
bool = bool 

if nome != string:
    print("O seu nome, ", nome, "foi regitrado como uma string.")
elif nome != inteiro:
    print("O seu nome, ", nome, "foi regitrado como um numero inteiro.")
elif nome != float:
    print("O seu nome, ", nome, "foi regitrado como um numero real.")
elif nome != bool:
    print("O seu nome, ", nome, "foi regitrado como uma variavel boolean.")
else:
    print("Termo não pode ser registrado pelo sistema.")