with open("input.txt", "r") as file: flip = lambda x: [x[1]]+x[:1]+x[2:]; wires = {lst[1]: int(lst[0]) if lst[0].isdigit() else lst[0].split() if len(lst[0].split()) in (1, 2) else list(map(lambda y: int(y) if y.isdigit() else y, flip(lst[0].split()))) for lst in [line.strip().split(" -> ") for line in file]}
[print(key+" " if len(key) == 1 else key, ":", val) for key, val in sorted(wires.items(), key=lambda x: x[0])]

def gate(loc: str) -> int:
    val = wires[loc]
    if isinstance(val, int):
        return val
    if len(val) == 1:
        result = (gate(val[0])) & 0xFFFF
    elif len(val) == 2:
        result = (~gate(val[1])) & 0xFFFF
    elif len(val) == 3:
        op = val.pop(0)
        match op:
            case "AND":
                result = (gate(val[0]) & val[1] if isinstance(val[1], int) else gate(val[1])) & 0xFFFF
            case "OR":
                result = (gate(val[0]) | val[1] if isinstance(val[1], int) else gate(val[1])) & 0xFFFF
            case "LSHIFT":
                result = (gate(val[0]) << val[1] if isinstance(val[1], int) else gate(val[1])) & 0xFFFF
            case "RSHIFT":
                result = (gate(val[0]) >> val[1] if isinstance(val[1], int) else gate(val[1])) & 0xFFFF

    wires[loc] = result
    return result

print(gate("a"))
[print(key+" " if len(key) == 1 else key, ":", val) for key, val in sorted(wires.items(), key=lambda x: x[0])]
