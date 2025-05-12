def main():

    program = input("what's your name ? ").title()
    program1 = replace_with_dots(program)
    print(f"hello {program1} have a lovely day !")


def replace_with_dots(text):
    return text.replace(" ", "...")    


main()