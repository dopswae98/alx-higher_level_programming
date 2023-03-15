#!/usr/bin/python3
def multiple_returns(sentence):
    t = ()
    length = len(sentence)
    if length == 0:
        t = (0, None)
    else:
        first_letter = sentence[0]
        t = (length, first_letter)
    return t
