import math
import numpy as np

class CountSubsetsWithDifference:
    def recursion(self, arr: list, index: int, totSum: int, currSum: int, target: int) -> int:
        if index == 0:
            if abs((totSum - currSum) - currSum) == target:
                return 1
            return 0
        return self.recursion(arr, index - 1, totSum, currSum, target) + self.recursion(arr, index - 1, totSum, currSum
                                                                                        + arr[index], target)

    def recursionCalling(self, arr: list, target: int) -> int:
        return self.recursion(arr, len(arr) - 1, sum(arr), 0, target)

    def dynamicProgrammingTabulation(self, arr: list, diff: int) -> int:
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
        number = 0
        for i in range(1, sum(arr)):
            if dp[-1][i]:
                if abs((sum(arr) - i) - i) == diff:
                    number += 1
        return int(number/2)


if __name__ == '__main__':
    countSubsetsWithDifference = CountSubsetsWithDifference()
    print(countSubsetsWithDifference.recursionCalling([5, 2, 6, 4], 3))
    print(countSubsetsWithDifference.dynamicProgrammingTabulation([5, 2, 6, 4], 3))

