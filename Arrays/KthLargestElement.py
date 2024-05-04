import heapq
from typing import List


class KthLargestElement:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, -nums[i])

        while k > 1:
            heapq.heappop(pq)
            k -= 1

        return -pq[0]


if __name__ == '__main__':
    kth_largest = KthLargestElement()
    print(kth_largest.find_kth_largest([1, 2, 4, 6, 5, 3], 3))
