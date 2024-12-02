def safe(report) -> int:
    if sorted(report) == report:
        for x in range(len(report)-1):
            if not report[x+1] - report[x] in (1, 2, 3):
                return 0
        return 1

    elif sorted(report, reverse=True) == report:
        for x in range(len(report)-1):
            if not report[x] - report[x+1] in (1, 2, 3):
                return 0
        return 1

    return 0

with open("input.txt", "r") as file: reports = [list(map(int, line.strip().split())) for line in file]

tot = 0

for report in reports:
    if safe(report):
        tot += 1
    else:
        temp = 0
        for x in range(len(report)):
            if safe(report[:x] + report[x+1:]):
                temp += 1
        if temp:
            tot += 1

print(tot)