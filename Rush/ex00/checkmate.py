def checkmate(board):
    board_2d = [list(row.strip()) for row in board.strip().splitlines()]
    
    valid_chars = {"R", "P", "B", "Q", "K", "."}
    row_lengths = [len(row) for row in board_2d]
    if len(set(row_lengths)) != 1 or row_lengths[0] != len(board_2d):
        print("Error")
        return
    for row in board_2d:
        if not all(c in valid_chars for c in row):
            print("Error")
            return
        
    length = len(board_2d)
    found = False
    for i in range(length):
        for j in range(length):
            cur = board_2d[i][j]
            if cur == "R" and rookHandler(i, j, board_2d, length):
                found = True
                break
            elif cur == "P" and pawnHandler(i, j, board_2d, length):
                found = True
                break
            elif cur == "B" and bishopHandler(i, j, board_2d, length):
                found = True
                break
            elif cur == "Q" and queenHandler(i, j, board_2d, length):
                found = True
                break
        if found:
            print("Success")
            return
    print("Fail")
    

def rookHandler(i, j, board, length):
    for x in range(i - 1, -1, -1):
        if board[x][j] == "K":
            return True
        if board[x][j] != ".":
            break

    for x in range(i + 1, length):
        if board[x][j] == "K":
            return True
        if board[x][j] != ".":
            break

    for y in range(j - 1, -1, -1):
        if board[i][y] == "K":
            return True
        if board[i][y] != ".":
            break

    for y in range(j + 1, length):
        if board[i][y] == "K":
            return True
        if board[i][y] != ".":
            break

    return False

def pawnHandler(i, j, board, length):
    if i - 1 >= 0:
        if j - 1 >= 0 and board[i - 1][j - 1] == "K":
            return True
        if j + 1 < length and board[i - 1][j + 1] == "K":
            return True
    return False

def bishopHandler(i, j, board, length):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        x, y = i + dx, j + dy
        while 0 <= x < length and 0 <= y < length:
            if board[x][y] == "K":
                return True
            
            if board[x][y] != ".":
                break
            x += dx
            y += dy
    return False

def queenHandler(i, j, board, length):
    
    return rookHandler(i, j, board, length) or bishopHandler(i, j, board, length)
