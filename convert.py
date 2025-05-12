distances = {
    "voyager 1": 163,
    "voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for name in distances.values():
        print(f"{name} is {convert(name)} m")



def convert(au):
    return au * 1459646431100


main()    