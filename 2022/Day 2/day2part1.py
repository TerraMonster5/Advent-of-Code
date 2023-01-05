vals = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}; total = 0
with open("input.txt","r") as file: lines = [line.strip().split() for line in file]
for pair in lines:
    total += vals[pair[1]]
    if vals[pair[0]] == vals[pair[1]]:
        total += 3
    elif (vals[pair[1]], vals[pair[0]]) in ((1, 3), (2, 1), (3, 2)):
        total += 6
print(total)