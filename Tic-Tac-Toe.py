# Игра "Крестики-Нолики" v1.0

from colorama import init

init()


def draw_play_field(x):
    print(f'\n   1  2  3')
    for i in range(len(x)):
        lf = line_format(x[i])
        print(f'{i + 1}', lf)
    print()


def line_format(x):
    s = ''
    for q in x:
        if q == '•':
            s = s + cr_bg + cr_grey + ' ' + cage_filler[0] + ' ' + cr_end
        elif q == 'X':
            s = s + cr_bg + cr_red + ' ' + cage_filler[1] + ' ' + cr_end
        elif q == 'O':
            s = s + cr_bg + cr_blue + ' ' + cage_filler[2] + ' ' + cr_end
    return s


def check_win(f):
    global win
    xo = [cage_filler[1], cage_filler[2]]
    xon = {xo[0]: player_name[0], xo[1]: player_name[1]}
    for i in xo:
        if f[0][0] == i and f[0][1] == i and f[0][2] == i:
            win = [True, xon[i]]
        elif f[1][0] == i and f[1][1] == i and f[1][2] == i:
            win = [True, xon[i]]
        elif f[2][0] == i and f[2][1] == i and f[2][2] == i:
            win = [True, xon[i]]
        elif f[0][0] == i and f[1][0] == i and f[2][0] == i:
            win = [True, xon[i]]
        elif f[0][1] == i and f[1][1] == i and f[2][1] == i:
            win = [True, xon[i]]
        elif f[0][2] == i and f[1][2] == i and f[2][2] == i:
            win = [True, xon[i]]
        elif f[0][0] == i and f[1][1] == i and f[2][2] == i:
            win = [True, xon[i]]
        elif f[2][0] == i and f[1][1] == i and f[0][2] == i:
            win = [True, xon[i]]


def victory_announce():
    draw_play_field(field)
    if not win[0]:
        print(f'{cr_yell}Игра закончена в Ничью!{cr_end}')
    else:
        print(f'{cr_yell}ПОБЕДА!!! Выигрывает "{win[1]}".{cr_end}')


cr_grey, cr_red, cr_bg, cr_end = '\033[90m', '\033[91m', '\033[40m', '\033[0m'
cr_green, cr_blue, cr_yell = '\033[92m', '\033[94m', '\033[93m'
cage_filler = ['•', 'X', 'O']
player_name = ['Крестик', 'Нолик']
player_color = [cr_red, cr_blue]
num_moves, max_moves = 1, 9
player = 1
text = ''
win = [False, '']
num_cell = [1, 2, 3]
field = [['•', '•', '•'], ['•', '•', '•'], ['•', '•', '•']]

while num_moves <= max_moves:
    if player > 2:
        player = 1
    draw_play_field(field)
    text = f'Сейчас ходит: {player_color[player - 1]}' \
           f'{cage_filler[player]}{cr_end} "{player_name[player - 1]}"'
    print(f'Ход #{num_moves} - {text}')
    mh, mv = map(int, input('Введите два числа через пробел для позиции '
                            'клетки по горизонтали и вертикали:\n').split())
    mh, mv = abs(mh), abs(mv)
    if mh not in num_cell or mv not in num_cell:
        print(f'\n{cr_green}Такой клетки на игровом поле нет! '
              f'Пожалуйста выберите клетку от 1-3 для хода:{cr_end}')
        continue
    nv, nh = mv - 1, mh - 1
    if field[nv][nh] == cage_filler[0]:
        field[nv][nh] = cage_filler[player]
    else:
        print(f'\n{cr_green}Эта клетка поля уже занята! '
              f'Пожалуйста выберите другую клетку для хода:{cr_end}')
        continue
    check_win(field)
    if win[0]:
        break
    player += 1
    num_moves += 1

victory_announce()
