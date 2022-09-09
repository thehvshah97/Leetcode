from typing import List


class RemoveElement:
    def removeelement(nums: List[int], val: int) -> int:
        last = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[last] = nums[i]
                last += 1
        return last


if __name__ == '__main__':
    print(RemoveElement.removeelement([0, 1, 2, 2, 3, 0, 4, 2], 2))
