"""Reverses each words."""


def reverse_words(text):
    """Reverse words."""
    result = []
    space_split = text.split(' ')
    for i in space_split:
        reversed = ''
        for k in i:
            reversed = k + reversed
        result.append(reversed)
    return ' '.join(result)


def other_reverse_words(str):
    """Best practices."""
    return ' '.join(s[::-1] for s in str.split(' '))
