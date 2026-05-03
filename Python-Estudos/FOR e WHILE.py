texto = input("Insira o texto:")

vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")

print("final")


for numero in range(0,51,5):
    print(numero, end = " ") # O end serve para printar os valores na horizontal