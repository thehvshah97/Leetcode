from itertools import combinations
from typing import List


class PayPal:
    def countVowels(nums: list, places: list) -> list:
        vowels = "aeiou"
        result = []
        for place in places:
            countOfVowels = 0
            for i in range(int(place[:place.find("-")]) - 1, int(place[place.rfind("-") + 1:])):
                if i < len(nums) and nums[i][0] in vowels and nums[i][len(nums[i]) - 1] in vowels:
                    countOfVowels += 1
            result.append(countOfVowels)
        return result

    def wholeMinute(time: List[int]) -> int:
        countsOfSongs = {}
        result = 0
        for song in time:
            modulo = song % 60
            if modulo not in countsOfSongs:
                countsOfSongs[modulo] = 0
            countsOfSongs[modulo] += 1

        if 0 in countsOfSongs:
            result += (countsOfSongs[0] * (countsOfSongs[0] - 1)) / 2

        if 30 in countsOfSongs:
            result += (countsOfSongs[30] * (countsOfSongs[30] - 1)) / 2

        for i in range(1, 30):
            if i in countsOfSongs and 60 - i in countsOfSongs:
                result = result + (countsOfSongs[i] * countsOfSongs[60 - i])

        return int(result)

    def wholeMinuteCombinations(time: List[int]) -> int:
        pairs = combinations(time, 2)
        result = 0
        for pair in pairs:
            if (pair[0] + pair[1]) % 60 == 0:
                result += 1
        return result

    def minimumAbsoluteDifference(arr: List[int]) -> List[List[int]]:
        result = []
        diffDict = {}
        arr.sort()
        for place in range(0, len(arr)-1):
            diffDict[arr[place], arr[place+1]] = abs(arr[place+1] - arr[place])

        mimimumDiff = min(diffDict.values())

        for key, value in diffDict.items():
            if value == mimimumDiff:
                result.append(list(key))
        return result

if __name__ == '__main__':

    print(PayPal.wholeMinute([10, 50, 90, 30]))


