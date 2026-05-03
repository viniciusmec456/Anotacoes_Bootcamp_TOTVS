opcao = "nulo"

while opcao != 7:

    texto = input("Digite sua string:")

    print("Escolha uma função:")
    print("1 - Deixar tudo minúsculo")
    print("2 - Deixar tudo em maiusculo")
    print("3 - Deixar em formato de Titulo")
    print("4 - Remover espaços em branco")
    print("5 - Centralizar")
    print("6 - Iterar caractere")
    print("7 - Sair")

    opcao = int(input("digite o número da opção desejada:"))


    if opcao == 1:
        print(texto.lower())

    if opcao == 2:
        print(texto.upper())

    if opcao == 3:
        print(texto.title())

    if opcao == 4:
        print(texto.strip())

    if opcao == 5:
        caractere = input("Digite o caractere:")
        print(texto.center(14,caractere))

    if opcao == 6:
        caractere = input("Digite o caractere:")
        print(caractere.join(texto))

   