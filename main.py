import random

user_score = 0
computer_score = 0
draw = 0

choices = ['r', 'p', 's']

while True:

    print('''
    1. Rock    (r)✊
    2. Paper   (p)✋
    3. Scissor (s)✌️
    ''')
    user_choice = input("Enter your choice(r/p/s): ").lower().strip()

    if user_choice not in choices:
        print("Invalid choice! Please enter r, p, or s.")
    else:
            
        print(f"You chose: {user_choice}")
        print("Now it's Computer's Turn...")

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        print(f"{user_choice} vs {computer}")
        if user_choice == computer:
            draw += 1
            print("<== It's a Draw! ==>")

        elif ((user_choice == 'r' and computer == 's') or  
            (user_choice == 's' and computer == 'p') or 
            (user_choice == 'p' and computer == 'r')):
            user_score += 1
            print("<== You Wins! ==>")

        else:
            computer_score += 1
            print("<== Computer Wins! ==>")

    play_again = input("Play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print("FINAL SCOREBOARD")
        print(f"User Score\tComputer Score\n    {user_score}\t\t    {computer_score}\n")
        if user_score > computer_score:
            print("User Winner!")
        elif user_score < computer_score:
            print("Computer Winner!")
        else:
            print("Match Draw!")
        break
        

