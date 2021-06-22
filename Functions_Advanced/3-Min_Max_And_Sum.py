def min_max_sum(list_of_nums):
    print(f"The minimum number is {min(list_of_nums)}")
    print(f"The maximum number is {max(list_of_nums)}")
    print(f"The sum number is: {sum(list_of_nums)}")


numbers = list(map(int, input().split(" ")))
min_max_sum(numbers)
