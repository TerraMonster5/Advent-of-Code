from math import sqrt

X, Y = 0, 1

val = 289326
oddRoot = int(sqrt(val))
if not oddRoot % 2: oddRoot -= 1
checkVal = oddRoot ** 2 + 1
x = y = oddRoot // 2; coords = [x, y]
coords[X] += 1

for i in range(oddRoot):
    if checkVal != val:
        coords[Y] -= 1
        checkVal += 1
    else:
        print(sum(map(abs, coords)))
        exit()

for i in range(oddRoot+2):
    if checkVal != val:
        coords[X] -= 1
        checkVal += 1
    else:
        print(sum(map(abs, coords)))
        exit()

for i in range(oddRoot+2):
    if checkVal != val:
        coords[Y] += 1
        checkVal += 1
    else:
        print(sum(map(abs, coords)))
        exit()

for i in range(oddRoot+2):
    if checkVal != val:
        coords[X] += 1
        checkVal += 1
    else:
        print(sum(map(abs, coords)))
        exit()