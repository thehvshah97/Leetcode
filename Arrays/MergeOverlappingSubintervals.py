from typing import List


class MergeOverlappingIntervals:
    def mergeBruteForce(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        interval = 0
        while interval < len(intervals):
            if interval == len(intervals) - 1:
                result.append(intervals[interval])
                interval += 1
            else:
                start1 = intervals[interval][0]
                start2 = intervals[interval + 1][0]
                end1 = intervals[interval][1]
                end2 = intervals[interval + 1][1]
                if end1 >= start2:
                    for i in range(interval+1, len(intervals)):
                        if max(end1, end2) >= intervals[i][0]:
                            end2 = max(end2, intervals[i][1])
                            interval += 1
                    result.append([start1, max(end1, end2)])
                    interval += 1
                else:
                    result.append([start1, end1])
                    interval += 1
        return result

    def mergeOptimal(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start1 = result[len(result) - 1][0]
            start2 = intervals[i][0]
            end1 = result[len(result) - 1][1]
            end2 = intervals[i][1]
            if end1 >= start2:
                result[len(result) - 1] = [min(start1, start2), max(end1, end2)]
            else:
                result.append(intervals[i])
        return result


if __name__ == '__main__':
    mergeOverlapping = MergeOverlappingIntervals()
    print(mergeOverlapping.mergeBruteForce([[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5], [0, 2], [3, 3]]))
    print(mergeOverlapping.mergeBruteForce([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(mergeOverlapping.mergeBruteForce([[1, 4], [0, 2], [3, 5]]))
    print(mergeOverlapping.mergeOptimal([[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5], [0, 2], [3, 3]]))
    print(mergeOverlapping.mergeOptimal([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(mergeOverlapping.mergeOptimal([[1, 4], [0, 2], [3, 5]]))
