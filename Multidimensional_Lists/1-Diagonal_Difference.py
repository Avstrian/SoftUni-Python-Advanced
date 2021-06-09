rows = int(input())
matrix = []
diag1 = 0
diag2 = 0
col = 0

for row in range(0, rows):
    matrix.append(list(map(int, input().split(" "))))
    diag1 += matrix[row][row]


for row in range(rows-1, -1, -1):
    diag2 += matrix[row][col]
    col += 1

if diag1 > diag2:
    print(diag1 - diag2)
else:
    print(diag2 - diag1)