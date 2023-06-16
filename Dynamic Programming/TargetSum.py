from typing import List
import numpy as np

class TargetSum:
    dp = [[]]
    def recursion(self, nums: List[int], target: int, index: int) -> int:
        if index == 0:
            if abs(target) == nums[0]:
                return 1
            return 0
        add = self.recursion(nums, target - nums[index], index - 1)
        subtract = self.recursion(nums, target + nums[index], index - 1)
        return add + subtract

    def recursionCalling(self, nums: List[int], target: int) -> int:
        return self.recursion(nums, target, len(nums) - 1)

    def dynamicProgramming(self, nums: List[int], target: int, index: int) -> int:
        if index == 0:
            if abs(target) == nums[0]:
                return 1
            return 0

        if self.dp[index][target] != -1:
            return self.dp[index][target]

        add = self.dynamicProgramming(nums, target - nums[index], index - 1)
        subtract = self.dynamicProgramming(nums, target + nums[index], index - 1)
        self.dp[index][target] = add + subtract
        return self.dp[index][target]

    def dynamicProgrammingCalling(self, nums: List[int], target: int) -> int:
        self.dp = [[-1 for _ in range(target + 1 + sum(nums))] for _ in range(len(nums) + 1)]
        return self.dynamicProgramming(nums, target, len(nums) - 1)

    def dynamicProgrammingTabulation(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        n = len(nums)
        if target > sm:
            return 0
        if (sm - target) % 2:
            return 0
        tr = (sm - target) // 2
        nums.sort()
        dp = [[0] * (tr + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        if nums[0] <= tr:
            dp[0][nums[0]] = 1
        for i in range(1, n):
            for j in range(tr + 1):
                x = 0
                if nums[i] <= j:
                    x = dp[i - 1][j - nums[i]]
                y = dp[i - 1][j]
                dp[i][j] = x + y
        zero = nums.count(0)
        if zero:
            return dp[-1][tr] * 2
        return dp[-1][tr]


if __name__ == '__main__':
    targetSum = TargetSum()
    print(targetSum.recursionCalling([1, 1, 1, 1, 1], 3))
    print(targetSum.dynamicProgrammingCalling([1, 1, 1, 1, 1], 3))
    print(targetSum.dynamicProgrammingTabulation([1, 1, 1, 1, 1], 3))
