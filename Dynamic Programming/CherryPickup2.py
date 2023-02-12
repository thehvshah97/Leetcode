from typing import List
import numpy as np


class NinjaTraining:
    def trainingRecursion(self, points: List[List[int]], day: int, lastTask: int) -> int:
        if day == 0:
            maxPoints = 0
            for task in range(len(points[0])):
                if task != lastTask:
                    maxPoints = max(points[0][task], maxPoints)
            return maxPoints

        maxPoints = 0
        for task in range(len(points[0])):
            if task != lastTask:
                maxPoints = max(maxPoints, points[day][task] + self.trainingRecursion(points, day - 1, task))
        return maxPoints

    def trainingDynamicProgrammingMemoization(self, points: List[List[int]], day: int, lastTask: int, memoization: List[List[int]]) -> int:
        if day == 0:
            maxPoints = 0
            for task in range(len(points[0])):
                if task != lastTask:
                    maxPoints = max(points[0][task], maxPoints)
            return maxPoints

        if memoization[day][lastTask] != -1:
            return memoization[day][lastTask]

        maxPoints = 0
        for task in range(len(points[0])):
            if task != lastTask:
                maxPoints = max(maxPoints,
                                points[day][task] + self.trainingDynamicProgrammingMemoization(points, day - 1, task, memoization))
        memoization[day][lastTask] = maxPoints
        return memoization[day][lastTask]

    def trainingDynamicProgrammingTabulation(self, points: List[List[int]], day: int, lastTask: int) -> int:
        tabulation = np.zeros((len(points[0]), len(points)), int).tolist()
        for i in range(len(points[0])):
            val = points[0].pop(i)
            tabulation[0][i] = max(points[0])
            points[0].insert(i, val)

        for day in range(1, len(points)):
            for last in range(len(points[0])):
                for task in range(len(points[0])):
                    if task != last:
                        tabulation[day][last] = max(tabulation[day][last],
                                                    points[day][task] + tabulation[day - 1][task])
        return tabulation[-1][-1]

    def ninjaTraining(self, n: int, points: List[List[int]]) -> int:
        memoization = [[-1] * (len(points[0]) + 1)] * len(points)
        return self.trainingDynamicProgrammingTabulation(points, n - 1, len(points[0]))


if __name__ == '__main__':
    ninjaTraining = NinjaTraining()
    print(ninjaTraining.ninjaTraining(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
