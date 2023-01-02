from typing import List


class RemoveDuplicatesFromList:
    def removeduplicates(nums: List[int]) -> int:
        nums[:] = list(set(nums))
        return len(nums)


if __name__ == '__main__':
    print(RemoveDuplicatesFromList.removeduplicates([1, 1, 2, 2, 3]))
