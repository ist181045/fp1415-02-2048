## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                  TEST 09                                   ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Reconhecedores: is_board, board_finished -- #
B = create_board()
is_board(B)
C = create_coordinate(1, 2)
B = board_fill_position(B, C, 2)
is_board(B)
is_board(C)
C = create_coordinate(1, 4)
B = board_fill_position(B, C, 2)
is_board(B)
print_board(B)
M = request_move()
W
B = board_reduce(B, M)
is_board(B)
C = create_coordinate(1, 4)
B = board_fill_position(B, C, 2)
is_board(B)
board_finished(B)
print_board(B)
M = request_move()
S
B = board_reduce(B, M)
C = create_coordinate(1, 4)
B = board_fill_position(B, C, 2)
print_board(B)
is_board(B)
board_finished(B)