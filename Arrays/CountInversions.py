import math
from typing import List


class CountInversions:
    def bruteForce(self, nums: List[int]) -> int:
        inversions = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    inversions += 1
        return inversions

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        low, high = left, mid + 1
        temp = []
        cnt = 0
        while low <= mid and high <= right:
            if nums[low] <= nums[high]:
                temp.append(nums[low])
                low += 1
            else:
                temp.append(nums[high])
                cnt += (mid - low + 1)
                high += 1
        while low <= mid:
            temp.append(nums[low])
            low += 1
        while high <= right:
            temp.append(nums[high])
            high += 1
        for i in range(left, right + 1):
            nums[i] = temp[i - left]
        return cnt

    def mergeSort(self, nums: List[int], left: int, right: int):
        cnt = 0
        if left >= right:
            return cnt
        else:
            mid = math.floor((left + right)/2)
            cnt += self.mergeSort(nums, left, mid)
            cnt += self.mergeSort(nums, mid + 1, right)
            cnt += self.merge(nums, left, mid, right)
            return cnt


if __name__ == '__main__':
    countInversions = CountInversions()
    print(countInversions.bruteForce([3, 2, 1]))
    print(countInversions.mergeSort([3, 2, 1], 0, 2))

