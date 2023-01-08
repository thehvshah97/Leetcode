from typing import List


class SingleNumber:
    def findSingleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        print(d)
        for key, value in d.items():
            print(key)
            if value == 1:
                return key


if __name__ == '__main__':
    singleNumber = SingleNumber()
    print(singleNumber.findSingleNumber([4, 1, 2, 1, 2]))
