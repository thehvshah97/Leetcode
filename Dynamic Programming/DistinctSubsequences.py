from typing import List


class DistinctSubsequences:

    def recursion(self, str1: str, str2: str, index1: int, index2: int) -> int:
        if index1 and index2 == 0:
            if str1[index1] == str2[index2]:
                return 1
            else:
                return 0
        elif index2 == 0:
            if str1[index1] == str2[index2]:
                return 1 + self.recursion(str1, str2, index1 - 1, index2)
        elif index1 <= 0:
            return 0

        if str1[index1] == str2[index2]:
            return self.recursion(str1, str2, index1 - 1, index2) + self.recursion(str1, str2, index1 - 1, index2 - 1)
        else:
            return self.recursion(str1, str2, index1 - 1, index2)

    def recursionCalling(self, str1: str, str2: str) -> int:
        return self.recursion(str1, str2, len(str1) - 1, len(str2) - 1)

    def dynamicprogrammingMemoization(self, str1: str, str2: str, index1: int, index2: int, dp: List[List[int]]) -> int:
        if index1 and index2 == 0:
            if str1[index1] == str2[index2]:
                return 1
            else:
                return 0
        elif index2 == 0:
            if str1[index1] == str2[index2]:
                dp[index1][index2] = 1 + self.dynamicprogrammingMemoization(str1, str2, index1 - 1, index2, dp)
                return dp[index1][index2]
        elif index1 <= 0:
            return 0
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if str1[index1] == str2[index2]:
            dp[index1][index2] = self.dynamicprogrammingMemoization(str1, str2, index1 - 1, index2, dp) + self.dynamicprogrammingMemoization(str1, str2, index1 - 1, index2 - 1, dp)
        else:
            dp[index1][index2] = self.dynamicprogrammingMemoization(str1, str2, index1 - 1, index2, dp)
        return dp[index1][index2]

    def dynamicProgrammingMemoizationCalling(self, str1: str, str2: str) -> int:
        dp = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        return self.dynamicprogrammingMemoization(str1, str2, len(str1) - 1, len(str2) - 1, dp)

    def dynamicProgrammingTabulation(self, str1: str, str2: str) -> int:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(len(str1)):
            if str1[index1] == str2[0]:
                dp[index1][0] += 1

        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = dp[index1 - 1][index2 - 1] + dp[index1 - 1][index2]
                else:
                    dp[index1][index2] = dp[index1 - 1][index2]
        return dp[-1][-1]


if __name__ == '__main__':
    distinctSubsequences = DistinctSubsequences()
    print(distinctSubsequences.recursionCalling('rabbbit', 'rabbit'))
    print(distinctSubsequences.dynamicProgrammingMemoizationCalling('rabbbit', 'rabbit'))
    print(distinctSubsequences.dynamicProgrammingTabulation('rabbbit', 'rabbit'))