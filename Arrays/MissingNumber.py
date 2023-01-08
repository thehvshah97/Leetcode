from typing import List


class MissingNumber:
    def findMissingNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1

        keys = d.keys()
        for i in range(len(keys) + 1):
            if i not in keys:
                return i


if __name__ == '__main__':
    missingNumber = MissingNumber()
    print(missingNumber.findMissingNumber([3, 0, 1]))
