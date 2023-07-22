class EditDistance:
    def recursion(self, str1: str, str2: str, index1: int, index2: int) -> int:
        if index1 <= 0:
            return index2 + 1
        if index2 <= 0:
            return index1 + 1
        if str1[index1] == str2[index2]:
            return self.recursion(str1, str2, index1 - 1, index2 - 1)
        else:
            return min(1 + self.recursion(str1, str2, index1 - 1, index2 - 1),
                       1 + self.recursion(str1, str2, index1 - 1, index2),
                       1 + self.recursion(str1, str2, index1, index2 - 1))

    def recursionCalling(self, str1: str, str2: str) -> int:
        return self.recursion(str1, str2, len(str1) - 1, len(str2) - 1)

    def dynamicProgrammingTabulation(self, str1: str, str2: str) -> int:
        if len(str1) == 0 or len(str2) == 0:
            return len(str1) + len(str2)
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        for index1 in range(1, len(str1) + 1):
            dp[index1][0] = index1
        for index2 in range(1, len(str2) + 1):
            dp[0][index2] = index2
        for index1 in range(1, len(str1) + 1):
            for index2 in range(1, len(str2) + 1):
                if str1[index1 - 1] == str2[index2 - 1]:
                    dp[index1][index2] = dp[index1 - 1][index2 - 1]
                else:
                    dp[index1][index2] = 1 + min(dp[index1 - 1][index2 - 1], dp[index1][index2 - 1],
                                                 dp[index1 - 1][index2])
        return dp[-1][-1]


if __name__ == '__main__':
    editDistance = EditDistance()
    print(editDistance.recursionCalling('horse', 'ros'))
    print(editDistance.dynamicProgrammingTabulation('distance', 'springbok'))
