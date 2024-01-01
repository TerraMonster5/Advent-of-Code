# Part 1
with open("input.txt", "r") as file: print(sum([int([x for x in line.rstrip() if x.isdigit()][0]+[x for x in line.rstrip() if x.isdigit()][-1]) for line in file]))

# Part 2
numstrings = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
with open("input.txt", "r") as file: lines = [line.rstrip() for line in file]
indices = [[None if line.find(x) == -1 else line.find(x) for x in numstrings] for line in lines]
print(indices)
print([list(filter(lambda a: a != None, x)) for x in indices])
first = [lines[count].replace(numstrings[x.index(min(list(filter(lambda a: a != None, x))))], nums[x.index(min(list(filter(lambda a: a != None, x))))], 1) if any(x) else lines[count] for count, x in enumerate(indices)]
last = [nums[x.index(max(list(filter(lambda a: a != None, x))))].join(lines[count].rsplit(numstrings[x.index(max(list(filter(lambda a: a != None, x))))], 1)) if any(x) else lines[count] for count, x in enumerate(indices)]
news = []
for x in range(len(lines)):
    temp = ""
    for count, char in enumerate(first[x]):
        if char.isdigit():
            temp += char
            break
    for count, char in enumerate(last[x][::-1]):
        if char.isdigit():
            temp += char
            break
    news.append(int(temp))
print(news)
print(sum(news))