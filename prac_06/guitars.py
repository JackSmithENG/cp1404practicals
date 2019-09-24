from prac_06.guitar_class_file import Guitar


def main():
    guitars = []
    name = "John"
    # name = input("Please enter guitar name: ")
    while name != "":
        # year = int(input("Year:"))
        year = 2015
        # cost = float(input("Cost: "))
        cost = 20
        new_guitar = Guitar(name, year, cost)
        print(new_guitar)
        guitars.append(new_guitar)
        print("{} added".format(new_guitar))
        # print(guitars)
        name = input("Please enter guitar name: ")

    for i in guitars:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, )
        # print(guitars)


main()
