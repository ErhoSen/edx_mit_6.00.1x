#!/usr/bin/env python
# encoding: utf-8

import grab
import sqlite3 as lite

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n == 0:
        return True
    elif n < 0:
        return False

    return McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20)

def main():
    print McNuggets(16)


if __name__ == '__main__':
    main()

