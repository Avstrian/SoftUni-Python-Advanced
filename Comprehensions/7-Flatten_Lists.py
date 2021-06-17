start_list = [numbers.split(' ') for numbers in input().split("|")]
start_list.reverse()
popped = [start_list[row][el] for row in range(len(start_list)) for el in range(len(start_list[row]))
          if not start_list[row][el] == '']
print(' '.join(popped))
