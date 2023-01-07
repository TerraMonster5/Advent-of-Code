with open("input.txt","r") as file: strings = [line.strip() for line in file]
def substringPair(checkVal: str) -> bool:
    for index in range(len(checkVal)-1):
        if checkVal.count(checkVal[index]+checkVal[index+1]) > 1:
            return True
    return False
def splitPair(checkVal: str) -> bool:
    for index in range(len(checkVal)-2):
        if checkVal[index] == checkVal[index+2]:
            return True
    return False
nice = 0
for string in strings:
    if substringPair(string) and splitPair(string):
        nice += 1
print(nice)