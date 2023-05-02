import numpy as np

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

    def dynamicProgrammingTabulation(self, arr: list) -> bool:
        if sum(arr) % 2 != 0:
            return False
        target = int(sum(arr)/2)
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
        return dp[-1][target]


if __name__ == '__main__':
    partitionEqualSubsetSum = PartitionEqualSubsetSum()
    print(partitionEqualSubsetSum.recursionCalling([1, 5, 11, 5]))
    print(partitionEqualSubsetSum.dynamicProgrammingMemoizationCalling([1, 5, 11, 5]))
    print(partitionEqualSubsetSum.dynamicProgrammingTabulation([1, 5, 11, 5]))

