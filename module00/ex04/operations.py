import sys
from collections import namedtuple


Operations = namedtuple(
    'Operations',
    'Sum Difference Product Quotient Remainder'
)

USAGE = """\
A program that takes two integers A and B as arguments and prints the result
of: sum, difference, product, quotient and remainder.
• If more or less than two argument are provided or if either of the argument
is not an integer, it prints an error message.
• If an operation is impossible, it prints an error message instead of a
numerical result

Ex:
    $> python3 operations.py 3 0
    Sum -> 3
    Difference -> 3
    Product -> 0
    Quotient -> Error: No division by zero.
    Remainder -> Error: No module by zero.\
"""


def do_operations(a: int, b: int):
    results = []
    results.append(a + b)
    results.append(a - b)
    results.append(a * b)
    try:
        results.append(a / b)
    except ZeroDivisionError:
        results.append("Error: No division by zero.")
    try:
        results.append(a % b)
    except ZeroDivisionError:
        results.append("Error: No module by zero.")
    return Operations._make(results)


def print_operations(operations: namedtuple):
    for key, value in operations._asdict().items():
        print(f"{key} -> {value}")


def main():
    if len(sys.argv) == 1:
        print(USAGE)
        return
    try:
        print_operations(do_operations(int(sys.argv[1]), int(sys.argv[2])))
    except ValueError:
        print("AssertionError: invalid arguments")
    except IndexError:
        print("AssertionError: invalid number of arguments")


if __name__ == '__main__':
    main()
