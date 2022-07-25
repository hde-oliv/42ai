import sys
from string import (
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
    whitespace
)


def text_analyzer(string: str = None):
    """
    This function counts the number of upper and lower characters
    and even punctuation and spaces in a given text!
    """

    if string is None:
        string = input("Which string?\n>> ")
    elif not isinstance(string, str):
        print("AssertionError: argument is not a string")
        return

    upper_case = 0
    lower_case = 0
    punct = 0
    spaces = 0

    for char in string:
        if char in ascii_lowercase:
            lower_case += 1
        elif char in ascii_uppercase:
            upper_case += 1
        elif char in punctuation:
            punct += 1
        elif char in whitespace:
            spaces += 1

    print(
        f"The text contains {len(string)} character(s)\n",
        f"- {upper_case} upper letter(s)\n",
        f"- {lower_case} lower letter(s)\n",
        f"- {punct} punctuation mark(s)\n",
        f"- {spaces} space(s)"
    )


def main():
    """
    The main function.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument")
    else:
        text_analyzer(sys.argv[1])


if __name__ == '__main__':
    main()
