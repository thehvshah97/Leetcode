class Subsequence:
    def recursion(self, index: int, inputArr: list, subSequence: list, result: list, n: int):
        if index >= n:
            res = subSequence.copy()
            result.append(res)
            return
        subSequence.append(inputArr[index])
        self.recursion(index + 2, inputArr, subSequence, result, n)
        subSequence.remove(inputArr[index])
        self.recursion(index + 2, inputArr, subSequence, result, n)

if __name__ == '__main__':
    subsequence = Subsequence()
    result = []
    sequence = []
    subsequence.recursion(0, [3, 1, 2], sequence, result, 3)
    print(result)

