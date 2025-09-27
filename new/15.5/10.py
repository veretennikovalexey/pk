def shift_word(word):
    shift = len(list(filter(str.isalpha, word)))  # длина без знаков препинания
    result = ""
    for c in word:
        if c.isalpha():
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += c
    return result

text = input()
parts = text.lower().split()
shifted = [shift_word(word) for word in parts]

shifted_text = " ".join(shifted)

shifted2 = ""
i = 0
for c in text:
    if c.isupper():
        shifted2 += shifted_text[i].upper()
    else:
        shifted2 += shifted_text[i]
    i += 1

print(shifted2)


