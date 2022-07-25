import sys
from collections import namedtuple

Oddness = namedtuple('Oddness', 'odd even zero')
RETURN_VALUES = Oddness("I'm Odd.", "I'm Even.", "I'm Zero.")


Errors = namedtuple('Errors', 'invalid_argument too_much_arguments')
ERROR_VALUES = Errors(
    "AssertionError: argument is not an integer",
    "AssertionError: more than one argument are provided"
)


USAGE = """\
A program that takes a number as argument, checks whether it is odd, even or
zero, and print the result.
• If more than one argument are provided or if the argument is not an integer,
it prints an error message.

Ex:
    $> python3 whois.py 12
    I'm Even.

    $> python3 whois.py 3
    I'm Odd.

    $> python3 whois.py 0
    I'm Zero.

    $> python3 whois.py Hello
    AssertionError: argument is not an integer

    $> python3 whois.py 12 3
    AssertionError: more than one argument are provided\
"""


def whois(number: int):
    if number == 0:
        return RETURN_VALUES.zero
    elif number % 2 == 0:
        return RETURN_VALUES.even
    else:
        return RETURN_VALUES.odd


def main():
    if len(sys.argv) == 1:
        print(USAGE)
    elif len(sys.argv) == 2:
        try:
            print(whois(int(sys.argv[1])))
        except ValueError:
            print(ERROR_VALUES.invalid_argument)
    else:
        print(ERROR_VALUES.too_much_arguments)


if __name__ == '__main__':
    main()
