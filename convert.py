text = input("What text would you like to be converted?\n")

output = []

def translate_char(char):
    switcher = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    return switcher.get(char, 1)

def convert_text(string):
    string = string.lower()
    for char in string:
        output.append(translate_char(char))
    print(output)

convert_text(text)