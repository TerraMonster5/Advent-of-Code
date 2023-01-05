vals = {"X" : 0, "Y" : 3, "Z" : 6}; total = 0
with open("input.txt","r") as file: lines = [line.strip().split() for line in file]
for pair in lines:
    total += vals[pair[1]]
    if pair in (["B", "X"], ["A", "Y"], ["C", "Z"]):
        total += 1
    elif pair in (["C", "X"], ["B", "Y"], ["A", "Z"]):
        total += 2
    elif pair in (["A", "X"], ["C", "Y"], ["B", "Z"]):
        total += 3
print(total)
