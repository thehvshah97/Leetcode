from typing import List


class FindFirstAndLastPositionInSorted:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(low, high, is_search_left):
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    index = mid
                    if is_search_left:
                        high = mid - 1
                    else:
                        low = mid + 1
            return index

        left = binary_search(0, len(nums) - 1, True)
        right = binary_search(0, len(nums) - 1, False)
        return [left, right]
