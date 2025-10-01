import random

print("Давай сыграем в крестики-нолики!")
print()
print('Сначала выбери, кем хочешь играть. Для крестика X, для нолика 0')
vibor = input('Твой выбор: ').upper()

if vibor in ['X', '0']:
    print('Чтобы сделать ход, нажми на цифру, которая соответствует клетке!')
else:
    print("Некорректный выбор, по умолчанию выбираем X")
    vibor = 'X'

computer = "0" if vibor == "X" else "X" # если игрок X → компьютер O, и наоборот

game = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
    # все выигрышные комбинации
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
        (0, 4, 8), (2, 4, 6)              # диагонали
    ]
    for x, y, z in win_combinations:
        if board[x] == board[y] == board[z]:
            return board[x]   # возвращает 'X' или 'O'
    return None

print_board(game)

# переменная для игрока
player = vibor

for iteracija in range(9):
    if player == vibor:
        # ход игрока
        try:
            move = int(input(f"Ход {player}. Введи номер клетки: "))
        except ValueError:
            print("Нужно ввести число от 1 до 9!")
            continue
    elif player == computer:  # компьютер
        Parodija_na_GPT = [cell for cell in game if isinstance(cell, int)]
        move = random.choice(Parodija_na_GPT)
        print(f"Компьютер ({player}) походил в клетку {move}")

    if 1 <= move <= 9 and isinstance(game[move - 1], int):
        game[move - 1] = player
    else:
        print("Некорректный ход, попробуй снова.")
        continue

    print_board(game)

    winner = check_win(game)
    if winner:
        print(f"Победил игрок {winner}!")
        break

    # меняем игрока
    player = "0" if player == "X" else "X"

else:  # если цикл завершился без break
    print("Ничья!")