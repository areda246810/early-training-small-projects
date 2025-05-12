def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("how many time do you want me to meow? "))
        if n > 0 :
            break
        else:
            return n 

def meow(n):
    for _ in range(n):
        print ("meow")   


main()