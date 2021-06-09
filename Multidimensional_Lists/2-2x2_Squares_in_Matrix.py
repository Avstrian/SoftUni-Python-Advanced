rows, columns = list(map(int, input().split(" ")))
matrix = []
all_equals = 0

for row in range(0, rows):
    matrix.append(list(input().split(" ")))

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            all_equals += 1

print(all_equals)