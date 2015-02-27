# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("fable.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    result = {}
    alphabet = string.ascii_lowercase
    for index, ch in enumerate(alphabet):
        result[ch] = alphabet[(index+shift)%len(alphabet)]
        result[ch.upper()] = alphabet[(index+shift)%len(alphabet)].upper()
    return result

def applyCoder(text, coder):
    result = ''
    ignore = string.digits + string.punctuation + ' ' + '\n'
    for ch in text:
        if ch in ignore:
            result+=ch
        else:
            result+=coder[ch]
    return result

def applyShift(text, shift):
    return applyCoder(text, buildCoder(shift))
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    # create local vars
    key = 26
    valid_counter = 0
    max_valid = 0
    result = 0
    # while key > 0
    while key > 0:
        # apply coder for this key
        plaintext = applyShift(text, key)
        # for word in plain text
        for word in plaintext.split(' '):
            # if word is valid
            if isWord(wordList, word):
                # counter + 1
                valid_counter+=1
        if valid_counter > max_valid:
            max_valid = valid_counter
            result = key
        valid_counter = 0
        # decrement key
        key-=1
    return result

def decryptStory():
    bad_story = getStoryString()
    return applyShift(bad_story, findBestShift(loadWords(), bad_story))

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
