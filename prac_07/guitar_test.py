from prac_07.guitar import Guitar


def main():
    """"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson)

    anothr_guitar = Guitar("Another Guitar", 1999, 2000.048)
    print(anothr_guitar)


    gibson.get_age()
    anothr_guitar.get_age()
    print(gibson.get_age())
    print(anothr_guitar.get_age())

main()