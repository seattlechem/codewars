# https://www.codewars.com/kata/is-it-a-number/python


def isDigit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
