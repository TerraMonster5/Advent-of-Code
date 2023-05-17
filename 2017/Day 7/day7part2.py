with open("input.txt", "r") as file: lines = [line.strip().split() for line in file]
sup = [row for row in lines if len(row) > 2]