def display_board(board):
    """Displays the current state of the Tic-Tac-Toe board in a friendly way."""
    print("\nHere's the current board:")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()  # Adding a blank line for readability

def check_win(board, marker):
    """Checks if the current player has won the game."""
    # All possible winning combinations (rows, columns, diagonals)
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == marker:
            return True
    return False

def is_board_full(board):
    """Checks if the board is full, which means it's a draw."""
    return all(space in ['X', 'O'] for space in board)

def get_player_move(board, player):
    """Asks the player for their move and ensures it's valid."""
    while True:
        try:
            move = int(input(f"{player}, it's your turn! Pick a spot (1-9): "))
            if 1 <= move <= 9 and board[move - 1] not in ['X', 'O']:
                return move - 1  # Convert to 0-based index
            else:
                print("Oops! That spot is either taken or doesn't exist. Try again!")
        except ValueError:
            print("Hmm, that's not a valid number. Please pick a number between 1 and 9.")

def play_game():
    """The main function to run the Tic-Tac-Toe game."""
    print("🌟 Welcome to Tic-Tac-Toe! 🌟")
    print("This is a two-player game where you take turns marking spots on the board.")
    print("Player 1 will be X, and Player 2 will be O. Let's get started!\n")

    # Ask for player names
    player1 = input("Player 1, what's your name? (You'll be X): ") or "Player 1"
    player2 = input("Player 2, what's your name? (You'll be O): ") or "Player 2"
    score = {player1: 0, player2: 0}  # Keep track of scores

    while True:  # Outer loop for multiple rounds
        # Reset the board for a new round
        board = [str(i) for i in range(1, 10)]
        turn = 0  # 0 for Player 1, 1 for Player 2

        while True:  # Inner loop for each turn
            display_board(board)
            current_player = player1 if turn == 0 else player2
            marker = 'X' if turn == 0 else 'O'

            # Get the player's move
            move = get_player_move(board, current_player)
            board[move] = marker

            # Check if the current player has won
            if check_win(board, marker):
                display_board(board)
                print(f"🎉 Congratulations, {current_player}! You won this round! 🎉")
                score[current_player] += 1
                print(f"Score update: {player1}: {score[player1]} | {player2}: {score[player2]}")
                break
            # Check if the board is full (draw)
            elif is_board_full(board):
                display_board(board)
                print("\nIt's a draw! Nobody wins this time. 🤝")
                break

            turn = 1 - turn  # Switch turns

        # Ask if they want to play another round
        play_again = input("\nWould you like to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Here are the final scores:")
            print(f"{player1}: {score[player1]} | {player2}: {score[player2]}")
            print("Hope you had fun! See you next time! 👋")
            break

# Start the game
if __name__ == "__main__":
    play_game()
