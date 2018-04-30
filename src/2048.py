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

def create_coordinate(row, col):
    """ create_coordinate : integer x integer -> coordinate
        - Takes two integer arguments between 1 e ROWS/COLS and returns a
        coordinate (tuple). Raises a ValueError if the parameters are
        invalid """
    
    if (isinstance(row, int) and 1 <= row <= ROWS
            and isinstance(col, int) and 1 <= col <= COLS):
        return (row, col)
    else:
        raise ValueError('create_coordinate: invalid arguments')


# ---------------------------------------------------------------------------- #
# |                                ACCESSORS                                 | #
# ---------------------------------------------------------------------------- #

def coordinate_row(coord):
    """ coordinate_row : coordinate -> integer
        - Returns a coordinate's row """
    
    return coord[0]


def coordinate_col(coord):
    """ coordinate_row : coordinate -> integer
        - Returns a coordinate's column """
    
    return coord[1]


# ---------------------------------------------------------------------------- #
# |                               RECOGNIZERS                                | #
# ---------------------------------------------------------------------------- #

def is_coordinate(arg):
    """ is_coordinate : universal -> bool
        - Checks if the given argument is a coordinate, checking if its
        representation corresponds with the one defined """
    
    return (isinstance(arg, tuple) and len(arg) == 2
            and isinstance(arg[0], int) and isinstance(arg[1], int)
            and 1 <= arg[0] <= ROWS and 1 <= arg[1] <= COLS)


# ---------------------------------------------------------------------------- #
# |                                  TESTS                                   | #
# ---------------------------------------------------------------------------- #

def coordinates_equal(c1, c2):
    """ coordinates_equal : coordinate x coordinate -> bool
        - Tests if two coordinates are the same, comparing their components.
        (a, b) = (c, d) if a == c AND b == d """

    return (coordinate_row(c1) == coordinate_row(c2)
            and coordinate_col(c1) == coordinate_col(c2))


## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                              Board ADT                                 | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# ---------------------------------------------------------------------------- #
# |                               CONSTRUCTOR                                | #
# ---------------------------------------------------------------------------- #

def create_board():
    """ create_board: {} -> board
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


def board_position(board, coord):
    """ board_position: board x coordinate -> integer
        - Returns the value of the panel in the given board at the given
        coordinates """
    
    if is_coordinate(coord):
        row = coordinate_row(coord) - 1
        col = coordinate_col(coord) - 1
        return board['board'][row][col]
    else:
        raise ValueError('board_position: invalid arguments')


def board_score(board):
    """ board_score: board -> integer
        - Returns the score of the given board """
    
    return board['score']


def board_empty_positions(board):
    """ board_empty_positions: board -> list
        - Calculates and returns a list with the coordinates of the given
        board's positions that are empty """
    
    empty = []
    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            coord = create_coordinate(i, j)
            if board_position(board, coord) == 0:
                empty = empty + [coord]
    return empty


# ---------------------------------------------------------------------------- #
# |                                MODIFIERS                                 | #
# ---------------------------------------------------------------------------- #

def board_fill_position(board, coord, value):
    """ board_fill_position: board x coordinate x integer -> board
        - Fills the position in the given board at the given coordinates
        with the given value and returns the modified board """
    
    if is_coordinate(coord) and isinstance(value, int):
        row = coordinate_row(coord) - 1
        col = coordinate_col(coord) - 1
        board['board'][row][col] = value
        return board
    else:
        raise ValueError('board_fill_position: invalid arguments')


def board_update_position(board, value):
    """ board_update_position: board x integer -> board
        - Adds to the board's score the given value and returns the board with
        the updated score """
    
    if isinstance(value, int) and value >= 0 and value % 4 == 0:
        board['score'] += value
        return board
    else:
        raise ValueError('board_update_position: invalid arguments')


