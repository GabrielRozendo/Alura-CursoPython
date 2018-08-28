import random

def jogar():
    tamanho = 50
    print("*"*tamanho)
    print("Bem vindo ao jogo da Forca!".center(tamanho))
    print("*"*tamanho)
    print()

    palavras = []
    
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio]

    palavra_secreta_upper = palavra_secreta.upper()

    chutes = []
    mascara = list("_" * len(palavra_secreta)) # "_" for letra in palavra_secreta
    enforcou = False
    acertou = False
    chances = len(palavra_secreta) + 6

    while(not enforcou and not acertou):
        print()
        print(f"Palavra: {''.join(mascara)}")
        chute = input(f"Tentativa {len(chutes)+1} de {chances}!\tDigite uma letra: ")
        chute = chute.strip()
        
        if len(chute) < 1:
            print(f"É dificil digitar uma letra?! Tenta de novo aí né...")
            continue
        elif len(chute) > 1:
            print(f"É dificil digitar só uma letra?! :/ vamos ignorar o restante: {chute[1:]}")
            chute = chute[0]
        
        chute_upper = chute.upper()        
                
        if chute_upper in chutes:
            print(f"Você já chutou a letra '{chute}', me ajuda aí né... Quer perder uma tentativa assim fácil?")
            continue
        
        chutes.append(chute_upper)

        if chute_upper in palavra_secreta_upper:
            index = 0
            for letra in palavra_secreta_upper:
                if(chute_upper == letra):                    
                    print(f"Acertou. Letra '{chute}' na posição {index}")
                    mascara[index] = palavra_secreta[index]
                index+=1
            acertou = not "_" in mascara

        else:
            print(f"Errou... Não tem '{chute}' na palavra")

        enforcou = len(chutes) == chances
        
    print()
    print("*"*tamanho)
    if acertou:
        print("Você ganhou!".upper().center(tamanho))
        print("Parabéns, você é o máximo!")
        print(f"Você conseguiu em {len(chutes)} tentativas")
        if len(chutes)>= 9:
            print("Foi quase hein... haha")            
    elif enforcou:
        print("Você perdeu!".upper().center(tamanho))
        print("Não desista, quem sabe na próxima...")
    print()
    print("*"*tamanho)
    print("Fim do jogo".center(tamanho))


if(__name__ == "__main__"):
    jogar()


