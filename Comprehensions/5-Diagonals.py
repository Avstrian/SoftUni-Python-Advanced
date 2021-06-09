matrix = [input().split(", ") for j in [i for i in range(0, int(input()))]]
first_diag = [[num for num in row if int(num) == row] for row in matrix]
print(first_diag)
#asdasdsadsa