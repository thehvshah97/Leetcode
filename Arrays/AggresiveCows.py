# Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls.
# You are also given an integer 'k' which denotes the number of aggressive cows.
# You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible.
# Find the maximum possible minimum distance.
from typing import List


class AgressiveCows:
    def findMinimumDistance(self, distance: List[int], cows: int) -> int:
        distance.sort()
        low, high = 1, distance[-1] - distance[0]
        while low <= high:
            mid = (low + high) // 2
            minDistance = self.calculate_distance(distance, cows, mid)
            if minDistance:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def calculate_distance(self, distance, cows, mid) -> bool:
        num_cows = 1
        last_position = distance[0]
        for i in range(1, len(distance)):
            if distance[i] - last_position >= mid:
                num_cows += 1
                last_position = distance[i]
        if num_cows >= cows:
            return True
        return False


if __name__ == '__main__':
    aggressiveCows = AgressiveCows()
    print(aggressiveCows.findMinimumDistance([0, 3, 4, 7, 10, 9], 4))

