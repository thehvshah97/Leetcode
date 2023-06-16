import math
import numpy as np

class CountSubsetsWithDifference:
    dp = []
    def recursion(self, arr: list, index: int, target: int) -> int:
        if index == 0:
            if target == 0 and arr[index] == 0:
                return 2
            elif target == 0 or arr[index] == target:
                return 1
            return 0
        not_pick = self.recursion(arr, index - 1, target)
        pick = 0
        if arr[index] <= target:
            pick = self.recursion(arr, index - 1, target - arr[index])
        return pick + not_pick

    def recursionCalling(self, arr: list, diff: int) -> int:
        if sum(arr) - diff < 0 or (sum(arr) - diff) % 2 != 0:
            return 0
        return self.recursion(arr, len(arr) - 1, (sum(arr) - diff) // 2)

    def dynamicProgrammingMemoization(self, arr: list, index: int, target: int):
        if index == 0:
            if target == 0 and arr[index] == 0:
                return 2
            elif target == 0 or arr[index] == target:
                return 1
            return 0
        elif self.dp[index][target] != -1:
            return self.dp[index][target]
        not_pick = self.dynamicProgrammingMemoization(arr, index - 1, target)
        pick = 0
        if arr[index] <= target:
            pick = self.dynamicProgrammingMemoization(arr, index - 1, target - arr[index])
        self.dp[index][target] = pick + not_pick
        return self.dp[index][target]

    def dynamicProgrammingCalling(self, arr: list, diff: int) -> int:
        self.dp = [[-1] * (sum(arr) + 1)] * (len(arr))
        if sum(arr) - diff < 0 or (sum(arr) - diff) % 2 != 0:
            return 0
        return self.dynamicProgrammingMemoization(arr, len(arr) - 1, (sum(arr) - diff) // 2)

    def dynamicProgrammingTabulation(self, arr: list, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(len(arr))]
        if arr[0] == 0:
            dp[0][0] = 2
        elif arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
        else:
            dp[0][0] = 1
        for i in range(1, len(arr)):
            for j in range(target + 1):
                not_pick = dp[i - 1][j]
                pick = 0
                if arr[i] <= j:
                    pick = dp[i - 1][j - arr[i]]
                dp[i][j] = (pick + not_pick)
        return dp[len(arr) - 1][target]

    def dynamicProgrammingTabulationCalling(self, arr: list, diff: int):
        if sum(arr) - diff < 0 or (sum(arr) - diff) % 2 != 0:
            return 0
        return self.dynamicProgrammingTabulation(arr, (sum(arr) - diff) // 2)



if __name__ == '__main__':
    countSubsetsWithDifference = CountSubsetsWithDifference()
    print(countSubsetsWithDifference.recursionCalling([5, 2, 6, 4], 3))
    print(countSubsetsWithDifference.dynamicProgrammingCalling([5, 2, 6, 4], 3))
    print(countSubsetsWithDifference.dynamicProgrammingTabulationCalling([5, 2, 6, 4], 3))

