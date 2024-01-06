with open("input.txt", "r") as file: cards = [[list(map(int, seg.split())) for seg in line.strip().split(": ")[1].split(" | ")] for line in file]
total = 0
for card in cards:
    score = 0
    flag = False
    for number in card[1]:
        if number in card[0]:
            if not flag:
                flag = True
                score += 1
            elif flag:
                score *= 2
    total += score
print(total)