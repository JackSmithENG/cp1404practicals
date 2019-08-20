"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when any non-integer is entered.

2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when the denominator is set to 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding a while loop that will ask the user for a non-zero answer that will break when
    denominator =! 0.

"""
finished = False
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        # while denominator == 0:
        #   print("Denominator cannot be 0!")
        #   denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        finished = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")
