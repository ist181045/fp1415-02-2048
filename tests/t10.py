## ========================================================================== ##
## -------------------------------------------------------------------------- ##
##                                 TEST 10                                    ##
## -------------------------------------------------------------------------- ##
## ========================================================================== ##

# -- Beste: boards_equal -- #
B1 = create_board()
B2 = create_board()
boards_equal(B1, B2)
C = create_coordinate(1, 2)
B1 = board_fill_position(B1, C, 2)
C = create_coordinate(2, 3)
B1 = board_fill_position(B1, C, 4)
C = create_coordinate(1, 2)
B2 = board_fill_position(B2, C, 2)
C = create_coordinate(2, 3)
B2 = board_fill_position(B2, C, 4)
boards_equal(B1, B2)
C = create_coordinate(1, 1)
B2 = board_fill_position(B2, C, 256)
boards_equal(B1, B2)