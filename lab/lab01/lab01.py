from typing import AnyStr


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    i=n
    if k == 1:
        return n
    elif k ==0:
        return 1
    else:
        while k > 1:
            i=i*(n-1)
            n=n-1
            k=k-1
    return i


    


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    a=0
    while y > 0:
            x = y % 10
            y = y // 10
            a = a + x
    return a


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    a=0
    while n > 0:
        x = n % 10
        n = n // 10
        if x == 8:
            a += 1
        if x != 8:
            a=0
        if a ==2:
            return True
    return False

double_eights(2882)

