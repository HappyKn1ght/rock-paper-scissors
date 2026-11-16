import random

def print_line():
    print("-" * 40)

user_score = 0
computer_score = 0
draw = 0

choices = ['r', 'p', 's']
fullName = {"r": "Rock", "p": "Paper", "s": "Scissors" }

# Display game rules
print("=== ROCK PAPER SCISSORS ===")
print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

while True:
    
    print('''
    1. Rock    (r)✊
    2. Paper   (p)✋
    3. Scissor (s)✌️
    ''')
    user_choice = input("Enter your choice(r/p/s): ").lower().strip()

    if user_choice not in choices:
        print("Invalid choice! Please enter r, p, or s.")
        continue
            
    print(f"You chose: {fullName[user_choice]}")
    print("Now it's Computer's Turn...")

    computer = random.choice(choices)
    print(f"Computer chose: {fullName[computer]}")

    print(f"{fullName[user_choice]} vs {fullName[computer]}")
    if user_choice == computer:
        draw += 1
        print("<== It's a Draw! ==>")

    elif ((user_choice == 'r' and computer == 's') or  
        (user_choice == 's' and computer == 'p') or 
        (user_choice == 'p' and computer == 'r')):
        user_score += 1
        print("<== You Win! ==>")

    else:
        computer_score += 1
        print("<== Computer Wins! ==>")

    play_again = input("Play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print_line()
        print("FINAL SCOREBOARD")
        print_line()

        print(f"User Score  Computer Score  Match Draw\n   {user_score}\t\t  {computer_score}\t\t{draw}\n")
        if user_score > computer_score:
            print_line()
            print("🏆 You Are the Overall Winner!")
            print_line()
        elif user_score < computer_score:
            print_line()
            print("💻 Computer Wins the Match!")
            print_line()
        else:
            print_line()
            print("🤝 Overall Match Draw!")
            print_line()
        break

print("\nThanks for playing!")        

