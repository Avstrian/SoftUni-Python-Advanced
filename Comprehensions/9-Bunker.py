bunker = {item: [] for item in input().split(", ")}
quantity = 0
quality = 0
number_of_entries = int(input())

for entry in range(number_of_entries):
    category, item_type, quantity_quality = input().split(" - ")
    quantity_quality_list = quantity_quality.split(";")
    qty_qty_fixed = [[char for char in row if char.isdigit()] for row in quantity_quality_list]
    qty_qty_joined = ["".join(row) for row in qty_qty_fixed]
    bunker[category].append(item_type)
    quantity += int(qty_qty_joined[0])
    quality += int(qty_qty_joined[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {quality / len(bunker):.2f}")
[print(f"{key} -> {', '.join(value)}") for key, value in bunker.items()]
