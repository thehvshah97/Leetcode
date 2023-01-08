class RepeatAndMissingNumber:
    def findRepeatAndMissing(self, nums: list) -> list:
        d = {}
        missing = 0
        repeat = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                repeat = i
                d[i] += 1

        keys = d.keys()
        for i in range(len(keys) + 1):
            if i not in keys:
                missing = i
        return [missing, repeat]


if __name__ == '__main__':
    repeatAndMissingNumber = RepeatAndMissingNumber()
    print(repeatAndMissingNumber.findRepeatAndMissing([1, 3, 5, 4, 4]))
