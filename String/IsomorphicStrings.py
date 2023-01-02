class IsomorphicStrings:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict and t[i] not in dict.values():
                dict[s[i]] = t[i]
            elif s[i] not in dict and t[i] in dict.values():
                return False
            elif t[i] != dict[s[i]]:
                return False
        print(dict)
        return True


if __name__ == '__main__':
    obj = IsomorphicStrings()
    print(obj.isIsomorphic("bar","foo"))
