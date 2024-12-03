import re
from operator import mul

with open("input.txt", "r") as file: prog = "".join([line.strip() for line in file])

expr = re.compile(r"mul\([0-9]+,[0-9]+\)")

print(sum(map(lambda x: mul(*map(int, x.strip("mul()").split(","))), expr.findall(prog))))