from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    my_taxi = None

    menu = "Lets drive! \nq)uit, c)hoose taxi, d)rive"
    print(menu)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            counter = 0
            for i in taxis:
                print("{} - {}".format(counter, i))
                counter += 1
            taxi_choice = int(input("Choose taxi:"))
            if taxi_choice == 0:
                my_taxi = taxis[0]
            elif taxi_choice == 1:
                my_taxi = taxis[1]
            else:
                my_taxi = taxis[2]
            print("Bill to date is ${:.2f}".format(bill))
        elif menu_choice == "d":
            my_taxi.start_fare()
            drive_distance = int(input("Drive how far? "))
            my_taxi.drive(drive_distance)
            taxi_cost = my_taxi.get_fare()
            print("Your {} trip will cost you ${:.2f}".format(my_taxi.name, taxi_cost))
            bill += taxi_cost
            print("Bill to date is ${:.2f}".format(bill))
        print(menu)
        menu_choice = input(">>> ").lower()
    print("Total trip cost is ${:.2f}".format(bill))
    print("Taxis are now:")
    counter = 0
    for i in taxis:
        print("{} - {}".format(counter, i))
        counter += 1


# print(menu)


main()
