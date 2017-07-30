def countLetters(strg, ch, start):
    letta = 0
    for char in strg[start:]:
        if char == ch:

            return letta
        letta += 1

name = 'Interogate'
print countLetters(name, 'a', 3)