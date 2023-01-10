from typing import List


class MajorityNumber:
    # Sort the array and return the number at N/2 position as the Majority Number appears more than N/2 time
    def majorityElementSorting(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]

    # Calculate count of the current number selected as candidate and if count reaches 0 replace the candidate with a new Number
    def majorityElementOptimized(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in range(len(nums)):
            if candidate == nums[i]:
                count += 1
            elif count == 0:
                candidate = nums[i]
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    majorityNumber = MajorityNumber()
    print(majorityNumber.majorityElementOptimized([3, 3, 4]))
