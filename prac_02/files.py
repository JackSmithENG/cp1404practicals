# OUTPUT_FILE_NAME = 'name.txt'  # Name the output file
# out_file_name = open(OUTPUT_FILE_NAME, 'w')  # Write to output file
#
# user_name = input("Enter your name: ")
# print(user_name.format(), file=out_file_name)
#
# in_file_name = open('name.txt', 'r')
# name = in_file_name.read().strip()
# print("Your name is", user_name, file=out_file_name)
# in_file_name.close()
#
# in_file_numbers = open('numbers.txt', 'r+')
# number1 = int(in_file_numbers.readline())
# number2 = int(in_file_numbers.readline())
# sum_of_file = number1 + number2
# print("Sum = {}".format(sum_of_file), file=in_file_numbers)
# in_file_numbers.close()
# out_file_name.close()

in_file_multiple_numbers = open('multiple_numbers.txt', 'r+')
finished = False
sum_total = 0
while not finished:
    try:
        current_line_number = int(in_file_multiple_numbers.readline())
        sum_total = sum_total + current_line_number
    except ValueError:
        finished = True
print("Sum = {}".format(sum_total), file=in_file_multiple_numbers)
