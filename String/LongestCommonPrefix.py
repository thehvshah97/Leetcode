class LongestCommonPrefix:
    def longestcommonprefix(strs: list[str]) -> str:
        result = min(strs, key=len)
        while True:
            flag= True
            for string in strs:
                if result!=string[0:len(result)]:
                    flag=False
                    break
            if flag:
                break
            else:
                result = result[0:len(result)-1]
        return result


if __name__ == '__main__':
    print(LongestCommonPrefix.longestcommonprefix(["car", "cat", "apple"]))

