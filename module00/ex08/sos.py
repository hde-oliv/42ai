import sys


MORSE_CODE_LOOKUP ={
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----",
    "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}


def sos(string: str):
    string = string.upper()
    morse_string = ""

    for letter in string:
        try:
            morse_string += MORSE_CODE_LOOKUP[letter] + " "
        except KeyError:
            print("ERROR")
            return

    print(morse_string.strip())


def main():
    if len(sys.argv) == 1:
        return

    string = " ".join(sys.argv[1:])
    sos(string)


if __name__ == "__main__":
    main()
