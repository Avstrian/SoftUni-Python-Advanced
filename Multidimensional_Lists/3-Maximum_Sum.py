rows, cols = list(map(int, input().split(" ")))
matrix = []
biggest_sum = 0
biggest_list = []

for i in range(rows):
    matrix.append(list(map(int, input().split(" "))))

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        current_list = [matrix[row][col], matrix[row][col+1], matrix[row][col+2],
                        matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2],
                        matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]

        if biggest_sum is None or sum(current_list) > biggest_sum:
            biggest_sum = sum(current_list)
            biggest_list = current_list

print(f"Sum = {biggest_sum}")
for j in range(0, len(biggest_list), 3):
    print(biggest_list[j], biggest_list[j+1], biggest_list[j+2], sep=" ")
