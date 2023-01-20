from itertools import permutations

with open("input.txt","r") as file: rows = [list(map(int, line.strip().split())) for line in file]

# Part 1
print(sum([max(row) - min(row) for row in rows]))

# Part 2
print(sum([[item for item in map(lambda x: int(x[0] / x[1]) if not x[0] % x[1] else None, permutations(row, 2)) if item][0] for row in rows]))