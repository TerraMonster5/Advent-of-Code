with open("input.txt","r") as file: string = file.readline().strip()
for x in range(0, len(string)):
    if len(set(string[x:x+14])) == 14:
        print(x+14,end=" ")