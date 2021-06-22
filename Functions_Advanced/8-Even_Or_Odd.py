def even_odd(*args):
    if args[-1] == "even":
        even_nums = [num for num in args if not num == args[-1] and num % 2 == 0]
        return even_nums

    if args[-1] == "odd":
        odd_nums = [num for num in args if not num == args[-1] and not num % 2 == 0]
        return odd_nums
