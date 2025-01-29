from collections import deque
from typing import List


class SubarraySumDivsibleByK:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        prefix_sum = {-1: 0}
        num_ways = 0
        for i in range(len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        return num_ways


if __name__ == '__main__':
    subarraySumDivsibleByK = SubarraySumDivsibleByK()
    print(subarraySumDivsibleByK.subarray_sum([4, 5, 0, -2, -3, 1], 5))

