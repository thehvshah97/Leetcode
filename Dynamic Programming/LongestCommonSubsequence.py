from typing import List

import numpy as np


class LongestCommonSubsequence:
    def recursion(self, str1: str, str2: str, index1: int, index2: int) -> int:
        if index1 and index2 == 0 and str1[index1] == str2[index2]:
            return 1
        elif index1 < 0 or index2 < 0:
            return 0
        if str1[index1] == str2[index2]:
            return 1 + self.recursion(str1, str2, index1 - 1, index2 - 1)
        return max(self.recursion(str1, str2, index1 - 1, index2), self.recursion(str1, str2, index1, index2 - 1))

    def recursionCalling(self, str1: str, str2: str) -> int:
        return self.recursion(str1, str2, len(str1) - 1, len(str2) - 1)

    def dynamicProgrammingMemoization(self, str1: str, str2: str, index1: int, index2: int, dp: List[List[int]]) -> int:
        if index1 and index2 == 0 and str1[index1] == str2[index2]:
            return 1
        elif index1 < 0 or index2 < 0:
            return 0
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if str1[index1] == str2[index2]:
            dp[index1][index2] = 1 + self.dynamicProgrammingMemoization(str1, str2, index1 - 1, index2 - 1, dp)
            return dp[index1][index2]
        dp[index1][index2] = max(self.dynamicProgrammingMemoization(str1, str2, index1 - 1, index2, dp), self.dynamicProgrammingMemoization(str1, str2, index1, index2 - 1, dp))
        return dp[index1][index2]

    def dynamicProgrammingMemoizationCalling(self, str1: str, str2: str) -> int:
        dp = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]
        return self.dynamicProgrammingMemoization(str1, str2, len(str1) - 1, len(str2) - 1, dp)

    def dynamicProgrammingTabulation(self, str1: str, str2: str) -> int:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                else:
                    dp[index1][index2] = max(dp[index1][index2 - 1], dp[index1 - 1][index2])
        return dp[-1][-1]

    def dynamicProgrammingTabulationPrint(self, str1: str, str2: str) -> str:
        dp = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = dp[index1 - 1][index2 - 1] + str1[index1 - 1]
                else:
                    if len(dp[index1][index2 - 1]) > len(dp[index1 - 1][index2]):
                        dp[index1][index2] = dp[index1][index2 - 1]
                    else:
                        dp[index1][index2] = dp[index1 - 1][index2]
        return dp[-1][-1]


if __name__ == '__main__':
    longestCommonSubsequence = LongestCommonSubsequence()
    print(longestCommonSubsequence.recursionCalling('abcde', 'ace'))
    print(longestCommonSubsequence.dynamicProgrammingMemoizationCalling('abcde', 'ace'))
    print(longestCommonSubsequence.dynamicProgrammingTabulation('abcde', 'ace'))
    print(longestCommonSubsequence.dynamicProgrammingTabulationPrint('abcde', 'ace'))
