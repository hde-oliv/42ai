import sys
from string import punctuation


def filter_words(string: str, punct: int):
    letter_count = 0
    for letter in string:
        if letter not in punctuation:
            letter_count += 1
    if letter_count > punct:
        return string.translate(str.maketrans("", "", punctuation))
    return None


def main():
    if len(sys.argv) != 3:
        print("ERROR")
        return

    string = sys.argv[1]
    punct = sys.argv[2]

    try:
        punct = int(punct)
    except ValueError:
        print("ERROR")
        return

    list_of_words = [filter_words(x, punct) for x in string.split()]
    list_of_words = [x for x in list_of_words if x is not None]
    print(list_of_words)


if __name__ == "__main__":
    main()
