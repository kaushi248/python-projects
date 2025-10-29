name=input("enter your name:")
print("welcome to my game!", name)

should_we_play=input("Do you want to play?").lower()

if should_we_play =="yes" or should_we_play!="y":
    print("we r gonna play!")
    
    weapon=input("choose a weapon(sword/axe):").lower()
    if weapon=="sword":
        print("you have chosen the sword!")
    elif weapon=="axe":
        print("you have chosen the axe!")

    else:
        print("invalid weapon, you get a stick!")

    direction=input("you r in a forest, do you want to go left or right?").lower()
    if direction=="left":
        print("you have encountered a monster and lost the game!")
    elif direction=="right":
        choice=input("you have encountered a monster, do you want to fight or run?").lower()
        if choice=="fight" and weapon=="sword":
            print("you have defeated the monster and won the game!")
        elif choice=="fight" and weapon=="axe":
            print("the monster has defeated you, you lost the game!")
        else:
            print("you ran away safely, but you didnt win the gold!")
    else:
        print("invalid direction, you tripped and lost the game!")

else:
    print("maybe next time!")

        



            

        

