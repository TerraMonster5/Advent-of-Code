import re
from operator import mul

with open("input.txt", "r") as file: prog = "".join([line.strip() for line in file])

expr = re.compile(r"do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)")
enable = True

matches = expr.findall(prog)

tot = 0

for match in matches:
    if match == "do()":
        enable = True
    elif match == "don't()":
        enable = False
    elif enable:
        tot += mul(*map(int, match.strip("mul()").split(",")))

print(tot)