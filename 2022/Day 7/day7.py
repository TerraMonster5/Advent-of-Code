from structs import Stack

dirs = {"/":[]}; pwd = Stack(); pwd.push("/")

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

for dir in dirs.keys():
    pass