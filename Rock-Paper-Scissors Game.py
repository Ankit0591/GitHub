import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    def get_computer_choice():
        return random.choice(choices)
    
    def get_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'
    
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Enter 'rock', 'paper', or 'scissors' to play.")
        print("Enter 'exit' to quit the game.")
        
        user_choice = input("Your choice: ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")
        
        winner = get_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        print(f"Score: You {user_score} - {computer_score} Computer")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

rock_paper_scissors()
