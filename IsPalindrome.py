class IsPalindrome:
    def ispalindrome(x: int) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(IsPalindrome.ispalindrome(1025))