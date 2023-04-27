class SubsetSumEqualToK:
    def recursion(self, arr: list, index: int, target: int) -> bool:
        if arr[index] == target:
            return True
        elif index == 0:
            return True if arr[index] == target else False
        notTaken = self.recursion(arr, index - 1, target)
        taken = self.recursion(arr, index - 1, target - arr[index])
        if taken or notTaken:
            return True
        else:
            return False

    def recursionCalling(self, arr: list, target: int) -> bool:
        return self.recursion(arr, len(arr) - 1, target)

    def dynamicProgrammingMemoizationCalling(self, arr: list, target: int) -> bool:
        dp = [False] * len(arr)
        return self.dynamicProgrammingMemoization(arr, len(arr) - 1, target, dp)

    def dynamicProgrammingMemoization(self, arr: list, index: int, target: int, dp: list) -> bool:
        if arr[index] == target:
            return True
        elif index == 0:
            return True if arr[index] == target else False
        elif dp[index]:
            return dp[index]
        notTaken = self.dynamicProgrammingMemoization(arr, index - 1, target, dp)
        taken = self.dynamicProgrammingMemoization(arr, index - 1, target - arr[index], dp)
        if taken or notTaken:
            dp[index] = True
            return True
        else:
            return False


if __name__ == '__main__':
    subsetSumEqualToK = SubsetSumEqualToK()
    print(subsetSumEqualToK.recursionCalling([1, 2, 3, 4], 4))
    print(subsetSumEqualToK.dynamicProgrammingMemoizationCalling([1, 2, 3, 4], 10))

