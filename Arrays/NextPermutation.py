from typing import List


class NextPermutation:
    def nextPermutation(self, nums: List[int]):
        ind = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        if ind == -1:
            temp = [nums[i] for i in range(len(nums))]
            ind = len(nums) - 1
            for i in range(len(nums)):
                nums[i] = temp[ind]
                ind -= 1

        else:
            for i in range(len(nums) - 1, ind, -1):
                if nums[i] > nums[ind]:
                    x = nums[i]
                    nums[i] = nums[ind]
                    nums[ind] = x
                    break
            nums[ind + 1:] = nums[ind + 1:][::-1]
        return nums


if __name__ == '__main__':
    nextPermutation = NextPermutation()
    nums = [3, 2, 1]
    print(nextPermutation.nextPermutation(nums))
    print(nums)
