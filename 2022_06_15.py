"""Task:
Given the mapping a = 1, b = 2, ... z = 26, and an
encoded message, count the number of ways it can be
decoded.

For example, the message '111' would give 3, since it
could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For
example, '001' is not allowed.
"""

def f(x):
    """
    Idea: recursively swipe from left to right and
    distinguish cases to ensure decodability.
    """

    if len(x) <= 1:
        return 1
    if int(x[0])*10+int(x[1]) > 26:
        # first digit must be picked alone, otherwise not decodable
        return f(x[1:])
    elif x[1] == "0":
        # firs= two digits to be picked together
        return f(x[2:])
    else:
        return f(x[1:])+ f(x[2:])

if __name__=="__main__":
    print("Got ", f("111"), ", expected 3")
    print("Got ", f("29111"), ", expected 3")
    print("Got ", f("291110"), ", expected 3")
    print("Got ", f("1234"), ", expected 3")
    print("Got ", f("1212"), ", expected 5")
