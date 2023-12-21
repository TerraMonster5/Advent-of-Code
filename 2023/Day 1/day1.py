with open("input.txt", "r") as file: print(sum([int([x for x in line.rstrip() if x.isdigit()][0]+[x for x in line.rstrip() if x.isdigit()][-1]) for line in file]))

numstrings = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
with open("input.txt", "r") as file: lines = [line.rstrip() for line in file]
indices = [[None if line.find(x) == -1 else line.find(x) for x in numstrings] for line in lines]
first = [lines[count].replace(numstrings[x.index(min(filter(lambda a: a != None, x)))], nums[x.index(min(filter(lambda a: a != None, x)))], 1) for count, x in enumerate(indices) if any(x)]
last = [nums[x.index(max(filter(lambda a: a != None, x)))].join(lines[count].rsplit(numstrings[x.index(max(filter(lambda a: a != None, x)))], 1)) for count, x in enumerate(indices) if any(x)]