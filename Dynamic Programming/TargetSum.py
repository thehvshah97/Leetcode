from typing import List


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

    def dynamicProgrammingTabulation(self, arr: List[int], target: int) -> int:
        tot_sum = sum(arr)
        if tot_sum < target:
            return 0
        elif (tot_sum - target) % 2 != 0:
            return 0
        target = (tot_sum - target) // 2
        dp = [[0] * (target + 1) for _ in range(len(arr))]
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1

        for i in range(1, len(arr)):
            for j in range(target + 1):
                not_pick = dp[i - 1][j]
                pick = 0
                if arr[i] <= j:
                    pick = dp[i - 1][j - arr[i]]
                dp[i][j] = (pick + not_pick)
        return dp[len(arr) - 1][target]


if __name__ == '__main__':
    targetSum = TargetSum()
    print(targetSum.recursionCalling([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
    print(targetSum.dynamicProgrammingCalling([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
    print(targetSum.dynamicProgrammingTabulation([1, 1, 1, 1, 1], 3))
