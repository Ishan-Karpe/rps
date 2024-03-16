import random

user_wins = 0
computer_wins = 0

options = ["r", "p", "s"]

while True:
    user_input = input("Enter your choice (r, p, s): ").lower()
    if user_input == "q":
        quit()
        
    if user_input not in options:
        print("Please enter a valid input")
        continue
    
    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_num]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "r" and computer_pick == "s":
        print("You won!")
        user_wins += 1
    elif user_input == "p" and computer_pick == "r":
        print("You won!")
        user_wins += 1
        
    elif user_input == "s" and computer_pick == "p":
        print("You won!")
        user_wins += 1
        
    else:
        print("You lost!")
        computer_wins += 1
        
        print("You have", user_wins, "wins.")
        print("Computer has", computer_wins, "wins.")