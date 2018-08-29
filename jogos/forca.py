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

class palavra_secreta_obj():
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.palavra_secreta_upper = palavra_secreta.upper()
        self.mascara = inicializar_mascara(palavra_secreta)
        
    def mascara_str(self):
        return ' '.join(self.mascara)

    def atualizar_mascara(self, index):
        self.mascara[index] = self.palavra_secreta[index]

    def acertou(self):
        return not "_" in self.mascara


def jogar():
    imprimir_cabecalho()    

    palavra_secreta_obj = carregar_palavra_secreta()

    chutes = []
    acertou = False    
    erro_obj = erros_obj(0, 7)

    while(not erro_obj.enforcou() and not acertou):
        continuar, chute, chute_upper = pedir_chute(palavra_secreta_obj.mascara_str(), chutes, erro_obj)
        if continuar:
            acertou = verificar_acerto(erro_obj, chute, chute_upper, palavra_secreta_obj)
        
    imprimir_resultado_cabecalho(palavra_secreta_obj.palavra_secreta)
    if acertou:        
        imprimir_mensagem_acertou(chutes, erro_obj.erros)
    elif erro_obj.enforcou():
        imprimir_mensagem_perdeu(len(chutes) == erro_obj.erros)
    imprimir_resultado_rodape()

def verificar_acerto(erro_obj, chute, chute_upper, palavra_secreta_obj):
    if chute_upper in palavra_secreta_obj.palavra_secreta_upper:
        # desenhar_forca(erro_obj.erros)
        index = 0
        for letra in palavra_secreta_obj.palavra_secreta_upper:
            if chute_upper == letra:
                print(f"Acertou. Letra '{chute}' na posição {index}")
                palavra_secreta_obj.atualizar_mascara(index)
            index+=1
        return palavra_secreta_obj.acertou()
    else:
        erro_obj.erros+=1
        # desenhar_forca(erro_obj.erros)
        plural_vez = "vez" + ("es" if erro_obj.chances_erro() > 1 else "")
        complemento_msg = f" Você pode errar apenas mais {erro_obj.chances_erro()} {plural_vez}" if erro_obj.chances_erro() > 0 else ""
        print()
        print(f"Errou... Não tem '{chute}' na palavra."+complemento_msg)        
        return False

def pedir_chute(mascara, chutes, erros_obj):
    print()
    desenhar_forca(erros_obj.erros)
    print(f"Palavra: {mascara}")
    chute = input(f"Tentativa {len(chutes)+1}!\tErros possíveis {erros_obj.chances_erro()}\tDigite uma letra: ")
    print()
    chute = chute.strip()
    continuar, chute, chute_upper = validar_chute(chutes, chute)
    if not continuar:
        return False, chute, chute_upper
    else:
        chutes.append(chute_upper)
        return True, chute, chute_upper

def validar_chute(chutes, chute):
    if len(chute) < 1:
        print(f"É dificil digitar uma letra?! 😒 Tenta de novo aí né...")
        return False, chute, None
    elif len(chute) > 1:
        print(f"É dificil digitar só uma letra?! :/ 😡 vamos ignorar o restante: {chute[1:]}")
        chute = chute[0]

    if not chute.isalpha():
        print("Só letras, blz? Tenta de novo aí que dessa vez não vou arrancar sua cabeça... 😇")
        return False, chute, None

    chute_upper = chute.upper()

    if chute_upper in chutes:
        print(f"Você já chutou a letra '{chute}', me ajuda aí né... 🤦‍ Quer perder uma tentativa assim fácil?")
        return False, chute, None

    return True, chute, chute_upper

def inicializar_mascara(palavra_secreta):
    return list("_" * len(palavra_secreta)) # "_" for letra in palavra_secreta

def carregar_palavra_secreta(nome_arquivo = "palavras.txt"):
    palavras = []

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero_aleatorio = random.randrange(0, len(palavras))
    return palavra_secreta_obj(palavras[numero_aleatorio])

def imprimir_cabecalho():
    imprimir_linha()
    print("Bem vindo ao jogo da Forca!".center(tamanho_tela))
    imprimir_linha()
    print()

def imprimir_mensagem_perdeu(errou_tudo):
    print("⚰️ Você perdeu! ☠️".upper().center(tamanho_tela))
    if errou_tudo:
        print("Poxa, mas também você não acertou nenhuma né...")
    else:
        print("Não desista, quem sabe na próxima...")
    print()
    imprimir_caveira()

def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    print(" |      {}   ".format("   " if erros ==0 else "(x)" if erros == 7 else "(_)"))
    print(" |      {1}{0}{2}   ".format(
                                    "|" if erros >= 2 else " ",
                                    "\\" if erros >= 3 else " ",
                                    "/" if erros >= 4 else " "))
    print(" |       {}    ".format("|" if erros >= 5 else " "))
    print(" |      {} {}     ".format(
                                    "/" if erros >= 6 else " ",
                                    "\\" if erros == 7 else " "))
    print("_|" + "_" * 12)
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

def imprimir_caveira():
    print(r"    _______________         ")
    print(r"   /               \       ")
    print(r"  /                 \      ")
    print(r"//                   \/\  ")
    print(r"\|   XXXX     XXXX   | /   ")
    print(r" |   XXXX     XXXX   |/     ")
    print(r" |   XXX       XXX   |      ")
    print(r" |                   |      ")
    print(r" \__      XXX      __/     ")
    print(r"   |\     XXX     /|       ")
    print(r"   | |           | |        ")
    print(r"   | I I I I I I I |        ")
    print(r"   |  I I I I I I  |        ")
    print(r"   \_             _/       ")
    print(r"     \_         _/         ")
    print(r"       \_______/           ")


def imprimir_mensagem_acertou(chutes, erros):
    print("🏆 Você ganhou! 👏".upper().center(tamanho_tela))
    print("Parabéns, você é o máximo!")
    print(f"Você conseguiu em {len(chutes)} tentativas")
    if erros <= 1:
        print("Foi quase hein... última chance haha")
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