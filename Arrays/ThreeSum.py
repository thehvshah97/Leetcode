from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
