from typing import List


class TwoSum:
    def twosum(nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i


if __name__ == '__main__':
    print(TwoSum.twosum([3, 3], 6))
