heroes = [(name, [0]) for name in input().split(", ")]
heroes_inventory = {key: value for (key, value) in heroes}


command = input().split("-")
while not command[0] == "End":
    name, item, cost = command
    if item in heroes_inventory[name]:
        pass
    else:
        heroes_inventory[name].append(item)
        heroes_inventory[name][0] += int(cost)

    command = input().split("-")


[print(f"{key} -> Items: {len(value) - 1}, Cost: {value[0]}") for key, value in heroes_inventory.items()]
