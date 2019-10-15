from prac_08.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    test_car = UnreliableCar("Test Car", 100, 60)

    for i in range(1, 8):
        print("Attempting to drive {}km:".format(i))
        print("{} drove {}km".format(test_car.name, test_car.drive(i)))

    print(test_car)


main()
