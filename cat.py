def main():

    players = input("please enter type of player : ")
    if not (players == "single player" or players == "multiplayer"):
        print("please enter correct numbers of players")
        return

    diffculty = input ("please enter required difficulty: ")
    if not (diffculty == "easy" or diffculty == "hard"):
        print ("please enter a correct diffculty")
        return


    if players == "single player" and diffculty == "easy":
        recommend("skyrim")
    elif players == "single player" and diffculty == "hard":
        recommend("dark souls")
    elif players == "multiplayer" and diffculty == "easy":
        recommend ("Pubg")


    else:
        recommend("LOL")
      




def recommend(game):
    print("your game might be : " , game) 
    
main()