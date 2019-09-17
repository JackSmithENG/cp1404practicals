from prac_06.guitar_class_file import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)

    another_name = "Gut tar"
    another_year = 2015
    another_cost = 10
    another_guitar = Guitar(another_name, another_year, another_cost)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 97, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 4, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))


main()
