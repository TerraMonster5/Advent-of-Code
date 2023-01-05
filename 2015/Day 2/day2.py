with open("input.txt","r") as file: lines = [list(map(int, line.strip().split("x"))) for line in file]; total = 0
def calcSize(dims: list[int]) -> list:   
    return [dims[index] * dims[(index+1)%3] for index in range(3)]
boxes = list(map(calcSize, lines))
for box in boxes:
    total += min(box)
    for side in box:
        total += 2 * side
print(total)