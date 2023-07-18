class MinimumInsertionsDeletions:
    def dynamicProgrammingTabulation(self, str1: str, str2: str) -> int:
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                else:
                    dp[index1][index2] = max(dp[index1][index2 - 1], dp[index1 - 1][index2])
        return len(str1) - dp[-1][-1] + len(str2) - dp[-1][-1]


if __name__ == '__main__':
    minimumInsertionsDeletions = MinimumInsertionsDeletions()
    print(minimumInsertionsDeletions.dynamicProgrammingTabulation('abcd', 'anc'))