def print_board(board):
    """Display the current game board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def print_positions():
    """Show position numbers to help players"""
    print("\nPosition numbers:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n")

def check_winner(board, player):
    """Check if the given player has won"""
    # Winning combinations (indices)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    """Check if the board is completely filled"""
    return all(space != ' ' for space in board)

def get_player_move(board, player):
    """Get valid move from player"""
    while True:
        try:
            move = input(f"Player {player}, enter position (1-9): ").strip()
            move = int(move)
            
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            
            # Convert to 0-indexed
            index = move - 1
            
            if board[index] != ' ':
                print("That position is already taken! Choose another.")
                continue
            
            return index
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def play_game():
    """Main game function"""
    print("=" * 40)
    print("Welcome to Tic Tac Toe!")
    print("=" * 40)
    print_positions()
    
    while True:
        # Initialize game
        board = [' '] * 9
        current_player = 'X'
        
        # Game loop
        while True:
            print_board(board)
            
            # Get player move
            move = get_player_move(board, current_player)
            board[move] = current_player
            
            # Check for winner
            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins! 🎉")
                break
            
            # Check for tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie! The board is full.")
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()