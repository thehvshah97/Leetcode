import sys


class ReverseInteger:
    def reverse(x: int) -> int:
        if x >= 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) >= -2**31 and int(str(x)[::-1]) <= 2**31 - 1 else 0
        else:
            return int(str(x)[1:][::-1]) * -1 if int(str(x)[1:][::-1]) * -1 >= -2**31 and int(str(x)[1:][::-1]) * -1 <= 2**31 - 1 else 0

if __name__ == '__main__':
    print(ReverseInteger.reverse(1534236469))
    print(2**31)