from typing import List


class Trains:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class NPlatfroms:
    def greedy(self, arrival: List[int], departure: List[int]) -> int:
        trains = [Trains(arrival[i], departure[i]) for i in range(len(arrival))]
        platforms = []
        platforms.append(trains[0].end)
        for i in range(1, len(trains)):
            index = self.isPossible(trains[i].start, platforms)
            if index != -1:
                platforms[index] = trains[i].end
            else:
                platforms.append(trains[i].end)
        return len(platforms)

    def isPossible(self, arrival: int, platforms: List[int]) -> int:
        for i in range(len(platforms)):
            if arrival > platforms[i]:
                return i
        return -1


if __name__ == '__main__':
    n_platfroms = NPlatfroms()
    print(n_platfroms.greedy([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
