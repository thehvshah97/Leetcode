from typing import List


class MedianOfTwoSortedArray:
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        mergedArray = nums1 + nums2
        mergedArray.sort()
        if len(mergedArray) % 2 == 0:
            return (mergedArray[int(len(mergedArray)/2)]+mergedArray[int(len(mergedArray)/2-1)])/2
        else:
            return mergedArray[int((len(mergedArray))/2)]

if __name__ == '__main__':
    print(MedianOfTwoSortedArray.findMedianSortedArrays([1,2],[4]))
