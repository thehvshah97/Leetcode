from typing import List
import numpy as np

class CherryPickup2:
    dp = 0
    def cherryPickupRecursion(self, grid: List[List[int]], level: int, robot1: int, robot2: int) -> int:
        # Base Case - Last level
        if robot1 < 0 or robot1 >= len(grid[0]) or robot2 < 0 or robot2 >= len(grid[0]):
            return 0
        if level == len(grid) - 1:
            if robot1 == robot2:
                return grid[level][robot1]
            else:
                return grid[level][robot1] + grid[level][robot2]
        maxValue = 0
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if robot1 == robot2:
                    maxValue = max(maxValue,
                                   self.cherryPickupRecursion(grid, level + 1, robot1 + i, robot2 + j) + grid[level][
                                       robot1])
                else:
                    maxValue = max(maxValue,
                                   self.cherryPickupRecursion(grid, level + 1, robot1 + i, robot2 + j) + grid[level][
                                       robot1] + grid[level][robot2])
        return maxValue

    def cherryPickupMemoization(self, grid: List[List[int]], level: int, robot1: int, robot2: int) -> int:
        if robot1 < 0 or robot1 >= len(grid[0]) or robot2 < 0 or robot2 >= len(grid[0]):
            return 0
        if level == len(grid) - 1:
            if robot1 == robot2:
                return grid[level][robot1]
            else:
                return grid[level][robot1] + grid[level][robot2]
        if self.dp[level][robot1][robot2] != 0:
            return self.dp[level][robot1][robot2]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if robot1 == robot2:
                    self.dp[level][robot1][robot2] = max(self.dp[level][robot1][robot2],
                                                         self.cherryPickupRecursion(grid, level + 1, robot1 + i,
                                                                                    robot2 + j) + grid[level][robot1])
                else:
                    self.dp[level][robot1][robot2] = max(self.dp[level][robot1][robot2],
                                                         self.cherryPickupRecursion(grid, level + 1, robot1 + i,
                                                                                    robot2 + j) + grid[level][robot1] +
                                                         grid[level][robot2])
        return self.dp[level][robot1][robot2]

    def cherryPickupRecursionCalling(self, grid: List[List[int]]) -> int:
        return self.cherryPickupRecursion(grid, 0, 0, len(grid[0]) - 1)

    def cherryPickupMemoizationCalling(self, grid: List[List[int]]) -> int:
        self.dp = [[[0 for k in range(len(grid))] for j in range(len(grid[0]))] for i in range(len(grid[0]))]
        return self.cherryPickupMemoization(grid, 0, 0, len(grid[0]) - 1)


if __name__ == '__main__':
    cherryPickup2 = CherryPickup2()
    print(cherryPickup2.cherryPickupRecursionCalling([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(cherryPickup2.cherryPickupMemoizationCalling([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
