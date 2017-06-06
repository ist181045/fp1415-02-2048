# Project #2 - 2048
# 80858 - Beatriz Grilo
# 81045 - Rui Ventura

##
## Constants
##

ROWS = COLS = 4



## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                             Coordinate ADT                             | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# ---------------------------------------------------------------------------- #
# |                               CONSTRUCTOR                                | #
# ---------------------------------------------------------------------------- #

def cria_coordenada(row, col):
    """ cria_coordenada : integer x integer -> coordinate
        - Takes two integer arguments between 1 e ROWS/COLS and returns a
        coordinate (tuple). Raises a ValueError if the parameters are
        invalid """
    
    if isinstance(row, int) and 1 <= row <= ROWS \
            and isinstance(col, int) and 1 <= col <= COLS:
        return (row, col)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')


# ---------------------------------------------------------------------------- #
# |                                ACCESSORS                                 | #
# ---------------------------------------------------------------------------- #

def coordenada_linha(coord):
    """ coordenada_linha : coordinate -> integer
        - Returns a coordinate's row """
    
    return coord[0]

def coordenada_coluna(coord):
    """ coordenada_linha : coordinate -> integer
        - Returns a coordinate's column """
    
    return coord[1]


# ---------------------------------------------------------------------------- #
# |                               RECOGNIZERS                                | #
# ---------------------------------------------------------------------------- #

def e_coordenada(arg):
    """ e_coordenada : universal -> bool
        - Checks if the given argument is a coordinate, checking if its
        representation corresponds with the one defined """
    
    return isinstance(arg, tuple) and len(arg) == 2 \
            and isinstance(arg[0], int) and isinstance(arg[1], int) \
            and 1 <= arg[0] <= ROWS and 1 <= arg[1] <= COLS


# ---------------------------------------------------------------------------- #
# |                                  TESTS                                   | #
# ---------------------------------------------------------------------------- #

def coordenadas_iguais(c1, c2):
    """ coordenadas_iguais : coordinate x coordinate -> bool
        - Tests if two coordinates are the same, comparing their components.
        (a, b) = (c, d) if a == c AND b == d """

    return coordenada_linha(c1) == coordenada_linha(c2) \
            and coordenada_coluna(c1) == coordenada_coluna(c2)



## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                              Board ADT                                 | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# ---------------------------------------------------------------------------- #
# |                               CONSTRUCTOR                                | #
# ---------------------------------------------------------------------------- #

def cria_tabuleiro():
    """ cria_tabuleiro: {} -> board
        - Creates a dictionary which has 2 keys, one for the board itself, a
        list, and another for the score, an integer """
    
    board = list()
    # A list with ROWS lists, each with COLS elements
    for i in range(ROWS):
        board = board + [[0] * COLS]
    return {'board': board, 'score': 0}

# ---------------------------------------------------------------------------- #
# |                                ACCESSORS                                 | #
# ---------------------------------------------------------------------------- #

def tabuleiro_posicao(board, coord):
    """ tabuleiro_posicao: board x coordinate -> integer
        - Returns the value of the panel in the given board at the given
        coordinates """
    
    if e_coordenada(coord):
        return board['board'] \
                [coordenada_linha(coord) - 1][coordenada_coluna(coord) - 1]
    else:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')

def tabuleiro_pontuacao(board):
    """ tabuleiro_pontuacao: board -> integer
        - Returns the score of the given board """
    
    return board['score']

def tabuleiro_posicoes_vazias(board):
    """ tabuleiro_posicoes_vazias: board -> list
        - Calculates and returns a list with the coordinates of the given
        board's positions that are empty """
    
    empty = []
    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            coord = cria_coordenada(i, j)
            if tabuleiro_posicao(board, coord) == 0:
                empty = empty + [coord]
    return empty


# ---------------------------------------------------------------------------- #
# |                                MODIFIERS                                 | #
# ---------------------------------------------------------------------------- #

def tabuleiro_preenche_posicao(board, coord, value):
    """ tabuleiro_preenche_posicao: board x coordinate x integer -> board
        - Fills the position in the given board at the given coordinates
        with the given value and returns the modified board """
    
    if e_coordenada(coord) and isinstance(value, int):
        board['board'][coordenada_linha(coord) - 1] \
                        [coordenada_coluna(coord) - 1] = value
        return board
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')

def tabuleiro_actualiza_pontuacao(board, value):
    """ tabuleiro_actualiza_pontuacao: board x integer -> board
        - Adds to the board's score the given value and returns the board with
        the updated score """
    
    if isinstance(value, int) and value >= 0 and value % 4 == 0:
        board['score'] = board['score'] + value
        return board
    else:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')

