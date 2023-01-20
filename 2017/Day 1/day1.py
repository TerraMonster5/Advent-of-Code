with open("input.txt","r") as file: sequence = file.readline().strip()

# Part 1
print(sum([int(sequence[index]) for index in range(len(sequence)) if sequence[index] == sequence[(index+1) % len(sequence)]]))

# Part 2
print(sum([int(sequence[index]) for index in range(len(sequence)) if sequence[index] == sequence[(index+int(len(sequence)/2)) % len(sequence)]]))