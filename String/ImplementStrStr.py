class StrStr:
    def strStr(haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.find(needle)


if __name__ == '__main__':
    print(StrStr.strStr('hello', 'll'))

