from typing import List


class MinOperationsReduce:
    def min_operations(self, nums: List[int], x: int):
        left = 0
        running_sum = 0
        target = sum(nums) - x
        max_length = - 1
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum > target and left <= right:
                running_sum -= nums[left]
                left += 1

            if running_sum == target:
                max_length = max(max_length, right - left + 1)

        return (len(nums) - max_length) if max_length != -1 else -1


if __name__ == '__main__':
    minOperations = MinOperationsReduce()
    print(minOperations.min_operations([1, 1, 4, 2, 3], 5))
