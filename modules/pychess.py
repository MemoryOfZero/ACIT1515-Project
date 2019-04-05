import pygame
import chess
import chess.engine
import json
import sys
from modules.chess_pieces import *
from time import sleep

x_to_col = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((60*8, 60*8))
pygame.display.set_caption('Chess')

bg = pygame.image.load('assets/chessboard.png')

clock = pygame.time.Clock()

screen.blit(bg, (0,0))
clock.tick(60)

board = chess.Board()
board.legal_moves

with open('config.json',  'r') as f:
    engine_path = json.load(f)['chess_engine']
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

def mouse_to_uci(mouse1, mouse2):
    return '{}{}{}{}'.format(x_to_col[mouse1[0]], 8 - mouse1[1], x_to_col[mouse2[0]], 8 - mouse2[1])

def parse_fen(fen):
    board_array = []
    fen_board = fen.split()[0].split('/')

    for row in fen_board:
        row_array = []
        row_split = list(row)
        for char in row_split:
            if char.isdigit():
                for i in range(int(char)):
                    row_array.append('')
            else:
                row_array.append(char)
        board_array.append(row_array)

    return board_array

def draw_board(array):
    sprite_list = pygame.sprite.Group()

    for row in range(len(array)):
        for col in range(len(array[row])):
            square = array[row][col]

            if square == 'r':
                sprite_list.add(Rook('b', col, row))
            elif square == 'n':
                sprite_list.add(Knight('b', col, row))
            elif square == 'b':
                sprite_list.add(Bishop('b', col, row))
            elif square == 'q':
                sprite_list.add(Queen('b', col, row))
            elif square == 'k':
                sprite_list.add(King('b', col, row))
            elif square == 'p':
                sprite_list.add(Pawn('b', col, row))
            elif square == 'R':
                sprite_list.add(Rook('w', col, row))
            elif square == 'N':
                sprite_list.add(Knight('w', col, row))
            elif square == 'B':
                sprite_list.add(Bishop('w', col, row))
            elif square == 'Q':
                sprite_list.add(Queen('w', col, row))
            elif square == 'K':
                sprite_list.add(King('w', col, row))
            elif square == 'P':
                sprite_list.add(Pawn('w', col, row))

    screen.blit(bg, (0,0))
    sprite_list.draw(screen)
    clock.tick(60)

def select_square():
    pos = pygame.mouse.get_pos()
    x = pos[0] // 60
    y = pos[1] // 60
    return (x, y)

def write_message(text):
    textfont = pygame.font.Font(None,40)
    text = textfont.render(text,True, (155,0,255))
    textpos = text.get_rect()
    textpos.center = (60*8/2, 60*8/2)
    screen.blit(text,textpos)
    pygame.display.update()

def run_game():

    turn = 'player'

    draw_board(parse_fen(board.fen()))
    pygame.display.update()

    mouse1 = ()
    mouse2 = ()
    selected = False

    while not board.is_game_over():

        if turn == 'player':
            if board.is_check():
                write_message('You are in check')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    engine.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and not selected:
                    mouse1 = select_square()
                    selected = True

                elif event.type == pygame.MOUSEBUTTONDOWN and selected:
                    mouse2 = select_square()

                    move = mouse_to_uci(mouse1, mouse2)
                    try:
                        board.push_uci(move)
                        selected = False
                        turn = 'AI'

                    except ValueError:
                        selected = False
                        write_message('Invalid Move')
                        sleep(1)

        elif turn == 'AI':
            result = engine.play(board, chess.engine.Limit(time=0.100))
            board.push(result.move)
            turn = 'player'

        draw_board(parse_fen(board.fen()))
        pygame.display.update()

    write_message('Game over')
    sleep(5)
    pygame.quit()
    engine.quit()
    sys.exit()

def start():
    run_game()

if __name__ == '__main__':
    run_game()
