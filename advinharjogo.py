from random import choice


lista = ["laranja","carro","foguete"]
escolha = choice(lista)

if escolha == "laranja":
    print("="*10)
    print("Dicas")
    print("Dica 1- é uma fruta")
    print("Dica 2- Pode ser azeda ou doce")
    user = input("Qual é a palavra? ")
    if user == escolha:
        print("Parabens! Voce acertou")
        print("Pressione qualquer tecla para sair...")
        input()
    else:
        print("Voce errou, tente novamente")
        print("Pressione qualquer tecla para sair...")
        input()

elif escolha == "carro":
    print("="*10)
    print("Dicas")
    print("Dica 1- é veiculo")
    print("Dica 2- ele tem rodas")
    user = input("Qual é a palavra? ")
    if user == escolha:
        print("Parabens! Voce acertou")
        print("Pressione qualquer tecla para sair...")
        input()
    else:
        print("Voce errou, tente novamente")
        print("Pressione qualquer tecla para sair...")
        input()
else:
    print("="*10)
    print("Dicas")
    print("Dica 1- é um veiculo")
    print("Dica 2- ele voa")
    user = input("Qual é a palavra? ")
    if user == escolha:
        print("Parabens! Voce acertou")
        print("Pressione qualquer tecla para sair...")
        input()
    else:
        print("Voce errou, tente novamente")
        print("Pressione qualquer tecla para sair...")
        input()