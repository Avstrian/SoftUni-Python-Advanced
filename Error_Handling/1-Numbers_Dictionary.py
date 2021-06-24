numbers_dictionary = {}

line = input()
while not line == "Search":
    num_as_digit = input()
    try:
        int(num_as_digit)
    except ValueError:
        print("The variable number must be an integer")

    else:
        numbers_dictionary[line] = num_as_digit

    line = input()


command = input()
while not command == "Remove":
    try:
        print(numbers_dictionary[command])
    except KeyError:
        print("Number does not exist in dictionary")

    command = input()


num_to_remove = input()
while not num_to_remove == "End":
    try:
        numbers_dictionary.pop(num_to_remove)
    except KeyError:
        print("Number does not exist in dictionary")

    num_to_remove = input()

print(numbers_dictionary)
