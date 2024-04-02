tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def exibir_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(jogador):
    
    for i in range(3):
        if all(pos == jogador for pos in tabuleiro[i]) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

jogador_atual = "X"

while True:
    exibir_tabuleiro()
    jogada = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")
    if not jogada.isdigit() or int(jogada) < 1 or int(jogada) > 9:
        print("Posição inválida. Escolha um número de 1 a 9.")
        continue
    linha, coluna = divmod(int(jogada) - 1, 3)
    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada. Escolha outra posição.")
        continue
    tabuleiro[linha][coluna] = jogador_atual
    if verificar_vitoria(jogador_atual):
        exibir_tabuleiro()
        print(f"Jogador {jogador_atual} venceu!")
        break
    if all(pos != " " for linha in tabuleiro for pos in linha):
        exibir_tabuleiro()
        print("Empate! Ninguém venceu.")
        break
    jogador_atual = "O" if jogador_atual == "X" else "X"