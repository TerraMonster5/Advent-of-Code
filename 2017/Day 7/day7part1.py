from collections import Counter
with open("input.txt", "r") as file: lines = [line.strip().split() for line in file]
for row in lines:
    row.pop(1)
    if "->" in row: row.remove("->")
    for count, item in enumerate(row): row[count] = item.replace(",", "")
every = [dom for sub in lines for dom in sub]
counts = Counter(every)
for item in counts.items():
    if item[1] == 1:
        print(item[0])
        break