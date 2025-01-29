class ValidWordAbbreviation:
    def validWord(self, word: str, abbr: str) -> bool:
        if len(word) < len(abbr):
            return False
        abbr_index = 0
        word_index = 0
        while abbr_index < len(abbr):
            char = abbr[abbr_index]
            if char.isnumeric():
                if char == '0':
                    return False
                else:
                    num = 0
                    while abbr_index < len(abbr) and abbr[abbr_index].isnumeric():
                        num = num * 10 + int(abbr[abbr_index])
                        abbr_index += 1

                    word_index += num
            else:
                if word_index >= len(word) or word[word_index] != char:
                    return False
                abbr_index += 1
                word_index += 1
        return word_index == len(word)

if __name__ == '__main__':
    print(ValidWordAbbreviation().validWord("apple", "a2le"))