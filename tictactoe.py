import math

def imprimir_tabuleiro(tabuleiro):
    #Imprime o tabuleiro

    for i in range(0, 9, 3):
        print(f" {tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]} ")
        if i < 6:
            print("-----------")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    #Verificador de vitoria 
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]

    for combo in combinacoes_vitoria:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    #Verifica se não existem mais jogadas a serem feitas
    return ' ' not in tabuleiro

def minimax(tabuleiro, profundidade, eh_maximizador):
    #Casos Base 
    if verificar_vitoria(tabuleiro, 'O'): 
        return 10 - profundidade #Prefere vitorias rápidas
    if verificar_vitoria(tabuleiro, 'X'): 
        return -10 + profundidade #Prefere derrotas lentas 
    if verificar_empate(tabuleiro):
        return 0

    #Logica de Maximização
    if eh_maximizador:
        melhor_pontuacao = -math.inf
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'O' # Simula jogada
                pontuacao = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ' ' # Desfaz jogada (Backtracking)
                melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

    #Lógica de Minimização 
    else:
        melhor_pontuacao = math.inf
        for i in range(9):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'X' # Simula jogada
                pontuacao = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ' ' # Desfaz jogada
                melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

def melhor_movimento_ia(tabuleiro):
    melhor_pontuacao = -math.inf
    melhor_movimento = None
    
    print("--- Raciocínio da IA (Logs) ---")
    
    for i in range(9):
        if tabuleiro[i] == ' ':
            # Simula o primeiro passo
            tabuleiro[i] = 'O'
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ' '
            
            print(f"Se jogar na posição {i}, pontuação estimada: {pontuacao}")
            
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = i
                
    print(f"--> Decisão Final: Posição {melhor_movimento}")
    print("-------------------------------")
    return melhor_movimento

#Loop Principal do Jogo
def jogar():
    tabuleiro = [' ' for _ in range(9)]
    humano = 'X'
    ia = 'O'
    
    print("Bem-vindo ao Jogo da Velha com Minimax!")
    print("Posições do tabuleiro: 0 a 8 (0 é superior esquerdo, 8 inferior direito)")
    imprimir_tabuleiro([str(i) for i in range(9)])
    print("Iniciando...\n")

    while True:
        #Turno do Jogador
        imprimir_tabuleiro(tabuleiro)
        try:
            move = int(input("Sua vez (X). Escolha uma posição (0-8): "))
            if tabuleiro[move] != ' ':
                print("Posição ocupada. Tente de novo.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Digite um número de 0 a 8.")
            continue
            
        tabuleiro[move] = humano

        if verificar_vitoria(tabuleiro, humano):
            imprimir_tabuleiro(tabuleiro)
            print("Você venceu! (Isso não deveria acontecer contra o Minimax perfeito...)")
            break
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        #Turno do NPC
        print("\nVez da IA (O)... Calculando...")
        move_ia = melhor_movimento_ia(tabuleiro)
        tabuleiro[move_ia] = ia

        if verificar_vitoria(tabuleiro, ia):
            imprimir_tabuleiro(tabuleiro)
            print("A IA venceu!")
            break
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

if __name__ == "__main__":
    jogar()