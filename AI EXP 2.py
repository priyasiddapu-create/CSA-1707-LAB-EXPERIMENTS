N = 8
board = [-1] * N

def solve(row):
    if row == N:
        print(board)
        return True

    for col in range(N):
        if all(board[i] != col and abs(board[i] - col) != row - i
               for i in range(row)):
            board[row] = col
            if solve(row + 1):
                return True
    return False

solve(0)
