matrix = [input().split(", ") for j in [i for i in range(int(input()))]]

diag_1 = [str(matrix[row][num]) for row in range(0, len(matrix)) for num in range(len(matrix[row])) if row == num]
matrix.reverse()
diag_2 = [str(matrix[row][num]) for row in range(0, len(matrix)) for num in range(len(matrix[row])) if row == num]
diag_2.reverse()

print(f"First diagonal: {', '.join(diag_1)}. Sum: {sum(int(num) for num in diag_1)}")
print(f"Second diagonal: {', '.join(diag_2)}. Sum: {sum(int(num) for num in diag_2)}")
