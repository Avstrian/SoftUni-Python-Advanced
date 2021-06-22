def negative_vs_positive(list_of_nums):
    negatives = [num for num in list_of_nums if num < 0]
    positives = [num for num in list_of_nums if num >= 0]
    print(sum(negatives))
    print(sum(positives))
    if abs(sum(negatives)) > abs(sum(positives)):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = list(map(int, input().split(" ")))
negative_vs_positive(numbers)
