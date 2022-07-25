import sys

USAGE = """\
A program that takes a string as argument, reverses it, swaps its letters case
and print the result.
• If more than one argument are provided, they are merged into a single string
with each argument separated by a space character.

Ex:
    $> python3 exec.py 'Hello World!'
    $> !DLROw OLLEh

    $> python3 exec.py 'Hello' 'my Friend'
    $> DNEIRf YM OLLEh$ \
"""


def exec(string: str):
    return string[::-1].swapcase()


def main():
    print(exec(' '.join(sys.argv[1:]))) if len(sys.argv) > 1 else print(USAGE)


if __name__ == "__main__":
    main()
