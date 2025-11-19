class CheckersGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = 'R'  # R for Red, B for Black
        self.must_capture = None  # For multi-jump scenarios
        
    def create_board(self):
        """Initialize the checkers board"""
        board = [[' ' for _ in range(8)] for _ in range(8)]
        
        # Place black pieces (top)
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'b'
        
        # Place red pieces (bottom)
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'r'
        
        return board
    
    def print_board(self):
        """Display the current board state"""
        print("\n   0 1 2 3 4 5 6 7")
        print("  ┌─────────────────┐")
        for i, row in enumerate(self.board):
            print(f"{i} │", end=" ")
            for cell in row:
                print(cell, end=" ")
            print("│")
        print("  └─────────────────┘")
        print("\nLegend: r=red piece, R=RED KING, b=black piece, B=BLACK KING\n")
    
    def is_valid_position(self, row, col):
        """Check if position is within board boundaries"""
        return 0 <= row < 8 and 0 <= col < 8
    
    def get_piece(self, row, col):
        """Get piece at position"""
        if self.is_valid_position(row, col):
            return self.board[row][col]
        return None
    
    def is_player_piece(self, row, col, player):
        """Check if piece belongs to current player"""
        piece = self.get_piece(row, col)
        if player == 'R':
            return piece in ['r', 'R']
        else:
            return piece in ['b', 'B']
    
    def is_king(self, row, col):
        """Check if piece is a king"""
        piece = self.get_piece(row, col)
        return piece in ['R', 'B']
    
    def promote_to_king(self, row, col):
        """Promote piece to king if it reaches the opposite end"""
        piece = self.board[row][col]
        if piece == 'r' and row == 0:
            self.board[row][col] = 'R'
        elif piece == 'b' and row == 7:
            self.board[row][col] = 'B'
    
    def get_valid_moves(self, row, col):
        """Get all valid moves for a piece"""
        moves = []
        captures = []
        piece = self.get_piece(row, col)
        
        if piece == ' ':
            return moves, captures
        
        is_king = self.is_king(row, col)
        player = self.current_player
        
        # Determine movement directions
        if player == 'R' or is_king:
            directions = [(-1, -1), (-1, 1)]  # Up-left, up-right
        if player == 'B' or is_king:
            if player == 'B':
                directions = [(1, -1), (1, 1)]  # Down-left, down-right
            else:
                directions.extend([(1, -1), (1, 1)])
        
        # Check each direction
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Regular move
            if self.is_valid_position(new_row, new_col) and self.board[new_row][new_col] == ' ':
                moves.append((new_row, new_col))
            
            # Capture move
            jump_row, jump_col = row + 2*dr, col + 2*dc
            if self.is_valid_position(new_row, new_col) and self.is_valid_position(jump_row, jump_col):
                middle_piece = self.board[new_row][new_col]
                if middle_piece != ' ' and not self.is_player_piece(new_row, new_col, player):
                    if self.board[jump_row][jump_col] == ' ':
                        captures.append((jump_row, jump_col, new_row, new_col))
        
        return moves, captures
    
    def make_move(self, from_row, from_col, to_row, to_col):
        """Execute a move"""
        piece = self.board[from_row][from_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = ' '
        
        # Check if it's a capture
        if abs(to_row - from_row) == 2:
            # Remove captured piece
            mid_row = (from_row + to_row) // 2
            mid_col = (from_col + to_col) // 2
            self.board[mid_row][mid_col] = ' '
            
            # Check for additional captures
            _, more_captures = self.get_valid_moves(to_row, to_col)
            if more_captures:
                self.must_capture = (to_row, to_col)
                return True  # More captures available
        
        # Promote to king if reached opposite end
        self.promote_to_king(to_row, to_col)
        self.must_capture = None
        return False
    
    def has_any_captures(self, player):
        """Check if player has any capture moves available"""
        for row in range(8):
            for col in range(8):
                if self.is_player_piece(row, col, player):
                    _, captures = self.get_valid_moves(row, col)
                    if captures:
                        return True
        return False
    
    def check_winner(self):
        """Check if there's a winner"""
        red_pieces = 0
        black_pieces = 0
        
        for row in self.board:
            for cell in row:
                if cell in ['r', 'R']:
                    red_pieces += 1
                elif cell in ['b', 'B']:
                    black_pieces += 1
        
        if red_pieces == 0:
            return 'B'
        elif black_pieces == 0:
            return 'R'
        return None
    
    def play(self):
        """Main game loop"""
        print("=" * 50)
        print("Welcome to Checkers!")
        print("=" * 50)
        print("Red (r/R) moves first. Captures are mandatory!")
        
        while True:
            self.print_board()
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                player_name = "Red" if winner == 'R' else "Black"
                print(f"🎉 {player_name} wins! 🎉")
                break
            
            player_name = "Red" if self.current_player == 'R' else "Black"
            print(f"{player_name}'s turn")
            
            # Check if must continue capturing
            if self.must_capture:
                from_row, from_col = self.must_capture
                print(f"You must continue capturing with piece at ({from_row}, {from_col})")
            else:
                # Get piece to move
                try:
                    from_input = input("Enter piece position (row col) or 'q' to quit: ").strip()
                    if from_input.lower() == 'q':
                        print("Thanks for playing!")
                        return
                    
                    from_row, from_col = map(int, from_input.split())
                    
                    if not self.is_player_piece(from_row, from_col, self.current_player):
                        print("Invalid piece! Choose your own piece.")
                        continue
                except:
                    print("Invalid input! Use format: row col (e.g., 5 0)")
                    continue
            
            # Get valid moves
            moves, captures = self.get_valid_moves(from_row, from_col)
            
            # Force capture if available
            if self.has_any_captures(self.current_player) and not captures:
                print("You must make a capture move!")
                self.must_capture = None
                continue
            
            if captures:
                print(f"Available captures: {[(c[0], c[1]) for c in captures]}")
                available = captures
                is_capture = True
            elif moves:
                print(f"Available moves: {moves}")
                available = moves
                is_capture = False
            else:
                print("No valid moves for this piece!")
                self.must_capture = None
                continue
            
            # Get destination
            try:
                to_input = input("Enter destination (row col): ").strip()
                to_row, to_col = map(int, to_input.split())
                
                # Validate move
                if is_capture:
                    valid = any(c[0] == to_row and c[1] == to_col for c in captures)
                else:
                    valid = (to_row, to_col) in moves
                
                if not valid:
                    print("Invalid move!")
                    continue
                
                # Make the move
                more_captures = self.make_move(from_row, from_col, to_row, to_col)
                
                # Switch player if no more captures
                if not more_captures:
                    self.current_player = 'B' if self.current_player == 'R' else 'R'
                else:
                    print("You can capture again!")
                    
            except:
                print("Invalid input! Use format: row col (e.g., 4 1)")
                continue

# Run the game
if __name__ == "__main__":
    game = CheckersGame()
    game.play()