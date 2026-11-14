import random



choices = ['r', 'p', 's']
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
        print("<== It's a Draw! ==>")

    elif ((user_choice == 'r' and computer == 's') or  
        (user_choice == 's' and computer == 'p') or 
        (user_choice == 'p' and computer == 'r')):
        print("<== You Wins! ==>")

    else:
        
        print("<== Computer Wins! ==>")

        

