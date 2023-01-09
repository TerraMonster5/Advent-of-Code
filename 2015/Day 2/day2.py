with open("input.txt", "r") as file: lines = [list(map(int, line.strip().split("x"))) for line in file]; total = 0
def calcSize(dims: list[int]) -> list[int]:
    return [dims[index] * dims[(index+1)%3] for index in range(3)]
boxes = list(map(calcSize, lines))
for box in boxes:
    total += min(box)
    for side in box:
        total += 2 * side

bows = list(map(lambda dims:dims[0]*dims[1]*dims[2] + 2*sum(dims[:2]), list(map(sorted, lines))))
totalRibon = sum(bows)

print(total, totalRibon)