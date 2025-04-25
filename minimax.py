import math

def print_board(board):
    for row in board:
        print(" | ".join(cell or " " for cell in row))
        print("-" * 9)

def check_winner(board):
    lines = board + list(map(list, zip(*board)))  # rows + columns
    lines.append([board[i][i] for i in range(3)])  # main diagonal
    lines.append([board[i][2-i] for i in range(3)])  # anti-diagonal
    for line in lines:
        if line[0] and all(cell == line[0] for cell in line):
            return line[0]
    if all(cell for row in board for cell in row):
        return "Draw"
    return None

def minimax(board, is_max, ai, human):
    winner = check_winner(board)
    if winner == ai:
        return 1, None
    elif winner == human:
        return -1, None
    elif winner == "Draw":
        return 0, None

    best = -math.inf if is_max else math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                board[i][j] = ai if is_max else human
                score, _ = minimax(board, not is_max, ai, human)
                board[i][j] = ""
                if is_max and score > best:
                    best = score
                    best_move = (i, j)
                elif not is_max and score < best:
                    best = score
                    best_move = (i, j)
    return best, best_move

def play_game():
    board = [["" for _ in range(3)] for _ in range(3)]
    player = input("Choose X or O: ").strip().upper()
    while player not in ['X', 'O']:
        player = input("Invalid. Choose X or O: ").strip().upper()

    ai = 'O' if player == 'X' else 'X'
    turn = 'X'

    while True:
        print_board(board)
        if turn == player:
            while True:
                try:
                    row, col = map(int, input("Enter row and column (0-2 space-separated): ").split())
                    if not board[row][col]:
                        board[row][col] = player
                        break
                    else:
                        print("Cell occupied.")
                except:
                    print("Invalid input.")
        else:
            print("AI is thinking...")
            _, move = minimax(board, True, ai, player)
            if move:
                board[move[0]][move[1]] = ai

        result = check_winner(board)
        if result:
            print_board(board)
            print("It's a draw!" if result == "Draw" else f"{result} wins!")
            break

        turn = ai if turn == player else player

if __name__ == "__main__":
    play_game()
