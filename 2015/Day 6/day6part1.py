with open("input.txt","r") as file: instructions = [line.strip() for line in file]
lights = [[False for x in range(1000)] for x in range(1000)]