''' filterFile makes a copy of oldFile, omitting any lines that begin with # '''
def filterFile(old, new):
    f1 = open(old,'r')
    f2 = open(new,'w')

    while True:
        text = f1.readline()
        if text == '':
            break
        elif text[0] == '#':
            continue
        f2.write(text)

    f1.close()
    f2.close()
    return

file1 = open('fi1.dat','w')
file1.write('This is first line\n')
file1.write('#Line 2\n')
file1.write('Line 3\n')

file1.close()


file2 = 'fil2.dat'

filterFile('fi1.dat', file2)

file2 = open(file2, 'r')
print file2.read()
