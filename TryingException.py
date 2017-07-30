'''
def exist_f(filename):
    try:
        f = open(filename, 'r')
        f.close()
        return True
    except IOError:
        return False
'''

no = input('Pick number: ')
if no != 8:
    print "Alright"
else:
    try:
        raise ValueError, "%s is bad" %no
    except ValueError:
         print "Bad no alert: %s" %no