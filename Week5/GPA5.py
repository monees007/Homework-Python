def process():
    x = board_min()  # Take the minimum at paper
    board_erase(x)  # Remove it from board
    if board_isEmpty():  # If board is empty
        return x  # end with empty board and return no of paper.
    y = board_min()  # pick the second smallest integer from board.
    board_erase(y)  # remove it from board.
    diff = int(x - y)  # take the difference
    if diff < 0:  # If it is negative
        diff = -1 * diff  # make it positive
    board_write(diff)  # write this value at board.
    return process()  # Repeat the whole process again

# Submission Successful! 3 out of 3 private test(s) passed.
