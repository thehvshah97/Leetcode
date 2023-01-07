from typing import List


# Merge Sorted Arrays without extra space
class MergeSortedArrays:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n -= 1
        for i in range(m, len(nums1)):
            nums1[i] = nums2[n]
            n -= 1
        nums1.sort()


if __name__ == '__main__':
    mergeOverlapping = MergeSortedArrays()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6]
    n = 3
    mergeOverlapping.merge(nums1, m, nums2, n)
    print(nums1)
