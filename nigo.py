a = [1,5,6,7,10,100]


def dum():
    for _ in a:
        print('dumbass') #cost c1 milliseconds


dum()

# c1 are constants
# Let n be the size of the input data.
# Let T(n) be the total cousuming time when we call function 'dum'
# T(1) = c1
# T(n) = c1*n
# T(n)/T(1) = n