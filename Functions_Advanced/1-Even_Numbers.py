def even_numbers(list_of_nums):
    even = filter(lambda x: x % 2 == 0, list_of_nums)
    print(list(even))


numbers = list(map(int, input().split(" ")))
even_numbers(numbers)
