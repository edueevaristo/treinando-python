import random

print("*********************************")
print("Bem vindo no jogo de Adivinhação")
print("*********************************", end="\n")

numero_secreto = random.randrange(1, 101)

total_de_tentativas = 0
rodada = 1

nivel_dificuldade = int(input("Qual será o nível de dificuldade? \n(1)Fácil (2)Médio (3)Difícil\nDigite aqui: "))

if nivel_dificuldade == 1:
    total_de_tentativas = 10
elif nivel_dificuldade == 2:
    total_de_tentativas = 5
else:
    total_de_tentativas = 3


while rodada <= total_de_tentativas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu número: ")
    print("Você digitou", chute)

    chute_int = int(chute)

    if chute_int < 1 or chute_int > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue

    # Validações de erros e acertos
    acertou = chute_int == numero_secreto
    maior = chute_int > numero_secreto
    menor = chute_int < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior que o número secreto. Tente um número mais baixo")
        elif menor:
            print("Você errou! O seu chute foi menor que o número secreto. Tente um número maior.")

    rodada = rodada + 1

print("Fim do jogo, o número secreto era {}".format(numero_secreto))
