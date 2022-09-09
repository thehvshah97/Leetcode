from typing import List


class RemoveDuplicatesFromList:
    def removeduplicates(nums: List[int]) -> int:
        return len(list(set(nums)))


if __name__ == '__main__':
    print(RemoveDuplicatesFromList.removeduplicates([1, 1, 2, 2, 3]))
