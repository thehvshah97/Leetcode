class SortColors:
    def sorting(self, inputArr: list):
        inputArr.sort()

    def countColors(self, inputArr: list):
        low, mid = 0, 0
        high = len(inputArr) - 1
        while mid <= high:
            if inputArr[mid] == 0:
                k = inputArr[mid]
                inputArr[mid] = inputArr[low]
                inputArr[low] = k
                low += 1
                mid += 1
            elif inputArr[mid] == 1:
                mid += 1
            elif inputArr[mid] == 2:
                k = inputArr[mid]
                inputArr[mid] = inputArr[high]
                inputArr[high] = k
                high -= 1


if __name__ == '__main__':
    sortColors = SortColors()
    nums = [2, 0, 2, 1, 1, 0]
    sortColors.countColors(nums)
    print("Sorting:", nums)
