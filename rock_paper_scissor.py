import random

def get_computer_choice():
    """Computer randomly chooses rock, paper, or scissors"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    """Determine the winner based on game rules"""
    if player == computer:
        return "It's a tie!"
    
    # Player wins scenarios
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main game function"""
    print("=" * 40)
    print("Welcome to Rock Paper Scissors!")
    print("=" * 40)
    
    player_score = 0
    computer_score = 0
    
    while True:
        print("\nChoose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            continue
        
        # Convert choice to weapon name
        choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        player_choice = choices[choice]
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Update scores
        if "You win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")

# Run the game
if __name__ == "__main__":
    play_game()