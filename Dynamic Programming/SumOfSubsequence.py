class SumOfSubsequence:
    def sumOfSubsequencerecursion(self, index: int, inputArr: list, subSequence: list, result: list, n: int,
                                  target: int):
        if index >= n:
            res = subSequence.copy()
            if sum(subSequence) == target:
                result.append(res)
            return
        subSequence.append(inputArr[index])
        self.sumOfSubsequencerecursion(index + 1, inputArr, subSequence, result, n, target)
        subSequence.remove(inputArr[index])
        self.sumOfSubsequencerecursion(index + 1, inputArr, subSequence, result, n, target)


if __name__ == '__main__':
    subsequence = SumOfSubsequence()
    result = []
    sequence = []
    subsequence.sumOfSubsequencerecursion(0, [1, 2, 3, 4], sequence, result, 4, 4)
    print(result)
