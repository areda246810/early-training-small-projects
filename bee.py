words = {"HAIR":4 , "PAIR":4 , "CHAIR":5 , "GRAPHICS" : 7}


def main():


    print("welcome to spelling bee")
    print("your letters are A I P C R H G")


    for key,value in words.items():
        print(f"{key} is worth {value} points")


    while len(words) > 0:
        print(f"{len(words)} words are left")
        guess = input("guess a word : ").upper()


        if guess == "GRAPHICS":
            words.clear()
            print("CRITICAL ROLE !!!!!")


        if guess in words.keys():
            points = words.pop(guess)
            print(f"congrats you scored {points} points !")

    print("That's the game !")  


main()