def tabuleiro_reduz(board, play):
    """ tabuleiro_reduz: board x string -> board
        - Reduces the board in the direction corresponding to the given play,
        performing combinations, if possible, and returns the reduced board """
    
    if not e_jogada(play):
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
    else:
        coord_orig, coord_dest = 0, 0 # Initialization
        # Distinction between horizontal and vertical moves. Allows boards with
        # generic dimensions n x p (where n may or not be equal to p)
        if play in ('N', 'S'):
            for j in range(1, COLS + 1):
                locked = [] # Coords of positions where combinations occurred
                for k in range(ROWS - 1):
                    for i in range(2, ROWS + 1 - k):            
                        if play == 'N':
                            coord_orig = cria_coordenada(i, j)
                            coord_dest = cria_coordenada(i - 1, j)
                        else:
                            coord_orig = cria_coordenada(ROWS + 1 - i, j)
                            coord_dest = cria_coordenada(ROWS + 2 - i, j)
                        # Moves the panel, if possible. Combines and locks the
                        # coordinates where combos occurred during a swipe
                        tab, locked = move_peca(board, coord_orig, coord_dest, \
                                                  locked)
        elif play in ('E', 'W'):
            for j in range(1, ROWS + 1):
                locked = []
                for k in range(COLS - 1):
                    for i in range(2, COLS + 1 - k):            
                        if play == 'E':
                            coord_orig = cria_coordenada(j, COLS + 1 - i)
                            coord_dest = cria_coordenada(j, COLS + 2 - i)
                        else:
                            coord_orig = cria_coordenada(j, i)
                            coord_dest = cria_coordenada(j, i - 1)
                        tab, locked = move_peca(board, coord_orig, coord_dest, \
                                                  locked)
        return tab


# Helpers (tabuleiro_reduz) ####################################################

def move_peca(board, coord_orig, coord_dest, locked):
    """ move_pecas : board x coordinate x coordinate x list -> board x lista 
        - Given a board and two coordinates, origin and destination, along with
        a list of coordinates of the positions between which combos occured,
        returns the updated board, if possible (combos or not), and a list with
        the coordinates where combos have occurred in this move """
    
    value_orig = tabuleiro_posicao(board, coord_orig)
    value_dest = tabuleiro_posicao(board, coord_dest)
    
    if value_dest == 0:
        if value_orig != 0:
            tabuleiro_preenche_posicao(board, coord_dest, value_orig)
            tabuleiro_preenche_posicao(board, coord_orig, 0)
    elif value_orig == value_dest:
        if coordenada_na_lista(coord_orig, locked):
            return board, locked
        else:
            valor = value_orig + value_dest
            tabuleiro_preenche_posicao(board, coord_dest, valor)
            tabuleiro_preenche_posicao(board, coord_orig, 0)
            tabuleiro_actualiza_pontuacao(board, valor)
            locked = locked + [coord_orig] + [coord_dest]
    
    return board, locked

def coordenada_na_lista(coord, lst):
    """ coordenada_na_lista : coordinate x list -> bool
        - Given a coordinate and a list of coordinates, returns True, if the
        coordinate is in the list, False, otherwise """
    
    for c in lst:
        if coordenadas_iguais(coord, c):
            return True
    return False

# FIM AUXILIARES ################################################################


# ---------------------------------------------------------------------------- #
# |                               RECOGNIZERS                                | #
# ---------------------------------------------------------------------------- #

def e_tabuleiro(arg):
    """ e_tabuleiro: universal -> bool
        - Checks if the given argument is a board, checking its representation,
        dimension and if the dictionary keys 'board' and 'score' exist """
    
    is_board = isinstance(arg, dict) and len(arg) == 2 \
            and 'board' in arg and isinstance(arg['board'], list) \
            and 'score' in arg and isinstance(arg['score'], int) \
            and len(arg['board']) == ROWS
    if is_board:
        for i in range(ROWS):
            is_board = is_board and len(arg['board'][i]) == COLS
    return is_board


# ---------------------------------------------------------------------------- #
# |                                  TESTS                                   | #
# ---------------------------------------------------------------------------- #

def tabuleiro_terminado(board):
    """ tabuleiros_terminado: board x board -> bool
        - Reduces a copy of the board in every direction. If both the copy and
        the original are the same, the board is finished """
    
    return len(tabuleiro_posicoes_vazias(board)) == 0 \
            and tabuleiros_iguais(board, \
                tabuleiro_reduz(copia_tabuleiro(board), 'N')) \
            and tabuleiros_iguais(board, \
                tabuleiro_reduz(copia_tabuleiro(board), 'S')) \
            and tabuleiros_iguais(board, \
                tabuleiro_reduz(copia_tabuleiro(board), 'E')) \
            and tabuleiros_iguais(board, \
                tabuleiro_reduz(copia_tabuleiro(board), 'W'))

