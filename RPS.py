import random 

print("\n\t\t\tRock Paper Scissors - The game\n")
player_name = input("Enter Your name\t>>>")
print("Welcome", player_name)
print('''
    Rules:
        - Choose Either Rock, Paper or Scissors. Anything aside that would be considered as an error.(NOTE: You can only make such error a minimum of 5 times )
        To win, know that:
        - Rock beats Scissors
        - Paper beats Rock
        - Scissors beats Paper
    ''')

while True:
    avail_choices = ["R", "P", "S"]
    computer_choice = random.choice(avail_choices).upper()
    player_choice_count = 0
    
    while player_choice_count <= 4:
         player_choice = input("\t****Enter your choice \n 'r' for Rock\n 'p' for Paper\n 's' for Scissors****\n>>").upper()
         player_choice_count += 1
         if player_choice in avail_choices:
            break
         else:
            print("Please enter a valid choice")
            continue
    else:
        print("\n!!!You clearly do not understand the scope of this game \t \n \t---Read the rules again and try again---")
                
                
    print(f"\t\tPlayer-{player_name}({player_choice}):CPU({computer_choice})\n") 
    
    if computer_choice == player_choice:
        print("\t It's a tie! \nYou and the computer picked the same thing")
            
    if player_choice == "R" and computer_choice == "P":
            print("[Paper covers Rock]")
            print("Computer WINS!!!")
            
    if player_choice == "P" and computer_choice == "R":
        print("[Paper covers Rock]")
        print(f"{player_name} WINS!!!")
        
    if player_choice == "S" and computer_choice == "R":
        print("[Rock Smashes Scissors]")
        print("Computer WINS!!!")
        
    if player_choice == "R" and computer_choice == "S":
        print("[Rock smashes Scissors]")
        print(f"{player_name} WINS!!!")
        
    if player_choice == "P" and computer_choice == "S":
        print("[Scissors cut Paper]")
        print("Computer WINS!!!")
        
    if player_choice == "S" and computer_choice == "P":
        print("[Scissors cut Paper]")
        print(f"{player_name} WINS!")
    
    end_game = input("Would you like to Play Again?\n ---Enter either Yes or 1 or Y to continue---\n Enter either No or 2 or N to quit game--- \n\t >>").lower()
    if end_game == "2" or end_game == "no" or end_game == "n":
        print("\n\n****Thanks for playing!****")
        break
