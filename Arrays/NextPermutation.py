from typing import List


class NextPermutation:
    def nextPermutation(self, nums: List[int]):
        break_point = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break
        if break_point < 0:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, break_point, -1):
                if nums[i] > nums[break_point]:
                    nums[i], nums[break_point] = nums[break_point], nums[i]
                    break
            nums[break_point + 1:] = nums[break_point + 1:][::-1]


if __name__ == '__main__':
    nextPermutation = NextPermutation()
    nums = [3, 2, 1]
    print(nextPermutation.nextPermutation(nums))
    print(nums)
