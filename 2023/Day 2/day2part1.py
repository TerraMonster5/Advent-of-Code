with open("input.txt", "r") as file: lines = [[{hand.split()[1]: int(hand.split()[0]) for hand in game.split(", ")} for game in line.strip().split(": ")[1].split("; ")] for line in file]
total = 0
for count, game in enumerate(lines, 1):
    temp = {"red": 0, "green": 0, "blue": 0}
    for hand in game:
        for key, value in hand.items():
            if value > temp[key]:
                temp[key] = value
    if all(not {"red": 12, "green": 13, "blue": 14}[key] < temp[key] for key in temp.keys()):
        total += count
print(total)