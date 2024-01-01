def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != ' ':
            return board[0][j]
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != ' ':
        return board[1][1]
    is_full = True
    for row in board:
        if ' ' in row:
            is_full = False
            break
    if is_full:
        return 'tie'
    return None
board = [
    ['X', 'O', ' '],
    ['O', 'X', 'O'],
    ['X', ' ', 'X']]
winner = check_winner(board)
if winner:
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"{winner} is the winner!")
else:
    print("No winner yet.")