from itertools import groupby
with open("input.txt","r") as file: lines = [line.strip() for line in file]
elves = [list(v) for k, v in groupby(lines, key=bool) if k]
intElves = [list(map(int, item)) for item in elves]
sums = [sum(elf) for elf in intElves]
totals = sorted(sums, reverse=True)[:3]
print(totals[0], sum(totals))