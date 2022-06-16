"""Task:

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda x,y: x)

def cdr(pair):
    return pair(lambda x,y: y)

if __name__=="__main__":
    from numpy.random import randint as ri
    for ii in range(6):
        a, b = ri(9), ri(9)
        pair = cons(a, b)
        print("Car(pair) = ", car(pair),
              ", expected ", a ,
              "; cdr(pair) = ", cdr(pair),
              ", expected ", b)
