rows, cols = list(map(int, input().split(" ")))
matrix = []

for i in range(rows):
    matrix.append(list(input().split(" ")))

command = input().split(" ")

while not command[0] == "END":
    swapping_list = []
    all_digits = True

    for cmd in range(1, len(command)):
        if not command[cmd].isdigit():
            all_digits = False

    if all_digits:
        if command[0] == "swap" and int(command[1]) <= rows and int(command[2]) <= cols and int(command[3]) <= rows \
                and int(command[4]) <= cols:
            swapping_list.append(matrix[int(command[1])][int(command[2])])
            swapping_list.append(matrix[int(command[3])][int(command[4])])
            matrix[int(command[1])][int(command[2])] = swapping_list[-1]
            matrix[int(command[3])][int(command[4])] = swapping_list[0]

            for i in range(len(matrix)):
                for j in range(0, len(matrix[i])):
                    print(matrix[i][j], end=" ")
                print()
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input().split(" ")
