from typing import List


class BuildingWithOceanView:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        answer = []
        for i in reversed(range(n)):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()

            if not stack:
                answer.append(i)

            stack.append(i)
        return answer[::-1]