def tabuleiros_iguais(board1, board2):
    """ tabuleiros_iguais: board x board -> bool
        - Checks if the given boards are the same, comparing the value of every
        position and both boards' scores """
    
    equal = True
    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            coord = cria_coordenada(i, j)
            equal = equal and tabuleiro_posicao(board1, coord) == \
                                tabuleiro_posicao(board2, coord)
            if not equal:
                return equal
    return equal and board1['score'] == board2['score']


# ---------------------------------------------------------------------------- #
# |                               TRANSFORMERS                               | #
# ---------------------------------------------------------------------------- #

def escreve_tabuleiro(board):
    """ escreve_tabuleiro: board -> {}
        - Writes the external representation of the given board """
    
    if e_tabuleiro(board):
        for i in range(1, ROWS + 1):
            row = ''
            for j in range(1, COLS + 1):
                row += '[ ' \
                    + str(tabuleiro_posicao(board, cria_coordenada(i, j))) \
                    + ' ] '
            print(row)
        print('Pontuacao: ' + str(tabuleiro_pontuacao(board)))
    else:
        raise ValueError('escreve_tabuleiro: argumentos invalidos')



## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                            Helper Functions                            | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

def pede_jogada():
    """ pede_jogada: {} -> string
        - Prompts the user to insert a play, returning it, if valid one """
    
    play = input('Introduza uma jogada (N, S, E, W): ')
    while not e_jogada(play):
        print('Jogada invalida.')
        play = input('Introduza uma jogada (N, S, E, W): ')
    return play

def copia_tabuleiro(board):
    """ board -> board
        - Returns a copy of the given board """
    board_copy = cria_tabuleiro()
    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            coord = cria_coordenada(i, j)
            tabuleiro_preenche_posicao(
                board_copy, coord, tabuleiro_posicao(board, coord))
    tabuleiro_actualiza_pontuacao(board_copy, tabuleiro_pontuacao(board))
    return board_copy

from random import random
def preenche_posicao_aleatoria(tab):
    """ preenche_posicao_aleatoria: board -> {}
        - Given a board, fills in an empty position at random with either a 2 or
        a 4, having the first one an 80% of being chosen, and the latter 20%
        chance """
    
    escolhas = (2, 2, 2, 2, 4) # Four 2s and a 4 => 80% 2s, 20% 4s
    vazias = tabuleiro_posicoes_vazias(tab)

    return tabuleiro_preenche_posicao(tab, vazias[int(random() * len(vazias))], \
                                      escolhas[int(random() * len(escolhas))])


# EXTRA ########################################################################

def e_jogada(arg):
    """ e_jogada: universal -> bool
        - Checks if the given argument is a valid play and returns True, if so,
        False otherwise """
    
    return isinstance(arg, str) and arg in ('N', 'S', 'E', 'W')

# END EXTRA ####################################################################



## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                              THE GAME                                  | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

def jogo_2048():
    """ jogo_2048: {} -> {}
        - Starts a game of 2048 (console) """
    
    game_board = cria_tabuleiro()
    preenche_posicao_aleatoria(preenche_posicao_aleatoria(game_board))
    
    achieved_2048, quit = False, False
    while not (tabuleiro_terminado(game_board) or quit):
        escreve_tabuleiro(game_board)
        board_copy = copia_tabuleiro(game_board)
        tabuleiro_reduz(game_board, pede_jogada())
        # If there is room or the boards are the same, fill an empty position
        if len(tabuleiro_posicoes_vazias(game_board)) > 0 and \
           not tabuleiros_iguais(game_board, board_copy):
            preenche_posicao_aleatoria(game_board)
            
        # Achieved a tile with 2048?
        if not achieved_2048 and posicao_no_tabuleiro(game_board, 2048):
            achieved_2048 = True
            escreve_tabuleiro(game_board)
            print('#======================================#\n' \
                + '# You won! :D You can continue playing #\n' \
                + '#======================================#')
            while True:
                keep_going = input('Do you wish to continue (Y/N)? ')[0]
                quit = keep_going == 'N'
                if keep_going in ('Y', 'N'): break
                else: print('Invalid answer, let\'s try that again..')

    print('Game over')

def posicao_no_tabuleiro(board, value):
    """ posicao_no_tabuleiro : board x value -> bool
        - Given a board and an integer value, checks if there is a position in
        the board with that value and returns True, if so, False, otherwise """
    
    if e_tabuleiro(board) and isinstance(value, int):
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if tabuleiro_posicao(board, cria_coordenada(i, j)) == value:
                    return True
    return False
