from os import system, name
from time import sleep
from random import randint


def print_legend():
    legend = {
        ".": "Casilla disponible",
        "#": "Nave aliada",
        "~": "Agua (intento fallido)",
        "X": "Nave destruida",
        "0-9": "Total barcos en fila y columna"
    }
    for k,v in legend.items():
        print(f"\t{k:^3} {v}")

def print_boards(personal_board: dict, atack_board: dict):
    board_1, board_2 = personal_board, atack_board
    numbers = "0 1 2 3 4 5 6"
    sep = " "*8
    print(f"\t{numbers:>15} {sep} {numbers:>15}")
    for i in range(6):
        label = "abcdef"[i]
        row_1 = " ".join(board_1[i])
        row_2 = " ".join(board_2[i])
        print(f"\t{label} {row_1} {sep} {label} {row_2}")
    print(f"\t{' Mi flota':^15} {sep} {' Ataques':^15}")


def show_game(personal_board: dict, atack_board: dict):
    titulo = f"\n\t{' BATTLESHIP ':=^40}"
    print(titulo)
    print_legend()
    print()
    print_boards(personal_board, atack_board)

def make_board():
    board = []
    for i in range(6):
        new_row = []
        for i in range(7):
            new_row.append(".")
        board.append(new_row)
    return board

def setup_myboard(board):
    i = 0
    while i < 6:
        r = randint(0, 5)
        c = randint(0, 6)
        if board[r][c] == ".":
            board[r][c] = "#"
            i += 1


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


if __name__ == "__main__":
    my_board = make_board()
    atack_board = make_board()

    salir = False
    while not salir:
        clear()
        setup_myboard(my_board)
        show_game(my_board, atack_board)
        o = input("\n\t> ")
        if o.lower() == "q": salir = True
        my_board = make_board()
