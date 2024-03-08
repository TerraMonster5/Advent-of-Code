import math
fuel = lambda x: math.floor(x/3)-2
with open("input.txt", "r") as file: masses = [int(line) for line in file]
bigtot = 0
for mass in masses:
    tot = mass
    while tot > 0:
        tot = int(fuel(tot))
        if tot < 0:
            tot = 0
        bigtot += tot
print(bigtot)