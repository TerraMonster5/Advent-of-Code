import hashlib
code = "bgvyzdsv"
def checkHash(string: str) -> int:
    num = -1
    hexHash = hashlib.md5(code.encode()).hexdigest()
    while not hexHash.startswith(string):
        num += 1
        hexHash = hashlib.md5(str(code+str(num)).encode()).hexdigest()
    return num
print(checkHash("00000"), checkHash("000000"))