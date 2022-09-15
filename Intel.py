from typing import List


class Intel:
    def intel(nums: list, places: list) -> list:
        vowels = "aeiou"
        result = []
        for place in places:
            countOfVowels = 0
            for i in range(int(place[:place.find("-")])-1, int(place[place.rfind("-")+1:])):
                if i < len(nums) and nums[i][0] in vowels and nums[i][len(nums[i])-1] in vowels:
                    countOfVowels += 1
            result.append(countOfVowels)
        return result


if __name__ == '__main__':
    print(Intel.intel(["aba", "bcb", "ece", "aa", "a"], ["1-3", "2-5", "2-2"]))
