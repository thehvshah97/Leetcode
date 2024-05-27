from typing import List


class LongestValidSubstring:
    def brute_force(self, s: str, forbidden: List[str]) -> int:
        substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        max_len = 0
        for substring in substrings:
            for word in forbidden:
                if word in substring:
                    break
                else:
                    max_len = max(max_len, len(substring))
        return max_len

    def optimized(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        max_len = 0
        right = len(word) - 1
        for i in range(len(word) - 1, -1, -1):
            for j in range(i, min(i+10, right + 1)):
                substring = word[i:j + 1]
                if substring in forbidden:
                    right = j - 1
                    break
            max_len = max(max_len, right - i + 1)
        return max_len


if __name__ == '__main__':
    longest_valid_substring = LongestValidSubstring()
    print(longest_valid_substring.brute_force('cbaaaabc', ['aaa', 'cb']))
    print(longest_valid_substring.optimized('cbaaaabc', ['aaa', 'cb']))
