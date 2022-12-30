from typing import List


class PivotIndex:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for index, value in enumerate(nums):
            rightSum -= value
            if leftSum == rightSum:
                return index
            leftSum += value
        return -1


if __name__ == '__main__':
    obj = PivotIndex()
    print(obj.pivotIndex([-1, -1, 0, 1, 1, 0]))
