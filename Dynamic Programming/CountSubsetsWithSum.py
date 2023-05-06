class CountSubsets:
    def recursion(self, arr: list, index: int, target: int) -> int:
        if target == 0:
            return 1
        if index == 0:
            if target == arr[index]:
                return 1
            return 0
        not_pick = self.recursion(arr, index - 1, target)
        pick = 0
        if arr[index] <= target:
            pick = self.recursion(arr, index - 1, target - arr[index])
        return pick + not_pick

    def recursionCalling(self, arr: list, target: int) -> int:
        return self.recursion(arr, len(arr) - 1, target)

    def dynamicProgramming(self, arr: list, index: int, target: int, dp: list) -> int:
        if target == 0:
            return 1
        if index == 0:
            if target == arr[index]:
                return 1
            return 0
        if dp[index][target] != -1:
            return dp[index][target]

        not_pick = self.dynamicProgramming(arr, index - 1, target, dp)
        pick = 0
        if arr[index] <= target:
            pick = self.dynamicProgramming(arr, index - 1, target - arr[index], dp)
        dp[index][target] = pick + not_pick
        return dp[index][target]

    def dynamicProgrammingMemoization(self, arr: list, target: int) -> int:
        dp = [[-1] * (target + 1)] * len(arr)
        return self.dynamicProgramming(arr, len(arr) - 1, target, dp)


if __name__ == '__main__':
    countSubsets = CountSubsets()
    print(countSubsets.recursionCalling([1, 2, 3, 4], 5))
    print(countSubsets.dynamicProgrammingMemoization([1, 2, 3, 4], 4))

