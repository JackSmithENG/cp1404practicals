def main():
    """ Jack Smith """
    import random

    min_length = random.randint(5, 20)
    password = get_password(min_length)

    print_passsword(password)

    print("\nYour password is valid")


def print_passsword(password):
    for i in password:
        print("*", end=" ")


def get_password(min_length):
    password = input("Please enter your {} character minimum password password: ".format(min_length))
    while len(password) < min_length:
        print("Password must be at least {} characters long".format(min_length))
        password = input("Please enter your {} character minimum password password: ".format(min_length))
    return password


main()
