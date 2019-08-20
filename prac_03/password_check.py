def main():
    """ Jack Smith """
    import random

    finished = False
    min_length = random.randint(5, 20)
    password = get_password(finished, min_length)

    print_passsword(password)

    print("\nYour password is valid")


def print_passsword(password):
    for i in password:
        print("*", end=" ")


def get_password(finished, min_length):
    while not finished:
        password = input("Please enter your {} character minimum password password: ".format(min_length))
        if len(password) < min_length:
            print("Password must be at least {} characters long".format(min_length))
        else:
            finished = True
    return password


main()