from typing import List


class Meetings:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class NMeetings:
    def greedy(self, start: List[int], end: List[int]) -> int:
        meetings = [Meetings(start[i], end[i]) for i in range(len(start))]
        max_meetings = 1
        sorted(meetings, key=lambda x: x.end)
        meet_end = meetings[0].end
        for i in range(1, len(meetings)):
            if meetings[i].start > meet_end:
                meet_end = meetings[i].end
                max_meetings += 1
        return max_meetings


if __name__ == '__main__':
    N_Meetings = NMeetings()
    print(N_Meetings.greedy([1, 3, 0, 5, 8, 5], [2, 4, 5, 7, 9, 9]))
