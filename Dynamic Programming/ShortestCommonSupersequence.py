from typing import List


class LongestCommonSubsequence:
    def dynamicProgrammingTabulationPrint(self, str1: str, str2: str) -> str:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                else:
                    dp[index1][index2] = max(dp[index1][index2 - 1], dp[index1 - 1][index2])
        index1 = len(str1)
        index2 = len(str2)
        ans = ''
        while index1 > 0 and index2 > 0:
            if str1[index1 - 1] == str2[index2 - 1]:
                ans += str1[index1 - 1]
                index1 -= 1
                index2 -= 1
            elif dp[index1 - 1][index2] > dp[index1][index2 - 1]:
                ans += str1[index1 - 1]
                index1 -= 1
            else:
                ans += str2[index2 - 1]
                index2 -= 1
        while index1 > 0:
            ans += str1[index1 - 1]
            index1 -= 1
        while index2 > 0:
            ans += str2[index2 - 1]
            index2 -= 1
        ans = ans[::-1]
        return ans


if __name__ == '__main__':
    longestCommonSubsequence = LongestCommonSubsequence()
    print(longestCommonSubsequence.dynamicProgrammingTabulationPrint('abac', 'cab'))
