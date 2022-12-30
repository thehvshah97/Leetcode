class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        longestString = 1
        l, r = 0, 0
        for mid in range(1, len(s)):
            l = 0
            r = mid*2
            lp, rp = mid
            while lp!=l and rp!=r:
                if 
        return s[l:r]

if __name__ == '__main__':
    obj = LongestPalindromicSubstring
    print(LongestPalindromicSubstring.longestPalindrome("babac"))