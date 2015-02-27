#!/usr/bin/env python
# encoding: utf-8

import grab
import sqlite3 as lite

def laceStrings(s1, s2):
    assert type(s1) == str and type(s2) == str
    result = ''
    ma = max([s1, s2], key=len)
    mi = min([s1, s2], key=len)
    for i in range(len(mi)):
        result+=s1[i] + s2[i]
    result+=ma[len(mi):]
    return result


def main():
    print laceStrings(323, 'ds')


if __name__ == '__main__':
    main()

