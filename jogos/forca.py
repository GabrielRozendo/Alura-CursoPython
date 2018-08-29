import random

tamanho_tela = 50

class erros_obj():
    def __init__(self, erros, limite):
        self.erros = erros
        self.limite = limite
        
    def chances_erro(self):
        return self.limite - self.erros

    def enforcou(self):
        return self.erros == self.limite

def jogar():
    imprimir_cabecalho()    

    palavra_secreta, palavra_secreta_upper = carregar_palavra_secreta()

    chutes = []
    mascara = inicializar_mascara(palavra_secreta)
    enforcou = False
    acertou = False    
    erro_obj = erros_obj(0, 7)

    while(not erro_obj.enforcou() and not acertou):
        continuar, chute, chute_upper = pedir_chute(mascara, chutes, erro_obj.limite)
        if continuar:
            acertou, mascara = verificar_acerto(erro_obj, chute, chute_upper, palavra_secreta, palavra_secreta_upper, mascara)
        
    imprimir_resultado_cabecalho(palavra_secreta)
    if acertou:        
        imprimir_mensagem_acertou(chutes)
    elif enforcou:
        imprimir_mensagem_perdeu()
    imprimir_resultado_rodape()

def verificar_acerto(erro_obj, chute, chute_upper, palavra_secreta, palavra_secreta_upper, mascara):
    if chute_upper in palavra_secreta_upper:
        index = 0
        for letra in palavra_secreta_upper:
            if chute_upper == letra:
                print(f"Acertou. Letra '{chute}' na posição {index}")
                mascara[index] = palavra_secreta[index]
            index+=1
        acertou = not "_" in mascara
        return acertou, mascara
    else:
        erro_obj.erros+=1
        desenha_forca(erro_obj.erros)
        plural_vez = "vez" + ("es" if erro_obj.chances_erro() > 1 else "")
        print(f"Errou... Não tem '{chute}' na palavra. Você pode errar apenas mais {erro_obj.chances_erro()} {plural_vez}")        
        return False, mascara

def pedir_chute(mascara, chutes, erros_possiveis):
    print()
    print(f"Palavra: {''.join(mascara)}")
    chute = input(f"Tentativa {len(chutes)+1}!\tErros possíveis {erros_possiveis}\tDigite uma letra: ")
    chute = chute.strip()
    continuar, chute, chute_upper = validar_chute(chutes, chute)
    if not continuar:
        return False, chute, chute_upper
    else:
        chutes.append(chute_upper)
        return True, chute, chute_upper

def validar_chute(chutes, chute):
    if len(chute) < 1:
        print(f"É dificil digitar uma letra?! Tenta de novo aí né...")
        return False, chute, None
    elif len(chute) > 1:
        print(f"É dificil digitar só uma letra?! :/ vamos ignorar o restante: {chute[1:]}")
        chute = chute[0]
    chute_upper = chute.upper()

    if chute_upper in chutes:
        print(f"Você já chutou a letra '{chute}', me ajuda aí né... Quer perder uma tentativa assim fácil?")
        return False, chute, None

    return True, chute, chute_upper

def inicializar_mascara(palavra_secreta):
    return list("_" * len(palavra_secreta)) # "_" for letra in palavra_secreta

def carregar_palavra_secreta():
    palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio]

    return palavra_secreta, palavra_secreta.upper()

def imprimir_cabecalho():
    imprimir_linha()
    print("Bem vindo ao jogo da Forca!".center(tamanho_tela))
    imprimir_linha()
    print()

def imprimir_mensagem_perdeu():
    print("Você perdeu!".upper().center(tamanho_tela))
    print("Não desista, quem sabe na próxima...")
    print()
    imprimir_forca()

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(r" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (x)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprimir_trofeu():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_forca():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprimir_mensagem_acertou(chutes):
    print("Você ganhou!".upper().center(tamanho_tela))
    print("Parabéns, você é o máximo!")
    print(f"Você conseguiu em {len(chutes)} tentativas")
    if len(chutes)>= 9:
        print("Foi quase hein... haha")
    imprimir_trofeu()

def imprimir_resultado_rodape():
    print()
    imprimir_linha()
    print("Fim do jogo".center(tamanho_tela))

def imprimir_linha():
    print("*" * tamanho_tela)

def imprimir_resultado_cabecalho(palavra_secreta):
    print()
    print(palavra_secreta.upper().center(tamanho_tela))
    imprimir_linha()

if(__name__ == "__main__"):
    jogar()