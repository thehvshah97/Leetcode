def count_palindromic_substrings(s):
    count = 0

    def expand_around_center(start, end):
        nonlocal count
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1

    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)

    return count


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"The number of palindromic substrings in '{s}' is: {count_palindromic_substrings(s)}")