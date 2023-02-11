from typing import List


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

    def trainingDynamicProgrammingMemoization(self, points: List[List[int]], day: int, lastTask: int,
                                              memoization: List[List[int]]) -> int:
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
                                points[day][task] + self.trainingDynamicProgrammingMemoization(points, day - 1, task,
                                                                                               memoization))
        memoization[day][lastTask] = maxPoints
        return memoization[day][lastTask]

    def ninjaTraining(self, n: int, points: List[List[int]]) -> int:
        memoization = [[-1] * (len(points[0]) + 1)] * len(points)
        return self.trainingDynamicProgrammingMemoization(points, n - 1, len(points[0]), memoization)


if __name__ == '__main__':
    ninjaTraining = NinjaTraining()
    print(ninjaTraining.ninjaTraining(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
