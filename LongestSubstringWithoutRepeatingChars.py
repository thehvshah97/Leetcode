class LongestSubstringWithoutRepeatingChars:
    def longestSubstringWithoutRepeatingChars(s: str) -> int:
        listOfChars= list(s)
        longestSubstring = 0
        for i in range(0, len(listOfChars)):
            charsVisited = []
            currentLongest = 0
            if i + longestSubstring > len(listOfChars):
                break
            else:
                for j in range(i, len(listOfChars)):
                    if listOfChars[j] in charsVisited:
                        break

                    elif j not in charsVisited:
                        charsVisited.append(listOfChars[j])
                        currentLongest += 1

                    if currentLongest > longestSubstring:
                        longestSubstring = currentLongest

        return longestSubstring

if __name__ == '__main__':
    print(LongestSubstringWithoutRepeatingChars.longestSubstringWithoutRepeatingChars("aabc"))
