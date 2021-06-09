rows, columns = list(map(int, input().split(" ")))
snake = input()
matrix = []
symbol = 0

for i in range(rows):
    matrix.append([])
    if i % 2 == 0 or i == 0:
        for j in range(columns):
            matrix[i].append(snake[symbol])
            symbol += 1
            if symbol >= len(snake):
                symbol = 0
    else:
        for j in range(columns - 1, -1, -1):
            matrix[i].append(snake[symbol])
            symbol += 1
            if symbol == len(snake):
                symbol = 0
        matrix[i].reverse()

for index in range(len(matrix)):
    for subindex in range(len(matrix[index])):
        print(matrix[index][subindex], end="")
    print()
