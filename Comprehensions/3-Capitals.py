countries = input().split(", ")
capitals = input().split(", ")
countries_and_capitals = {print(f"{countries[num]} -> {capitals[num]}") for num in range(0, len(capitals))}