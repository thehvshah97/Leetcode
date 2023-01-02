from typing import List


class LengthOfLastWord:
    def lengthOfLastWord( s: str) -> int:
        return len(s.rstrip(" ").split(" ")[-1])

if __name__ == '__main__':
    print(LengthOfLastWord.lengthOfLastWord("Hello Word  "))
