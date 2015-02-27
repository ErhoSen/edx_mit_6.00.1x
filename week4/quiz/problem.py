#!/usr/bin/env python
# encoding: utf-8


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    assert type(x) == int and type(b) == int
    assert x > 0 and b >= 2
    i = 1
    while b**i <= x:
        print b**i, x
        i+=1
    return i-1


def main():
    print myLog(15, 3)


if __name__ == '__main__':
    main()

