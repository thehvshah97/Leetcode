from typing import List


class FindDuplicate:
    def findDuplicateNaive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicateDict(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return i


if __name__ == '__main__':
    findDuplicateNumber = FindDuplicate()
    print(findDuplicateNumber.findDuplicateNaive([1, 3, 4, 2, 2]))
    print(findDuplicateNumber.findDuplicateDict([1, 3, 4, 2, 2]))
