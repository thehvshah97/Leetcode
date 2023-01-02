class AddBinary:
    def addBinary(a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


if __name__ == '__main__':
    print(AddBinary.addBinary("11", "1"))
