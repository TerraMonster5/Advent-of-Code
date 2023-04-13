with open("input.txt", "r") as file: gates = [line.strip().split() for line in file]

def gate(pos: int):
    if len(gates[pos]) == 3:
        if gates[pos][0].isdigit():
            return int(gates[pos][0])
        else:
            return gate([x[-1] for x in gates].index(gates[pos][0]))
    elif len(gates[pos]) == 4:
        return int(~gate([x[-1] for x in gates].index(gates[pos][1])))
    elif len(gates[pos]) == 5:
        match gates[pos][1]:
            case "AND":
                if gates[pos][0].isdigit():
                    return int(int(gates[pos][0]) & gate([x[-1] for x in gates].index(gates[pos][2])))
                else:
                    return int(gate([x[-1] for x in gates].index(gates[pos][0])) & gate([x[-1] for x in gates].index(gates[pos][2])))
            case "OR":
                return int(gate([x[-1] for x in gates].index(gates[pos][0])) | gate([x[-1] for x in gates].index(gates[pos][2])))
            case "LSHIFT":
                return int(gate([x[-1] for x in gates].index(gates[pos][0]))<<int(gates[pos][2]))
            case "RSHIFT":
                return int(gate([x[-1] for x in gates].index(gates[pos][0]))>>int(gates[pos][2]))

loc = 0

for count, line in enumerate(gates):
    if line[-1] == "a":
        loc = count

print(gate(loc))