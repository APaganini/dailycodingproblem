"""Task:

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""

def f(x):
    "Note: division is not an option because an entry could be 0."

    # special case
    if len(x)==1:
        return []

    # otherwise
    y = [1]*len(x)
    for ii, x_ in enumerate(x):
        for jj in [kk for kk in range(len(x)) if kk is not ii]:
            y[jj] *= x_
    return y


if __name__=="__main__":
    x = [[1, 2, 3, 4, 5], [3, 2, 1], [], [1,0,-1], [1]]
    y = [[120, 60, 40, 30, 24], [2, 3, 6], [], [0, -1, 0], []]
    for ii in range(len(x)):
        print("With the input  ", x[ii])
        print("this code gives ", f(x[ii]))
        print("and we expected ", y[ii])
        print()

