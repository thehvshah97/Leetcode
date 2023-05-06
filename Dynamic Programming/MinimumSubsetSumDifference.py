import math

import numpy as np

class MinimumSubsetSumSequence:
    def recursion(self, arr: list, index: int, totSum: int, currSum: int) -> int:
        if index == 0:
            return abs((totSum - currSum)-currSum)
        return min(self.recursion(arr, index - 1, totSum, currSum), self.recursion(arr, index - 1, totSum, currSum + arr[index]))

    def recursionCalling(self, arr: list) -> int:
        return self.recursion(arr, len(arr) - 1, sum(arr), 0)

    def dynamicProgrammingTabulation(self, arr: list) -> int:
        target = sum(arr)
        dp = np.zeros([len(arr), target + 1], dtype=bool)
        for i in range(len(arr)):
            dp[i][0] = True
        if arr[0] < target:
            dp[0][arr[0]] = True
        for i in range(1, len(arr)):
            for j in range(1, target + 1):
                notTaken = dp[i - 1][j]
                taken = False
                if arr[i] <= target:
                    taken = dp[i - 1][j - arr[i]]
                dp[i][j] = taken or notTaken

        minDiff = math.inf
        for i in range(1, sum(arr)):
            if dp[-1][i]:
                minDiff = min(minDiff, abs((sum(arr) - i) - i))
        return minDiff


if __name__ == '__main__':
    minimumSubsetSumSequence = MinimumSubsetSumSequence()
    print(minimumSubsetSumSequence.recursionCalling([1, 2, 3, 4]))
    print(minimumSubsetSumSequence.dynamicProgrammingTabulation([8, 6, 5]))

