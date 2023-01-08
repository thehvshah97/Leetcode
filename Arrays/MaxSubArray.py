class MaxSubArray:
    def maxSubArray(self, nums: list) -> int:
        maxSum = nums[0]
        localSum = 0
        for i in nums:
            localSum += i
            if maxSum < localSum:
                maxSum = localSum
            if localSum <= 0:
                localSum = 0
        return maxSum


if __name__ == '__main__':
    maxSum = MaxSubArray()
    print(maxSum.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
