"""Find longest word in the provided dictionary."""


def findLongestWord(s, d):
    """Longest word in dictionary from the provided string via deleting."""
    # first sort dict by (1) word length and then by (2) lexicographically\
    # smallest using list.sort() by providing your own key function.
    d.sort(key=lambda x: (-len(x), x))
    # word with largest length will end up with the smallest number b/o neg
    # pay attention: tuple is given to provide more than one function for

    for word in d:
        i = 0
        for char in s:
            if i < len(word) and word[i] == char:
                i += 1
        if i == len(word):
            return word
    return ""
    """
    first start with the longest word since dict was sorted by longest word
    first.
    iterating string by each char and increment i whenever i < len(word) and
    word[i] matches to one of char of string (while iterating string)
    after finishing iteration, if final i matches to length of word, then it
    means given word can be formed in a string by deleting character(s)

    """
