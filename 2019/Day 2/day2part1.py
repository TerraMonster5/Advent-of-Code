with open("input.txt", "r") as file: codes = file.readline().strip().split(",")
codes[1] = 12
codes[2] = 2
for i in range(0, len(codes), 4):
    if codes[i] == 99:
        break
    elif codes[i] == 1:
        codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
    elif codes[i] == 2:
        codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
print(codes[0])