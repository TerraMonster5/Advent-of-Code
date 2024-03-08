import math
fuel = lambda x: math.floor(x/3)-2
with open("input.txt", "r") as file: masses = [fuel(int(line)) for line in file]
print(sum(masses))