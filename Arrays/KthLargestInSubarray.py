import heapq
from typing import List


class KthLargestElementSubarray:
    def find_kth_largest_subarray_bruteforce(self, nums: List[int], m: int, k: int) -> List[int]:
        result = []
        for i in range(len(nums) - m + 1):
            j = i
            pq = []
            for j in range(j, j + m):
                heapq.heappush(pq, -nums[j])

            l = k - 1
            while l > 0:
                heapq.heappop(pq)
                l -= 1
            result.append(-pq[0])
        return result

    def find_kth_largest_subarray(self, nums: List[int], m: int, k: int) -> List[int]:
        result = []
        subarray = nums[:m]
        heapq.heapify(subarray)
        k_largest = heapq.nlargest(k, subarray)[-1]
        result.append(k_largest)

        # Slide the window and find the kth largest element for each subarray
        for i in range(m, len(nums)):
            # Remove the first element from the previous subarray
            subarray.remove(nums[i - m])

            # Add the new element to the current subarray
            subarray.append(nums[i])

            # Update the heap
            heapq.heapify(subarray)

            # Find the kth largest element
            k_largest = heapq.nlargest(k, subarray)[-1]
            result.append(k_largest)

        return result


if __name__ == '__main__':
    kth_largest = KthLargestElementSubarray()
    print(kth_largest.find_kth_largest_subarray([1, 2, 4, 6, 5, 3], 3, 2))
