import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        denominator = sum(w)
        #calculate probabilities for each index
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denominator

        #calculate the running sum of probabilities which is going to be plotted on a number line
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        #random number selected between 0 and 1
        rand = random.uniform(0, 1)
        flag = False
        index = -1
        #since all the numbers have uniform probability of getting picked we traverse the weight array to find number smaller or equal to current number
        while not flag:
            index += 1
            if rand <= self.w[index]:
                flag = True
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
