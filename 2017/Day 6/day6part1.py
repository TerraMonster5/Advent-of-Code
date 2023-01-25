with open("input.txt","r") as file: banks = list(map(int, file.readline().strip().split()))
previous = [banks]