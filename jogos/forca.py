def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    palavra_secreta_upper = palavra_secreta.upper()
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        chute_upper = chute.upper()
        index = 0
        if chute_upper in palavra_secreta_upper:
            for letra in palavra_secreta_upper:
                if(chute_upper == letra):
                    print(f"Acertou. Letra '{chute}' na posição {index}")
                index+=1
        else:
            print(f"Errou... Não tem '{chute}' na palavra")
        # print("jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
