import random
import string

Letras_M = string.ascii_letters
Letras_m = string.ascii_lowercase
Num = string.digits
caracteres_Espe = "!@#$%&*(){}^~_-"

Total = Letras_M + Letras_m + Num + caracteres_Espe

def gerador_alfanumerico(tamanho):
    senha = "".join(random.choice(Total) for _ in range(tamanho))
    return senha

continua = "S"
while continua == "S":
    tamanho = random.randint(10, 50)
    senha = gerador_alfanumerico(tamanho)
    print(f"Senha gerada: {senha}")
    continua = input("Quer gerar outra senha? S/N: ").upper()