def board_reduce(board, move):
    """ board_reduce: board x string -> board
        - Reduces the board in the direction corresponding to the given move,
        performing combinations, if possible, and returns the reduced board """
    
    if not is_move(move):
        raise ValueError('board_reduce: invalid arguments')

    coord_orig, coord_dest = 0, 0  # Initialization
    # Distinction between horizontal and vertical moves. Allows boards with
    # generic dimensions n x p (where n may or not be equal to p)
    if move in ('N', 'S'):
        for j in range(1, COLS + 1):
            locked = []  # Coords of positions where combinations occurred
            for k in range(ROWS - 1):
                for i in range(2, ROWS + 1 - k):            
                    if move == 'N':
                        coord_orig = create_coordinate(i, j)
                        coord_dest = create_coordinate(i - 1, j)
                    else:
                        coord_orig = create_coordinate(ROWS + 1 - i, j)
                        coord_dest = create_coordinate(ROWS + 2 - i, j)
                    # Moves the panel, if possible. Combines and locks the
                    # coordinates where combos occurred during a swipe
                    board, locked = move_piece(
                        board, coord_orig, coord_dest, locked)
    elif move in ('E', 'W'):
        for j in range(1, ROWS + 1):
            locked = []
            for k in range(COLS - 1):
                for i in range(2, COLS + 1 - k):            
                    if move == 'E':
                        coord_orig = create_coordinate(j, COLS + 1 - i)
                        coord_dest = create_coordinate(j, COLS + 2 - i)
                    else:
                        coord_orig = create_coordinate(j, i)
                        coord_dest = create_coordinate(j, i - 1)
                    board, locked = move_piece(
                        board, coord_orig, coord_dest, locked)
        return board


# Helpers (board_reduce) ####################################################

def move_piece(board, coord_orig, coord_dest, locked):
    """ move_piece : board x coordinate x coordinate x list -> board x list 
        - Given a board and two coordinates, origin and destination, along with
        a list of coordinates of the positions between which combos occured,
        returns the updated board, if possible (combos or not), and a list with
        the coordinates where combos have occurred in this move """
    
    value_orig = board_position(board, coord_orig)
    value_dest = board_position(board, coord_dest)
    
    if value_dest == 0:
        if value_orig != 0:
            board_fill_position(board, coord_dest, value_orig)
            board_fill_position(board, coord_orig, 0)
    elif value_orig == value_dest:
        if coordinate_in_list(coord_orig, locked):
            return board, locked
        else:
            value = value_orig + value_dest
            board_fill_position(board, coord_dest, value)
            board_fill_position(board, coord_orig, 0)
            board_update_position(board, value)
            locked += [coord_orig] + [coord_dest]
    
    return board, locked


def coordinate_in_list(coord, lst):
    """ coordinate_in_list : coordinate x list -> bool
        - Given a coordinate and a list of coordinates, returns True, if the
        coordinate is in the list, False, otherwise """
    
    for c in lst:
        if coordinates_equal(coord, c):
            return True
    return False

# END HELPERS ##################################################################


# ---------------------------------------------------------------------------- #
# |                               RECOGNIZERS                                | #
# ---------------------------------------------------------------------------- #

def is_board(arg):
    """ is_board: universal -> bool
        - Checks if the given argument is a board, checking its representation,
        dimension and if the dictionary keys 'board' and 'score' exist """
    
    is_board = (isinstance(arg, dict) and len(arg) == 2
                and 'board' in arg and isinstance(arg['board'], list)
                and 'score' in arg and isinstance(arg['score'], int)
                and len(arg['board']) == ROWS)
    if is_board:
        for i in range(ROWS):
            is_board = is_board and len(arg['board'][i]) == COLS
    return is_board


# ---------------------------------------------------------------------------- #
# |                                  TESTS                                   | #
# ---------------------------------------------------------------------------- #

def board_finished(board):
    """ board_finished: board x board -> bool
        - Reduces a copy of the board in every direction. If both the copy and
        the original are the same, the board is finished """
    
    return (len(board_empty_positions(board)) == 0
            and boards_equal(board, board_reduce(copy_board(board), 'N'))
            and boards_equal(board, board_reduce(copy_board(board), 'S'))
            and boards_equal(board, board_reduce(copy_board(board), 'E'))
            and boards_equal(board, board_reduce(copy_board(board), 'W')))


