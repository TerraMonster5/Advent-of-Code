from math import sqrt

X = 0
Y = 1

val = 289326

oddRoot = int(sqrt(val))

oddSquare = oddRoot**2

layer = oddRoot//2

coords = [layer]*2

coords[X] += 1

val -= (oddSquare + 1)