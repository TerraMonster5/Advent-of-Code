with open("input.txt","r") as file: print(sum([ord(value)-38 if value.isupper() else ord(value)-96 for value in [next(iter(set(line[:len(line)//2]).intersection(line[len(line)//2:]))) for line in file]]))