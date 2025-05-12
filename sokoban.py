def main():
    history = []

    while True:
        action = input("enter action: ")
        
        if action == "undo":
            undone = history.pop()
            print(f'{undone} was removed')

        elif action == "restart":
            history.clear()
            print('game has been reset')    

        else:    
            history.append(action)

        print(history)


main()