matrix = [list(map(int, input().split(" "))) for row in range(int(input()))]


command = input().split(" ")
while not command[0] == "END":
    r = int(command[1])
    c = int(command[2])
    value = int(command[3])

    if command[0] == "Add":
        if 0 <= r <= len(matrix) - 1:
            if 0 <= c <= len(matrix[r]):
                matrix[r][c] += value
            else:
                print("Invalid coordinates")
        else:
            print("Invalid coordinates")

    if command[0] == "Subtract":
        if 0 <= r <= len(matrix) - 1:
            if 0 <= c <= len(matrix[r]):
                matrix[r][c] -= value
            else:
                print("Invalid coordinates")
        else:
            print("Invalid coordinates")

    command = input().split(" ")

matrix_as_strings = [[str(el) for el in row] for row in matrix]
[print(f"{' '.join(row)}") for row in matrix_as_strings]
