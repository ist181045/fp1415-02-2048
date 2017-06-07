## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                 TEST 11                                    ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Best: request_move; output transformer: print_board
B = create_board()
print_board(B)
C = create_coordinate(1, 2)
B = board_fill_position(B, C, 2)
print_board(B)
C = create_coordinate(2, 3)
B = board_fill_position(B, C, 4)
B = board_update_score(B, 48)
print_board(B)
C = create_coordinate(2, 2)
B = board_fill_position(B, C, 8)
print_board(B)
C = create_coordinate(3, 3)
B = board_fill_position(B, C, 2048)
B = board_update_score(B, 2048)
print_board(B)
C = create_coordinate(1, 1)
B = board_fill_position(B, C, 256)
print_board(B)
B = create_board()
C = create_coordinate(1, 2)
B = board_fill_position(B, C, 2)
C = create_coordinate(1, 4)
B = board_fill_position(B, C, 2)
print_board(B)
M = request_move()
S
B = board_reduce(B, M)
C = create_coordinate(1, 4)
B = board_fill_position(B, C, 2)
print_board(B)