import pygame
from .constants import CELL_NUM, CELL_SIZE, SPACE, C_LOC


def draw_chessboard(screen: object, color: tuple, chess_arr: list) -> None:

    for i in range(CELL_NUM):
        width = 3 if i == 0 or i == CELL_NUM - 1 else 1
        pygame.draw.line(screen, color, (i*CELL_SIZE+SPACE, SPACE),
                         (i*CELL_SIZE+SPACE, SPACE+(CELL_NUM-1)*CELL_SIZE), width)
        pygame.draw.line(screen, color, (SPACE, SPACE+i*CELL_SIZE),
                         (SPACE+(CELL_NUM-1)*CELL_SIZE, SPACE+i*CELL_SIZE), width)

    for x, y in C_LOC:
        pygame.draw.circle(screen, color,
                           (SPACE+x*CELL_SIZE, SPACE+y*CELL_SIZE), 4, 4)

    for x, y, c in chess_arr:
        chess_color = (30, 30, 30) if c == 1 else (205, 205, 205)
        pygame.draw.circle(screen, chess_color,
                           (x*CELL_SIZE+SPACE, y*CELL_SIZE+SPACE), 12, 12)


def mouse_operation(game_state: int, chess_arr: list, flag: int) -> tuple:

    if game_state != 1:

        return (game_state, flag)

    x, y = pygame.mouse.get_pos()

    x = int(round((x-SPACE)*1.0/CELL_SIZE))
    y = int(round((y-SPACE)*1.0/CELL_SIZE))
    if 0 <= x < CELL_NUM and 0 <= y < CELL_NUM and (x, y, 1) not in chess_arr and (x, y, 2) not in chess_arr:
        chess_arr.append((x, y, flag))
        if check_win(chess_arr, flag):

            return (2 if flag == 1 else 3, flag)
        else:

            return (game_state, 2 if flag == 1 else 1)
    else:
        return (game_state, flag)


def check_win(chess_arr: list, flag: int) -> bool:

    m = [[0]*CELL_NUM for _ in range(CELL_NUM)]
    for x, y, c in chess_arr:
        if c == flag:
            m[y][x] = 1
    lx = chess_arr[-1][0]
    ly = chess_arr[-1][1]

    dire_arr = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)],
                [(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]

    for dire1, dire2 in dire_arr:
        num1 = get_num(lx, ly, dire1, m)
        num2 = get_num(lx, ly, dire2, m)
        if num1 + num2 >= 4:
            return True
    return False


def get_num(x: int, y: int, dire: tuple, board: list) -> int:

    t_x, t_y = x, y
    dire_x, dire_y = dire
    ret = 0
    while True:
        t_x += dire_x
        t_y += dire_y
        if t_x < 0 or t_x >= CELL_NUM or t_y < 0 or t_y >= CELL_NUM or board[t_y][t_x] == 0:
            return ret
        ret += 1


def draw_script(flag: int, screen, game_state: int) -> None:

    text = "BLACK" if flag == 1 else "WHITE"
    show_text(screen, (480, 50), "Current："+text,
              (223, 223, 223), False, 18, False)

    if game_state == 2:
        show_text(screen, (200, 200), "BLACK Victory",
                  (210, 210, 0), False, 30, False)
    if game_state == 3:
        show_text(screen, (200, 200), "WHITE Victory",
                  (210, 210, 0), False, 30, False)


def draw_mouse_indicator(screen: object, game_state: int) -> None:

    if game_state == 1:

        x, y = pygame.mouse.get_pos()
        x = int(round((x-SPACE)*1.0/CELL_SIZE))
        y = int(round((y-SPACE)*1.0/CELL_SIZE))
        if 0 <= x <= CELL_NUM and 0 <= y <= CELL_NUM:
            pygame.draw.line(screen, (255, 33, 56), (x*CELL_SIZE+SPACE-int(CELL_SIZE/2), y*CELL_SIZE+SPACE-int(
                CELL_SIZE/2)), (x*CELL_SIZE+SPACE-int(CELL_SIZE/2), y*CELL_SIZE+SPACE+int(CELL_SIZE/2)), 1)
            pygame.draw.line(screen, (255, 33, 56), (x*CELL_SIZE+SPACE-int(CELL_SIZE/2), y*CELL_SIZE+SPACE-int(
                CELL_SIZE/2)), (x*CELL_SIZE+SPACE+int(CELL_SIZE/2), y*CELL_SIZE+SPACE-int(CELL_SIZE/2)), 1)
            pygame.draw.line(screen, (255, 33, 56), (x*CELL_SIZE+SPACE+int(CELL_SIZE/2), y*CELL_SIZE+SPACE-int(
                CELL_SIZE/2)), (x*CELL_SIZE+SPACE+int(CELL_SIZE/2), y*CELL_SIZE+SPACE+int(CELL_SIZE/2)), 1)
            pygame.draw.line(screen, (255, 33, 56), (x*CELL_SIZE+SPACE-int(CELL_SIZE/2), y*CELL_SIZE+SPACE+int(
                CELL_SIZE/2)), (x*CELL_SIZE+SPACE+int(CELL_SIZE/2), y*CELL_SIZE+SPACE+int(CELL_SIZE/2)), 1)


def show_text(screen: object, pos: tuple, text: str, color: tuple, font_bold=False, font_size=60, font_italic=False):

    cur_font = pygame.font.SysFont("SimHei", font_size)

    cur_font.set_bold(font_bold)

    cur_font.set_italic(font_italic)

    text_fmt = cur_font.render(text, 1, color)

    screen.blit(text_fmt, pos)
