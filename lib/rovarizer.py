import string

def rovarize(text):
    chars = []
    word = ""
    for c in text:
        c_upper = string.upper(c)
        c_lower = string.lower(c)

        if c_lower in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]:
            if c_upper == c:
                chars.append(c_upper + "o" + c_lower)
            else:
                chars.append(c_lower + "o" + c_lower)
        else:
            chars.append(c)

    for i in range(len(chars)):
        word = word + chars[i]
    return word

def derovarize(text):
    enciphered_chars = []
    deciphered_chars = []
    word = ""
    for c in text:
        enciphered_chars.append(c)

    position = 0
    while position < len(enciphered_chars):
        if enciphered_chars[position] == enciphered_chars[position+2] and enciphered_chars[position+1] == "o":
            position += 2
        deciphered_chars.append(enciphered_chars[position])
        position += 1

    for i in range(len(deciphered_chars)):
        word = word + deciphered_chars[i]

    return word

print derovarize(rovarize(text=raw_input("test: ")))


enciphered_chars = [1, 3, 45, 56, 46]
i = 0