def boards_equal(board1, board2):
    """ boards_equal: board x board -> bool
        - Checks if the given boards are the same, comparing the value of every
        position and both boards' scores """
    
    equal = True
    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            coord = create_coordinate(i, j)
            equal = equal and (
                board_position(board1, coord) == board_position(board2, coord))
            if not equal:
                return equal
    return equal and board1['score'] == board2['score']


# ---------------------------------------------------------------------------- #
# |                               TRANSFORMERS                               | #
# ---------------------------------------------------------------------------- #

def print_board(board):
    """ print_board: board -> {}
        - Writes the external representation of the given board """
    
    if is_board(board):
        for i in range(1, ROWS + 1):
            row = ''
            for j in range(1, COLS + 1):
                row += ('[ %d ] ' %
                        board_position(board, create_coordinate(i, j)))
            print(row)
        print('Score: %d' % board_score(board))
    else:
        raise ValueError('print_board: invalid arguments')


## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                            Helper Functions                            | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

def request_move():
    """ request_move: {} -> string
        - Prompts the user to insert a move, returning it, if valid one """
    
    while True:
        move = input('Pick a move (N, S, E, W): ')
        if not is_move(move):
            print('Invalid move.')
        else:
            break
    return move


def copy_board(board):
    """ board -> board
        - Returns a copy of the given board """
    
    board_copy = create_board()
    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            coord = create_coordinate(i, j)
            board_fill_position(board_copy, coord,
                                board_position(board, coord))
    board_update_position(board_copy, board_score(board))
    return board_copy


def fill_random_position(board):
    """ fill_random_position: board -> {}
        - Given a board, fills in an empty position at random with either a 2 or
        a 4, having the first one an 80% of being chosen, and the latter 20%
        chance """
    
    from random import random
    choices = (2, 2, 2, 2, 4)  # Four 2s and a 4 => 80% 2s, 20% 4s
    empty = board_empty_positions(board)

    return board_fill_position(board, empty[int(random() * len(empty))],
                                      choices[int(random() * len(choices))])


# EXTRA ########################################################################

def is_move(arg):
    """ is_move: universal -> bool
        - Checks if the given argument is a valid play and returns True, if so,
        False otherwise """
    
    return isinstance(arg, str) and arg in 'NSEW'

# END EXTRA ####################################################################


## ========================================================================== ##
## -------------------------------------------------------------------------- ##
## |                              THE GAME                                  | ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

def game_2048():
    """ game_2048: {} -> {}
        - Starts a game of 2048 (console) """
    
    game_board = create_board()
    fill_random_position(fill_random_position(game_board))
    
    achieved_2048, quit = False, False
    while not (board_finished(game_board) or quit):
        print_board(game_board)
        board_copy = copy_board(game_board)
        board_reduce(game_board, request_move())
        
        # If there is room or the boards are the same, fill an empty position
        if (len(board_empty_positions(game_board)) > 0
                and not boards_equal(game_board, board_copy)):
            fill_random_position(game_board)
            
        # Achieved a tile with 2048?
        if not achieved_2048 and position_in_board(game_board, 2048):
            achieved_2048 = True
            print_board(game_board)
            print('#======================================#\n' \
                + '# You won! :D You can continue playing #\n' \
                + '#======================================#')
            while True:
                keep_going = input('Do you wish to continue (Y/n)? ')[0]
                if len(keep_going) == 0 or keep_going in 'YNyn':
                    quit = keep_going in 'Nn'
                    break
                else:
                    print('Invalid answer, let\'s try that again..')

    print('Game over')


def position_in_board(board, value):
    """ position_in_board : board x value -> bool
        - Given a board and an integer value, checks if there is a position in
        the board with that value and returns True, if so, False, otherwise """
    
    if is_board(board) and isinstance(value, int):
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if board_position(board, create_coordinate(i, j)) == value:
                    return True
    return False
