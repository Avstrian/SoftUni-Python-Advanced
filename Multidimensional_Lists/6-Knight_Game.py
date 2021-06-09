size = int(input())
board = []
knight_location = []
most_aggressive_knight = 0
no_aggressive_knights = False
removed_knights = 0

for i in range(size):
    board.append(list(input()))

while not no_aggressive_knights:
    for row in range(len(board)):
        for column in range(len(board[row])):
            aggression = 0
            if board[row][column] == "K":
                positions_to_check = (
                    (row - 2, column - 1),
                    (row - 2, column + 1),
                    (row - 1, column - 2),
                    (row - 1, column + 2),
                    (row + 1, column - 2),
                    (row + 1, column + 2),
                    (row + 2, column - 1),
                    (row + 2, column + 1))

                for position in positions_to_check:
                    pos_row, pos_col = position

                    if not 0 <= pos_row <= len(board) - 1:
                        continue
                    if not 0 <= pos_col <= len(board) - 1:
                        continue

                    if board[pos_row][pos_col] == "K":
                        aggression += 1

            if aggression > most_aggressive_knight:
                most_aggressive_knight = aggression
                knight_location = [row, column]

    if not most_aggressive_knight == 0:
        most_aggressive_knight = 0
        board[knight_location[0]][knight_location[1]] = "0"
        removed_knights += 1
    else:
        no_aggressive_knights = True
        print(removed_knights)
