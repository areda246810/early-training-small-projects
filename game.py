def main():
    players=input("single or multi ? ")
    difficulty = input("easy or hard ? ")

    if players == "single":
        if difficulty == "easy":
            recommend("skyrim")
        elif difficulty == "hard":
            recommend("dark souls")
        else:
            print("please enter a valid difficulty")    

    elif players == "multi":
        if difficulty == "easy":
            recommend("pubg")
        elif difficulty == "hard":
            recommend("lol")
        else:
            print("enter a valid difficulty")        
    else:
        print("please enter a valid number of players")        








def recommend(game):
    print("your game might be " , game )


main()    
