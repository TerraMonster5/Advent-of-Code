with open("input.txt","r") as file: strings = [line.strip() for line in file]
def has3Vowels(checkVal: str) -> bool:
    num = 0
    for char in checkVal:
        if char in ("a","e","i","o","u"):
            num += 1
    if num > 2:
        return True
    else:
        return False
nice = 0
for string in strings:
    forbidden = sum((string.count("ab"),string.count("cd"),string.count("pq"),string.count("xy")))
    if forbidden == 0 and any(a==b for a,b in zip(string,string[1:])) and has3Vowels(string):
        nice += 1
print(nice)