import random

def get_player_choice():
    """Prompt the player to enter their choice and validate it."""
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the round."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the game."""
    player_score = 0
    rounds = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print("Computer chooses:", computer_choice)

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1

        rounds += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over!")
    print("Your score:", player_score, "/", rounds)

if __name__ == "__main__":
    play_game()
