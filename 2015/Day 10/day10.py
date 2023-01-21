from itertools import groupby

code = "1113222113"

def runLength(text: str) -> str:
    newCode = ""
    for group in ["".join(g) for k, g in groupby(text)]:
        newCode += str(len(group)) + group[0]
    return newCode

# Part 1
for x in range(40):
    code = runLength(code)

print(len(code))

# Part 2
for x in range(10):
    code = runLength(code)

print(len(code))