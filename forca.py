import random

tamanho_tela = 50

class erros_obj():
    """Classe para tratar os chutes errados"""
    def __init__(self, erros, limite):
        self.erros = erros
        self.limite = limite
    
    @property
    def chances_erro(self):
        """Quantidade de erros possíveis antes de ser enforcado"""
        return self.limite - self.erros

    @property
    def enforcou(self):
        """Verifica se foi enforcado pela quantidade de erros cometidos"""
        return self.erros == self.limite

class palavra_secreta_obj():
    """Classe para tratar a palavra secreta da forca"""
    def __init__(self, palavra_secreta):
        """Inicializa o objeto informando a palavra a ser descoberta"""
        self.palavra_secreta = palavra_secreta
        self.palavra_secreta_upper = palavra_secreta.upper()
        self.mascara = inicializar_mascara(palavra_secreta)
    
    @property
    def mascara_str(self):
        """Retorna a mascara em formato de impressão na tela"""
        return ' '.join(self.mascara)

    def atualizar_mascara(self, index):
        """Atualiza a máscara exibindo as letras já descobertas"""
        self.mascara[index] = self.palavra_secreta[index]

    @property
    def acertou(self):
        """Verifica se acertou todas as letras"""
        return not "_" in self.mascara


class chutes_obj():
    """Classe dos chutes"""
    def __init__(self):
        """Inicializa o objeto chute"""
        self.chutes = []
        self._chute = None
        self.chupe_upper = None

    @property
    def chute(self):
        """Retorna o último chute (atual)"""
        return self._chute

    @chute.setter
    def chute(self, value):
        """Atribuí um valor ao chute
        Já atualiza a versão em maiscúlo e também adiciona à lista"""
        if value:
            self._chute = value
            self.chute_upper = value.upper()
            self.chutes.append(value)

    @property
    def quantidade_chutes(self):
        """A quantidade de chutes válidos já realizados"""
        return len(self.chutes)

    @property
    def tentativa(self):
        """Exibe a tentativa em questão"""
        return f"Tentativa {self.quantidade_chutes+1}!"
    
    def existe(self, chute):
        """Verifica se a letra já foi chutada antes"""
        return chute in self.chutes or chute.upper() in self.chutes

def jogar():
    imprimir_cabecalho()    

    acertou = False    
    palavra_secreta_obj = carregar_palavra_secreta()
    erro_obj = erros_obj(0, 7)
    chute_obj = chutes_obj()

    while(not erro_obj.enforcou and not acertou):
        if pedir_chute(palavra_secreta_obj.mascara_str, erro_obj, chute_obj):
            acertou = verificar_acerto(erro_obj, chute_obj, palavra_secreta_obj)
    
    desenhar_forca(erro_obj.erros)
    imprimir_resultado_cabecalho(palavra_secreta_obj.palavra_secreta)
    if acertou:        
        imprimir_mensagem_acertou(erro_obj, chute_obj.quantidade_chutes)
    elif erro_obj.enforcou:
        imprimir_mensagem_perdeu(chute_obj.quantidade_chutes == erro_obj.erros)
    imprimir_resultado_rodape()

def verificar_acerto(erro_obj, chute_obj, palavra_secreta_obj):
    if chute_obj.chute_upper in palavra_secreta_obj.palavra_secreta_upper:
        # desenhar_forca(erro_obj.erros)
        index = 0
        for letra in palavra_secreta_obj.palavra_secreta_upper:
            if chute_obj.chute_upper == letra:
                print(f"Acertou. Letra '{chute_obj.chute}' na posição {index}")
                palavra_secreta_obj.atualizar_mascara(index)
            index+=1
        return palavra_secreta_obj.acertou
    else:
        erro_obj.erros+=1
        # desenhar_forca(erro_obj.erros)
        plural_vez = "vez" + ("es" if erro_obj.chances_erro > 1 else "")
        complemento_msg = f" Você pode errar apenas mais {erro_obj.chances_erro} {plural_vez}" if erro_obj.chances_erro > 0 else ""
        print()
        print(f"Errou... Não tem '{chute_obj.chute}' na palavra."+complemento_msg)        
        return False

def pedir_chute(mascara, erros_obj, chute_obj):
    print()
    desenhar_forca(erros_obj.erros)
    print(f"Palavra: {mascara}")
    chute_usuario = input(f"{chute_obj.tentativa}\tErros possíveis {erros_obj.chances_erro}\tDigite uma letra: ")
    print()
    return validar_chute(chute_obj, chute_usuario.strip())

def validar_chute(chute_obj, chute_usuario):
    if len(chute_usuario) < 1:
        print(f"É dificil digitar uma letra?! 😒 Tenta de novo aí né...")
        return False
    elif len(chute_usuario) > 1:
        print(f"É dificil digitar só uma letra?! :/ 😡 vamos ignorar o restante: {chute_usuario[1:]}")
        chute_usuario = chute_usuario[0]

    if not chute_usuario.isalpha():
        print("Só letras, blz? Tenta de novo aí que dessa vez não vou arrancar sua cabeça... 😇")
        return False

    if chute_obj.existe(chute_usuario):
        print(f"Você já chutou a letra '{chute_usuario}', me ajuda aí né... 🤦‍ Quer perder uma tentativa assim fácil?")
        return False
    else:
        chute_obj.chute = chute_usuario
        return True

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
    print("       ___________      ".center(tamanho_tela))
    print("      '._==_==_=_.'     ".center(tamanho_tela))
    print("      .-\\:      /-.    ".center(tamanho_tela))
    print("     | (|:.     |) |    ".center(tamanho_tela))
    print("      '-|:.     |-'     ".center(tamanho_tela))
    print("        \\::.    /      ".center(tamanho_tela))
    print("         '::. .'        ".center(tamanho_tela))
    print("           ) (          ".center(tamanho_tela))
    print("         _.' '._        ".center(tamanho_tela))
    print("        '-------'       ".center(tamanho_tela))

def imprimir_caveira():
    print(r"      _______________        ".center(tamanho_tela))
    print(r"     /               \       ".center(tamanho_tela))
    print(r"    /                 \      ".center(tamanho_tela))
    print(r" /\/                   \/\   ".center(tamanho_tela))
    print(r" \ |   XXXX     XXXX   | /   ".center(tamanho_tela))
    print(r"  \|   XXXX     XXXX   |/    ".center(tamanho_tela))
    print(r"   |   XXX       XXX   |     ".center(tamanho_tela))
    print(r"   |                   |     ".center(tamanho_tela))
    print(r"   \__      XXX      __/     ".center(tamanho_tela))
    print(r"     |\     XXX     /|       ".center(tamanho_tela))
    print(r"     | |           | |       ".center(tamanho_tela))
    print(r"     | I I I I I I I |       ".center(tamanho_tela))
    print(r"     |  I I I I I I  |       ".center(tamanho_tela))
    print(r"     \_             _/       ".center(tamanho_tela))
    print(r"       \_         _/         ".center(tamanho_tela))
    print(r"         \_______/           ".center(tamanho_tela))


def imprimir_mensagem_acertou(erros_obj, quantidade_chutes):
    print("🏆 Você ganhou! 👏".upper().center(tamanho_tela))
    print("Parabéns, você é o máximo!")
    print(f"Você conseguiu em {quantidade_chutes} tentativas")
    if erros_obj.erros == 0:
        print("Você foi perfeito, não errou uma sequer! Que isso hein!")
    elif erros_obj.erros == erros_obj.limite - 1:
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