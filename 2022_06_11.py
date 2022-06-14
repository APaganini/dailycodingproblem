""" Task:

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
"""

def f(x):
    # this solution is a commented version of the one found at
    # https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti

    # STEP 1: if the list doesn't contain 1, return 1.
    # A naive way is to create a list of ones contained in x, and if this list
    # is empty return 1. However, this is not "constant space" (worst case is
    # if x == [1]*len(x). To make it constant space, use iterators. The list is
    # created on-the-fly, and next returns the first entry. If the tuple is
    # empty, it returns 0. This way, if next returns something unequal 0, it
    # returns 1 because we found the value 1 in the list x.
    if not next((x_ for x_ in x if x_==1), 0):
        return 1
    # then, move all entries < 1 to the back of x
    lo = 0
    ii = 0  # index used to swipe through x
    hi = len(x)-1  # index of last postive number in x
    while ii <= hi:
        if x[ii] < 1:  # move entries <1 to the back
            x[ii], x[hi] = x[hi], x[ii]
            hi -= 1  # we have just put a negative number at the back
        else:
            ii += 1

    # swipe through the positive numbers and, for those smaller than hi+1, ensure
    # that the sign of x[abs[x[n]-1] is negative
    for n in range(hi+1):
        y = abs(x[n])
        if 0 < y <= hi + 1 and x[y - 1] > 0:
            x[y - 1] *= -1

    # swipe through x and if you spot a positive number, the missing integer
    # is its index + 1
    return next((i for i, v in enumerate(x[:hi + 1]) if v >= 0), hi+1) + 1



if __name__=="__main__":
    print("Got ", f([3, 4, -1, 1]), " expected 2")
    print("Got ", f([3, 2, 1, 0]), " expected 4")
    print("Got ", f([1, 2, 0]), " expected 3")
    print("Got ", f([]), " expected 1")
    print("Got ", f([2,1,2,2,3]), " expected 4")
    print("Got ", f([0,0,3]), " expected 1")
    print("Got ", f([1,2,3]), " expected 4")
    print("Got ", f([1, 2, 1, 0]) , " expected 3")
    print("Got ", f([3, 4, -1, 1]) , " expected 2")
    print("Got ", f([7, 8, 9, 11, 12]) , " expected 1")
    print("Got ", f([1]) , " expected 2")
    print("Got ", f([]) , " expected 1")
    print("Got ", f([0]) , " expected 1")
    print("Got ", f([2, 1]) , " expected 3")
    print("Got ", f([-1, -2, -3]) , " expected 1")
    print("Got ", f([1, 1]) , " expected 2")
    print("Got ", f([1000, -1]) , " expected 1")
    print("Got ", f([-10, -3, -100, -1000, -239, 1]) , " expected 2")
    print("Got ", f([1, 1]) , " expected 2")

