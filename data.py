data = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "10": "_____"
}


def encode(input_str):
    morse = ""
    for alph in input_str:
        if alph == " ":
            morse += "/"
        else:
            morse += data[alph.upper()] + " "
    return morse


def to_morse(msg):
    for key, value in data.items():
        if msg == value:
            return key


def decode(user_input):
    msg = ""
    for alpha in user_input.split():
        if "/" in alpha:
            for space in alpha.split("/"):
                if space == "":
                    msg += " "
                else:
                    msg += to_morse(space)
        else:
            msg += to_morse(alpha)
    return msg


QUITE = True
while QUITE:
    print("########################################################################")
    user_input = input("Please choose.\n1) Encode \n2) Decode \n3) Quite\n")
    if user_input.upper() == "QUITE":
        print("Thank you for visit")
        QUITE = False
    else:
        msg = input("Input: ")
        if user_input.upper() == "DECODE":
            print(f"Output: {decode(msg)}")
        else:
            print(f"Output: {encode(msg)}")

