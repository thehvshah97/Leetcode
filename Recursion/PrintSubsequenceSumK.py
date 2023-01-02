class SubSequenceSumK:
    def recursion(self, index: int, inputArr: list, subSequence: list,  s: int):
        if index == len(inputArr):
            if sum(subSequence) == s:
                print(subSequence)
            return
        subSequence.append(inputArr[index])
        self.recursion(index + 1, inputArr, subSequence, s)
        subSequence.remove(inputArr[index])
        self.recursion(index + 1, inputArr, subSequence, s)


class OnlyOneSubsequence:
    def recursion(self, index: int, inputArr: list, subSequence: list,  s: int) -> bool:
        if index == len(inputArr):
            if sum(subSequence) == s:
                print(subSequence)
                return True
            else:
                return False
        subSequence.append(inputArr[index])
        if self.recursion(index + 1, inputArr, subSequence, s):
            return True
        subSequence.remove(inputArr[index])
        self.recursion(index + 1, inputArr, subSequence, s)
        return False


if __name__ == '__main__':
    #subSequenceSumK = SubSequenceSumK()
    #subSequenceSumK.recursion(0, [1, 2, 1], [], 2)
    onlyOneSubsequence = OnlyOneSubsequence()
    onlyOneSubsequence.recursion(0, [1, 2, 1], [], 2)
