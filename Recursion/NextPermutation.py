class NextPermutation:
    def findPermutations(self, index: int, inputArr: list, result: list):
        if index == len(inputArr):
            res = inputArr.copy()
            result.append(res)
            return

        for i in range(index, len(inputArr)):
            self.swap(i, index, inputArr)
            self.findPermutations(index + 1, inputArr, result)
            self.swap(i, index, inputArr)

    def swap(self, i: int, j: int, inputArr: list):
        k = inputArr[i]
        inputArr[i] = inputArr[j]
        inputArr[j] = k


if __name__ == '__main__':
    nextPermutation = NextPermutation()
    result = []
    nextPermutation.findPermutations(0, [3, 1, 2], result)
    print(result)
    index = result.index([1, 2, 3])
    print(result[index + 1])
