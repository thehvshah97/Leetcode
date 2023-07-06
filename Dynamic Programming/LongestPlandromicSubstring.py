class LongestCommonSubstring:
    def dynamicProgrammingTabulation(self, str1: str, str2: str) -> int:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        ans = 0
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                    ans = max(dp[index1][index2], ans)
                else:
                    dp[index1][index2] = 0
        return ans

    def dynamicProgrammingTabulationCalling(self, str1: str) -> int:
        return self.dynamicProgrammingTabulation(str1, str1[::-1])


if __name__ == '__main__':
    longestCommonSubstring = LongestCommonSubstring()
    print(longestCommonSubstring.dynamicProgrammingTabulationCalling('bbbab'))

