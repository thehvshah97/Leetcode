class Subsequence:
    def recursion(self, index: int, inputArr: list, subSequence: list, n: int):
        if index >= n:
            print(subSequence)
            return
        subSequence.append(inputArr[index])
        self.recursion(index + 1, inputArr, subSequence, n)
        subSequence.remove(inputArr[index])
        self.recursion(index + 1, inputArr, subSequence, n)


if __name__ == '__main__':
    subSequence = Subsequence()
    subSequence.recursion(0, [3, 1, 2], [], 3)

