total_apples = 21

while total_apples > 0:

    player_pick = int(input(" apples  to pick (1-4)? "))
    while player_pick < 1 or player_pick > 4 or player_pick > total_apples:
        print("Invalid input")
        player_pick = int(input("apples to pick (1-4)? "))
    
    total_apples -= player_pick
    print(f"You picked {player_pick} apple(s).")
    print(f"Remaining apples  : {total_apples} \n")
     
    if total_apples <= 0:
        print("You picked the last ! you lost")
        break
    

    total_apples -= computer_pick
    print(f"The computer picked {computer_pick} apple(s).")
    print(f"Remaining apples: {total_apples}\n")
    
    if total_apples <= 0:
        print("The computer picked the last apple ! you won")
        break
