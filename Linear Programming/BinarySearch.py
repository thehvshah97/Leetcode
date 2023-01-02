from typing import List

class BinarySearch:
    def search(nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while high >= low:
            mid = int((high+low)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return -1


if __name__ == '__main__':
    print(BinarySearch.search([-1, 0, 3, 5, 9, 12], 9))
