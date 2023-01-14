from typing import List


class MajorityElement:
    def majorityElementNaive(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        res = []
        for key, value in d.items():
            if value > len(nums) / 3:
                res.append(key)
        return res

    def majorityElementOptimized(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = -1, -1
        count1 = 0
        count2 = 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        res = []
        if count1 > len(nums) / 3:
            res.append(candidate1)
        if count2 > len(nums) / 3:
            res.append(candidate2)
        return res


if __name__ == '__main__':
    majorityElement = MajorityElement()
    print(majorityElement.majorityElementNaive([2, 2, 1, 3]))
    print(majorityElement.majorityElementOptimized([2, 2, 1, 3]))
