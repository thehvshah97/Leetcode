from typing import List


class Subsets:
    def find_subsets_recursion(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def createSubset(index):
            if index == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[index])
            createSubset(index + 1)

            subset.pop()
            createSubset(index + 1)

        createSubset(0)
        return result
