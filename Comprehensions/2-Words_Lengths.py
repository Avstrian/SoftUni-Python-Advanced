lengths = [key for key in input().split(", ")]

for el in lengths:
    if el == lengths[-1]:
        print(f"{el} -> {len(el)}")
        break
    print(f"{el} -> {len(el)}", end=", ")
