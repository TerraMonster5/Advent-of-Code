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

with open("input.txt", "r") as file: print(sum(map(safe, [list(map(int, line.strip().split())) for line in file])))