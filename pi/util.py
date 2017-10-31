

def is_valid_location(coord):
    """
    Check if a coordinate is within the range (0, 7) inclusive for each coordinate part
    :param coord: A 2-tuple representing the (row, col) coordinate on the board
    :return: Boolean, True if the coordinate is within range
    """
    row, col = coord[0], coord[1]
    return 0 <= row <= 7 and 0 <= col <= 7


def detect_check(piece, coord, chess_board):
    """
    Detects if teams king is in "check" based on the movements on board
    :param piece: a king object
    :param coord: A 2-tuple representing the (row, col) coordinate on the board
    :return: Boolean, True if king passed in is in check else false
    """

    locs = []
    r, c = coord[0], coord[1]
    for r in range[0, 7]:
        for c in range[0, 7]:
            if chess_board[(r, c)] is not None and chess_board[(r, c)].is_black != piece.is_black:
                locs += chess_board[(r, c)].get_moves()
    if coord in locs:
        return True
    else:
        return False



