def odd_or_even(command, list_of_numbers):
    if command == "Odd":
        odd_nums = [num for num in list_of_numbers if not num % 2 == 0]
        print(sum(odd_nums) * len(list_of_numbers))
    elif command == "Even":
        even_nums = [num for num in list_of_numbers if num % 2 == 0]
        print(sum(even_nums) * len(list_of_numbers))


cmd = input()
numbers = list(map(int, input().split(" ")))
odd_or_even(cmd, numbers)
