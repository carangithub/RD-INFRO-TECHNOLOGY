ximport random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("-------------------------")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3): ")

        if user_choice == "4":
            print("\nFinal Score:")
            print(f"User: {user_score}")
            print(f"Computer: {computer_score}")
            break

        try:
            user_choice = ["rock", "paper", "scissors"][int(user_choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nUser chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("User wins this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScore - User: {user_score}, Computer: {computer_score}")

        play_again = input("\nPlay again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()