from itertools import permutations

with open("input.txt","r") as file: passphrases = [line.strip().split() for line in file]

# Part 1
print(len([phrase for phrase in passphrases if len(set(phrase)) == len(phrase)]))

# Part 2
valid = 0

for phrase in passphrases:
    anagrams = list(map(lambda x: sorted(x[0]) == sorted(x[1]), permutations(phrase, 2)))
    if anagrams.count(True) > 0:
        continue
    if len(set(phrase)) == len(phrase):
        valid += 1

print(valid)