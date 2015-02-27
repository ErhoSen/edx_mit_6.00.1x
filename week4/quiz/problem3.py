#!/usr/bin/env python
# encoding: utf-8

import grab
import sqlite3 as lite

def laceStringsRecur(s1, s2):
    assert type(s1) == str, type(s2) == str

    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        elif s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:],s2[1:], out + s1[0]+s2[0])

    return helpLaceStrings(s1, s2, '')


def main():
    print laceStringsRecur('abcdlm', 'efghij')


if __name__ == '__main__':
    main()

