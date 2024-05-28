from typing import List


class Jobs:
    def __init__(self, job_id: int, end: int, profit: int):
        self.job_id = job_id
        self.end = end
        self.profit = profit


class JobSequencing:
    def greedy(self, job_id: List[int], end: List[int], profit: List[int]):
        jobs = [Jobs(job_id[i], end[i], profit[i]) for i in range(len(job_id))]
        sorted(jobs, key=lambda x: x.profit)
        profits = [0] * (max(end) + 1)
        for i in range(len(jobs)):
            if profits[jobs[i].end] < jobs[i].profit:
                profits[jobs[i].end] = jobs[i].profit
        return sum(profits)


if __name__ == '__main__':
    job_scheduling = JobSequencing()
    print(job_scheduling.greedy([1, 2, 3, 4], [4, 1, 1, 1], [20, 10, 40, 30]))


