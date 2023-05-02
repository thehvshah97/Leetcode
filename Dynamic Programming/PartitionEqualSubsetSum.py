class PartitionEqualSubsetSum:
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

    def recursionCalling(self, arr: list) -> bool:
        if sum(arr) % 2 != 0:
            return False
        else:
            return self.recursion(arr, len(arr) - 1, sum(arr)/2)
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
    def dynamicProgrammingMemoizationCalling(self, arr: list) -> bool:
        if sum(arr) % 2 != 0:
            return False
        else:
            dp = [False] * len(arr)
            return self.dynamicProgrammingMemoization(arr, len(arr) - 1, sum(arr) / 2, dp)


if __name__ == '__main__':
    partitionEqualSubsetSum = PartitionEqualSubsetSum()
    print(partitionEqualSubsetSum.recursionCalling([1, 5, 11, 5]))
    print(partitionEqualSubsetSum.dynamicProgrammingMemoizationCalling([1, 5, 11, 5]))

