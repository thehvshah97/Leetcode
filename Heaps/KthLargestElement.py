import heapq
from typing import List


class KthLargestElement:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, -1 * num)
        num = 0
        while k > 0:
            num = -1 * heapq.heappop(heap)
            k -= 1
        return num

