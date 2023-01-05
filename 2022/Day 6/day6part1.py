with open("input.txt","r") as file: string = file.readline().strip()
for x in range(0, len(string)):
    if len(set(string[x:x+4])) == 4:
        print(x+4,end=" ")