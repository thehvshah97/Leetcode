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

    def repeatedNumber(self, A) -> List[int]:
        n = len(A)
        d = {}
        for i in range(n):
            if A[i] not in d:
                d[A[i]] = 0
            d[A[i]] += 1
    
        missing = -1
        duplicate = -1
        for i in range(n):
            if i not in d:
                missing = i
            elif d[i] > 1:
                duplicate = i
        return [duplicate, missing]


if __name__ == '__main__':
    missingNumber = MissingNumber()
    print(missingNumber.findMissingNumber([3, 0, 1]))
    print(missingNumber.repeatedNumber([3, 1, 2, 5, 3]))
