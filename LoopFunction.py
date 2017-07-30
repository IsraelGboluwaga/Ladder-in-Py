def countdown(n):
        if n==0:
                print 'Blastoff'
        else:
                print n
                countdown(n-1)
n = input('Enter number to start countdown from: ')
countdown(n)
