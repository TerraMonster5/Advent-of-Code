checkVal = 33100000

def factors(num: int) -> list:
    return [x for x in range(1, num+1) if not num % x]

temp = 0

for y in range(1, int(checkVal/10)):
    if sum(factors(y))*10 >= checkVal:
        temp = y
        break

print(temp)