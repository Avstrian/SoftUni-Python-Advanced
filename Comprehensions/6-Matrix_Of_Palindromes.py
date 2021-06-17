rows, columns = list(map(int, input().split(" ")))
matrix = []
letter = 97
middle_letter = 97

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(f"{chr(letter)}{chr(middle_letter)}{chr(letter)}")
        middle_letter += 1
    letter += 1
    middle_letter = letter

[print(" ".join(el)) for el in matrix]
