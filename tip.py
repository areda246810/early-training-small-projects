def main():
    dollars=dollars_to_float(input("how much was the meal? "))
    percentage=percentage_to_float(input("how much would you like to tip? "))
    percent = percentage / 100
    tip = dollars * percent
    print(f"your tip is {tip:0.2f}$")


def dollars_to_float(d):
    return float(d.replace("$"," "))


def percentage_to_float(p):
    return float(p.replace("%" ," " ))


main()