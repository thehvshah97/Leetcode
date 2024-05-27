from typing import List


class StrengthOfWizards:
    def brute_force(self, strength: List[int]) -> int:
        subsets = [strength[i: j] for i in range(len(strength) + 1) for j in range(i + 1, len(strength) + 1)]
        result = 0
        for subset in subsets:
            power = min(subset) * sum(subset)
            result += power
        return result


if __name__ == '__main__':
    strength_of_wizards = StrengthOfWizards()
    print(strength_of_wizards.brute_force([1, 3, 1, 2]))

