from structs import Stack

dirs = {"/":[]}; pwd = Stack(); pwd.push("/")

def calcSize(directory: str) -> int:
    total = 0
    for item in dirs[directory]:
        if item.startswith("dir"):
            total += calcSize(item.split()[1])
        else:
            total += int(item.split()[0])
    return total

with open("input.txt","r") as file:
    ls = False
    for count, line in enumerate(iter(file)):
        if count == 0:
            continue
        elif line.startswith("$ cd"):
            ls = False
            new = line.strip().split()[2]
            if new == "..":
                pwd.pop()
            else:
                dirs[new] = []
                pwd.push(new)
        elif line.startswith("$ ls"):
            ls = True
        elif ls:
            dirs[pwd.peek()].append(line.strip())

while pwd.peek() != "/":
    pwd.pop()

print(dirs)

bigTotal = 0

for key in dirs.keys():
    size = calcSize(key)
    if size < 100000:
        bigTotal += size

print(bigTotal)