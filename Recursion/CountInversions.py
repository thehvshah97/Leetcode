class CountInversions:
    def countInversion(self, nums: list) -> int:
        inversions = 0
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            inversions += self.countInversion(left)
            inversions += self.countInversion(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    inversions += (mid - i)
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        return inversions


if __name__ == '__main__':
    countInversions = CountInversions()
    print(countInversions.countInversion([5, 3, 2, 1, 4]))
