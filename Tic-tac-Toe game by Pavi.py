# Initialize the game board as a 3x3 grid
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board():
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if a player has won
def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Main game loop
current_player = 'X'
while True:
    print_board()
    print(f"Player {current_player}'s turn:")
    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))

    # Check if the chosen cell is empty
    if board[row][col] == ' ':
        board[row][col] = current_player
    else:
        print("That cell is already occupied. Try again.")
        continue

    # Check for a win or a draw
    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins! Congratulations!")
        break
    elif all(cell != ' ' for row in board for cell in row):
        print_board()
        print("It's a draw!")
        break

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'
