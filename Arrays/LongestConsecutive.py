from collections import defaultdict
from typing import List


class LongestConsecutive:
    def longestConsecutiveOptimized(self, nums: List[int]) -> int:
        vertex = defaultdict(list)
        visited = defaultdict(bool)
        max_consecutive = 0
        for i in nums:
            if visited[i]:
                continue
            visited[i] = True
            left, right = i, i
            if vertex[i + 1]:
                right = vertex[i + 1][0]
            if vertex[i - 1]:
                left = vertex[i - 1][1]
            vertex[left] = [right, left]
            vertex[right] = [right, left]
            max_consecutive = max(max_consecutive, right - left + 1)
        return max_consecutive


if __name__ == '__main__':
    longestConsecutive = LongestConsecutive()
    print(longestConsecutive.longestConsecutiveOptimized([100, 4, 200, 1, 3, 2]))

