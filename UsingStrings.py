'''
As an exercise, add a fourth parameter, end, that specifies where to
stop looking.
'''

def find(str, ch, start = 0, end = -1):
    index = start

    while index < str[end]:
        if str[index] == ch:
            return index
        index += 1
        if index == str[end]:
            return
    return -1


print find("Majemu", "m", 1, 3)

#Not worked yet