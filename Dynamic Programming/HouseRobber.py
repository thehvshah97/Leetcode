class HouseRobber:
    def recursion(self, index: int, inputArr: list,) -> int:
        if index == 0:
            return inputArr[0]
        elif index < 0:
            return 0

        pick = inputArr[index] + self.recursion(index - 2, inputArr)
        notPick = 0 + self.recursion(index - 1, inputArr)
        return max(pick, notPick)

    def dynamicProgrammingMemoization(self, index: int, inputArr: list, values: list) -> int:
        if index == 0:
            return inputArr[0]
        elif index < 0:
            return 0

        if values[index] != -1:
            return values[index]
        pick = inputArr[index] + self.recursion(index - 2, inputArr)
        notPick = 0 + self.recursion(index - 1, inputArr)
        values[index] = max(pick, notPick)
        return values[index]

    def dynamicProgrammingTabulation(self, inputArr: list) -> int:
        values = [-1] * len(inputArr)
        values[0] = inputArr[0]
        for i in range(1, len(inputArr)):
            pick = inputArr[i]
            if i > 1:
                pick += values[i-2]
            notPick = values[i-1]
            values[i] = max(pick, notPick)
        return values[len(inputArr) - 1]

    def dynamicProgrammingTabulationSpaceOptimized(self, inputArr: list) -> int:
        prev = inputArr[0]
        prev2 = 0
        for i in range(1, len(inputArr)):
            pick = inputArr[i]
            if i > 1:
                pick += prev2
            notPick = prev
            curr = max(pick, notPick)
            prev2 = prev
            prev = curr
        return prev


if __name__ == '__main__':
    houseRobber = HouseRobber()
    inputArr = [2, 1]
    values = [-1] * len(inputArr)
    print("Recursion(TLE):", houseRobber.recursion(len(inputArr) - 1, inputArr))
    print("Memoization(TLE):", houseRobber.dynamicProgrammingMemoization(len(inputArr) - 1, inputArr, values))
    print("Tabulation:", houseRobber.dynamicProgrammingTabulation(inputArr))
    print("Tabulation Space Optimized", houseRobber.dynamicProgrammingTabulationSpaceOptimized(inputArr))

