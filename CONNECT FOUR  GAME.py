import random

print("Welcome to Connect Four")
print("-----------------------")

# Constants
ROWS = 6
COLS = 7
POSSIBLE_COLUMNS = ["A", "B", "C", "D", "E", "F", "G"]

# Initialize the game board with empty strings
game_board = [["" for _ in range(COLS)] for _ in range(ROWS)]

# Function to print the game board
def print_game_board():
    print("\n     A    B    C    D    E    F    G")
    for row in range(ROWS):
        print("   +----+----+----+----+----+----+----+")
        print(row, " |", end="")
        for col in range(COLS):
            if game_board[row][col] == "🔵":
                print("", game_board[row][col], end=" |")
            elif game_board[row][col] == "🔴":
                print("", game_board[row][col], end=" |")
            else:
                print("  ", end=" |")
        print("")
    print("   +----+----+----+----+----+----+----+")

# Function to modify the board based on the player's move
def drop_piece(col, piece):
    for row in reversed(range(ROWS)):
        if game_board[row][col] == "":
            game_board[row][col] = piece
            return True
    return False

# Function to check if the move is valid
def is_valid_move(col):
    return game_board[0][col] == ""

# Function to convert column letter to index
def letter_to_index(letter):
    return POSSIBLE_COLUMNS.index(letter.upper())

# Function to check for a win condition
def check_win(piece):
    # Check horizontal locations for win
    for c in range(COLS - 3):
        for r in range(ROWS):
            if game_board[r][c] == piece and game_board[r][c + 1] == piece and game_board[r][c + 2] == piece and game_board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLS):
        for r in range(ROWS - 3):
            if game_board[r][c] == piece and game_board[r + 1][c] == piece and game_board[r + 2][c] == piece and game_board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if game_board[r][c] == piece and game_board[r + 1][c + 1] == piece and game_board[r + 2][c + 2] == piece and game_board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if game_board[r][c] == piece and game_board[r - 1][c + 1] == piece and game_board[r - 2][c + 2] == piece and game_board[r - 3][c + 3] == piece:
                return True

    return False

# Game loop
turn_counter = 0
game_over = False

while not game_over:
    print_game_board()

    # Determine whose turn it is
    if turn_counter % 2 == 0:
        print("Player 1 (🔵), it's your turn.")
        player_piece = "🔵"
    else:
        print("Player 2 (🔴), it's your turn.")
        player_piece = "🔴"

    # Ask the player to choose a column
    column_letter = input("Choose a column (A-G): ").upper()

    # Ensure the input is valid
    if column_letter not in POSSIBLE_COLUMNS:
        print("Invalid input. Please choose a column between A and G.")
        continue

    column_index = letter_to_index(column_letter)

    if not is_valid_move(column_index):
        print("Column is full. Please choose a different column.")
        continue

    # Drop the piece on the board
    drop_piece(column_index, player_piece)

    # Check for a win condition
    if check_win(player_piece):
        print_game_board()
        print(f"Player {1 if turn_counter % 2 == 0 else 2} wins!")
        game_over = True

    turn_counter += 1

    # Check for a tie
    if turn_counter == ROWS * COLS and not game_over:
        print_game_board()
        print("The game is a tie!")
        game_over = True
