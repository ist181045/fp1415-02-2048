## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                 TEST 12                                    ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Abstraction: coordinate and board -- #
B = create_board()
C1 = create_coordinate(3, 2)
C2 = create_coordinate(2, 3)
B = board_fill_position(B, C1, 2)
B = board_fill_position(B, C2, 4)
R = board_empty_positions(B)
coordinate_in_list(C1, R)
coordinate_in_list(C2, R)
coordinate_in_list(create_coordinate(1, 1), R)
# - (additional hidden tests) - #
B = create_board()
print(', '.join(str(coord) for coord in board_empty_positions(B)))
B = board_fill_position(B, create_coordinate(1, 1), 2)
B = board_fill_position(B, create_coordinate(1, 3), 8)
B = board_fill_position(B, create_coordinate(2, 1), 32)
B = board_fill_position(B, create_coordinate(2, 4), 256)
B = board_fill_position(B, create_coordinate(3, 3), 2048)
print(', '.join(str(coord) for coord in board_empty_positions(B)))
B = create_board()
B = board_fill_position(B, create_coordinate(1, 3), 2)
B = board_fill_position(B, create_coordinate(1, 4), 2)
B = board_fill_position(B, create_coordinate(2, 2), 2)
B = board_fill_position(B, create_coordinate(2, 3), 2)
B = board_fill_position(B, create_coordinate(3, 1), 2)
B = board_fill_position(B, create_coordinate(3, 2), 2)
B = board_fill_position(B, create_coordinate(4, 1), 2)
B = board_fill_position(B, create_coordinate(4, 4), 2)
B = board_reduce(B, 'E')
print_board(B)
