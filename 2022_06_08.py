""" Task:
Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def f(x, k):
    # this probably counts as n*n/2 passes. Not so sure about
    # solving this in one pass without duplicating values or
    # creating bespoke sets for each entry of x
    for ii, y in enumerate(x):
        for jj in range(ii+1, len(x)):
            if k == y + x[jj]:
                print("Found: ", k, " = ", y, " + ", x[jj])
                return True

    print("Not found. No pairwise sum in ", x, " returns ", k)
    return False

if __name__=="__main__":
    f([10, 15, 3, 7], 17)
    f([10, 15, 3, 8], 17)
    f([], 17)
    from numpy.random import randint as rint
    for ii in range(5):
        f(rint(-20, 20, size=rint(10)), k = rint(-30, 30))
