class HouseRobber2:
    def dynamicProgrammingTabulation(self, inputArr: list) -> int:
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

    def dynamicProgrammingCalling(self, inputArr: list) -> list:
        first = self.dynamicProgrammingTabulation(inputArr[0:len(inputArr)-1])
        last = self.dynamicProgrammingTabulation(inputArr[1:])
        return max(first, last)


if __name__ == '__main__':
    houseRobber2 = HouseRobber2()
    inputArr = [2, 3, 2]
    print("Tabulation Space Optimized:", houseRobber2.dynamicProgrammingCalling(inputArr))

