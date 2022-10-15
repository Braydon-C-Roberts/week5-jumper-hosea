from random import randint

WORDS = [
    "python",
    "bacon",
    "ted",
    "apples",
    "pineapples"
]


def pick():
    return WORDS[randint()%len(WORDS)]