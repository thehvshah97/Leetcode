from typing import List


class SearchInsertPosition:
    def searchinsert(nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
        return len(nums)


if __name__ == '__main__':
    print(SearchInsertPosition.searchinsert([1, 3, 5, 6], 7))
