from typing import List


class MinimumCostClimbingStairs:
    def recursion(self, nums: List[int], index: int):
        if index >= len(nums):
            return 0

        return min(self.recursion(nums, index + 1) + nums[index], self.recursion(nums, index + 2) + nums[index])

    def recursion_calling(self, nums: List[int]):
        return min(self.recursion(nums, 0), self.recursion(nums, 1))

    def dynamic_programming_memoization(self, nums: List[int], index: int, dp: List[int])  -> int:
        if index >= len(nums):
            return 0
        elif dp[index] != -1:
            return dp[index]

        dp[index] = min(self.dynamic_programming_memoization(nums, index + 1, dp) + nums[index],
                        self.dynamic_programming_memoization(nums, index + 2, dp) + nums[index])
        return dp[index]

    def dynamic_programming_memoization_calling(self, nums: List[int]):
        dp = [-1 for _ in range(len(nums))]
        return min(self.dynamic_programming_memoization(nums, 0, dp), self.dynamic_programming_memoization(nums, 1, dp))

    def dynamic_programming_tabulation(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for index in range(len(nums) + 1):
            dp[index] = min(dp[index - 1], dp[index - 2])
            if index < len(nums):
                dp[index] = dp[index] + nums[index]
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    minCost = MinimumCostClimbingStairs()
    print(minCost.recursion_calling([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(minCost.dynamic_programming_memoization_calling([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(minCost.dynamic_programming_tabulation([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
