from typing import List

class PlusOne:
    def plusOne(digits: List[int]) -> List[int]:
        digits.reverse()
        for i in range(len(digits)):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = digits[i] % 10
            else:
                digits.reverse()
                return digits
        digits.insert(len(digits), 1)
        digits.reverse()
        return digits


if __name__ == '__main__':
    print(PlusOne.plusOne([9]))
