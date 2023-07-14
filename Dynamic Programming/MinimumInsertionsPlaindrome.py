from typing import List


class MinimumInsertions:
    def recursion(self, str1: str, str2: str, index1: int, index2: int) -> int:
        if index1 == len(str1) - 1 and index2 == len(str2) - 1:
            if str1[index1] != str2[index2]:
                return 2
            else:
                return 0
        elif index1 == len(str1) - 1 or index2 == len(str2) - 1:
            return (len(str2) - 1 - index2) + (len(str1) - 1 - index1) + 1
        if str1[index1] == str2[index2]:
            return self.recursion(str1, str2, index1 + 1, index2 + 1)
        return min(1 + self.recursion(str1, str2, index1 + 1, index2), 1 + self.recursion(str1, str2, index1, index2 + 1))

    def recursionCalling(self, text: str) -> int:
        if len(text) % 2 != 0:
            mid = len(text) // 2
            return self.recursion(text[0: mid], text[len(text) - 1: mid: -1], 0, 0)
        else:
            mid = len(text) // 2
            return self.recursion(text[0: mid], text[len(text) - 1: mid - 1: -1], 0, 0)

    def dynamicProgrammingMemoization(self, str1: str, str2: str, index1: int, index2: int, dp: List[List[int]]) -> int:
        if index1 == len(str1) - 1 and index2 == len(str2) - 1:
            if str1[index1] != str2[index2]:
                return 2
            else:
                return 0
        elif index1 == len(str1) - 1 or index2 == len(str2) - 1:
            return (len(str2) - 1 - index2) + (len(str1) - 1 - index1) + 1
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if str1[index1] == str2[index2]:
            return self.dynamicProgrammingMemoization(str1, str2, index1 + 1, index2 + 1, dp)
        dp[index1][index2] = min(1 + self.dynamicProgrammingMemoization(str1, str2, index1 + 1, index2, dp), 1 + self.dynamicProgrammingMemoization(str1, str2, index1, index2 + 1, dp))
        return dp[index1][index2]

    def dynamicProgrammingCalling(self, text: str) -> int:
        if len(text) % 2 != 0:
            mid = len(text) // 2
            dp = [[-1 for _ in range(len(text[0: mid]) + 1)] for _ in range(len(text[len(text) - 1: mid: -1]) + 1)]
            return self.dynamicProgrammingMemoization(text[0: mid], text[len(text) - 1: mid: -1], 0, 0, dp)
        else:
            mid = len(text) // 2
            dp = [[-1 for _ in range(len(text[0: mid]) + 1)] for _ in range(len(text[len(text) - 1: mid - 1: -1]) + 1)]
            return self.dynamicProgrammingMemoization(text[0: mid], text[len(text) - 1: mid - 1: -1], 0, 0, dp)

    def dynamicProgrammingTabulation(self, text: str) -> int:
        str1 = text
        str2 = text[::-1]
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                else:
                    dp[index1][index2] = max(dp[index1][index2 - 1], dp[index1 - 1][index2])
        return len(text) - dp[-1][-1]


if __name__ == '__main__':
    minimumInsertions = MinimumInsertions()
    print(minimumInsertions.recursionCalling('mbadm'))
    print(minimumInsertions.dynamicProgrammingCalling('zzazz'))
    print(minimumInsertions.dynamicProgrammingTabulation('leetcode'))