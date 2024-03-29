from typing import List


class FourSum:
    def FourSumNaive(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            if temp not in result:
                                result.append(temp)
        return result

    def FourSumOptimized(self, nums: List[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if target - nums[i] - nums[j] - nums[k] in nums:
                        l = nums.index(target - nums[i] - nums[j] - nums[k])
                        if l != i and l != j and l != k:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            if temp not in result:
                                result.append(temp)
        return result

    def FourSumOptimal(self, nums: List[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sums = nums[i] + nums[j] + nums[k] + nums[l]
                    if sums == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        if temp not in result:
                            result.append(temp)
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sums >= target:
                        l -= 1
                    else:
                        k += 1
        return result


if __name__ == '__main__':
    fourSums = FourSum()
    print(fourSums.FourSumNaive([1,0,-1,0,-2,2], 0))
    print(fourSums.FourSumOptimized([1,0,-1,0,-2,2], 0))
    print(fourSums.FourSumOptimal([1,0,-1,0,-2,2], 0))
