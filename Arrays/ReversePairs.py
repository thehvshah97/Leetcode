from typing import List
import math

class ReversePairs:
    def bruteForce(self, nums: List[int]) -> int:
        reversepairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    reversepairs += 1
        return reversepairs

    def reversePairsOptimized(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums: List[int], left: int, right: int):
        cnt = 0
        if left >= right:
            return cnt
        else:
            mid = math.floor((left + right)/2)
            cnt += self.mergeSort(nums, left, mid)
            cnt += self.mergeSort(nums, mid + 1, right)
            cnt += self.countPairs(nums, left, mid, right)
            self.merge(nums, left, mid, right)
            return cnt

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        low, high = left, mid + 1
        temp = []
        while low <= mid and high <= right:
            if nums[low] <= nums[high]:
                temp.append(nums[low])
                low += 1
            else:
                temp.append(nums[high])
                high += 1

        while low <= mid:
            temp.append(nums[low])
            low += 1

        while high <= right:
            temp.append(nums[high])
            high += 1

        for i in range(left, right + 1):
            nums[i] = temp[i - left]

    def countPairs(self, nums: List[int], left: int, mid: int, right: int) -> int:
        cnt = 0
        high = mid + 1
        for i in range(left, mid + 1):
            while high <= right and nums[i] > 2 * nums[high]:
                high += 1
            cnt += (high - (mid + 1))
        return cnt


if __name__ == '__main__':
    reversePairs = ReversePairs()
    print(reversePairs.bruteForce([1, 3, 2, 3, 1]))
    print(reversePairs.reversePairsOptimized([1, 3, 2, 3, 1]))
