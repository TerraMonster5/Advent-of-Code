with open("input.txt", "r") as file: cards = [[list(map(int, seg.split())) for seg in line.strip().split(": ")[1].split(" | ")] for line in file]
for card in cards:
    count = 0
    for num in card[1]:
        if num in card[0]:
            count += 1