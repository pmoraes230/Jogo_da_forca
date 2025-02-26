from palavras import palavra_aleatoria, categoria_aleatoria
from boneco import desenha_forca

def forca_jogo():
    letras_usuario = []
    chances = 6
    ganhou = False
    
    while True:
        desenha_forca(chances)
        for letras in palavra_aleatoria:
            if letras.lower() in letras_usuario:
                print(letras, end=" ")
            else:
                print("_", end=" ")
        print(f"\nVocê tem {chances} chances")
        tentativa = input(f"Adicione uma letra, Dica: a palavra é da categoria '{categoria_aleatoria}': ")
        letras_usuario.append(tentativa.lower())
        if tentativa.lower() not in palavra_aleatoria.lower():
            chances -= 1
        ganhou = True
        for letras in palavra_aleatoria:
            if letras.lower() not in letras_usuario:
                ganhou = False
                break
        if chances == 0 or ganhou:
            break
        
    desenha_forca(chances)
    print(f"Parabéns, você ganhou. A palavra era: {palavra_aleatoria}") if ganhou else print(f"Você perdeu. A palavra era: {palavra_aleatoria}")
    
forca_jogo()