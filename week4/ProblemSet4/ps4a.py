# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    score = 0
    for ch in word:
        score += SCRABBLE_LETTER_VALUES[ch]
    score*=len(word)
    if len(word) == n:
        score+=50
    return score



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    hnd = hand.copy()
    for ch in word:
        if ch in hand:
            hnd[ch] -= 1
            if hnd[ch] == 0:
                hnd.pop(ch, None)
    return hnd



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    hnd = hand.copy()
    if word in wordList:
        for ch in word:
            if ch in hnd:
                hnd[ch]-=1
                if hnd[ch] == 0:
                    hnd.pop(ch, None)
            else:
                return False
    else:
        return False
    return True



#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    handlen = 0
    for elem in hand:
        handlen+=hand[elem]
    return handlen



def playHand(hand, wordList, n):
    temphand = hand.copy()
    total_score = 0
    buf = False
    while len(hand) > 0:
        print 'Current Hand:', displayHand(temphand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            buf = True
            break
        else:
            if not(isValidWord(word,temphand,wordList)):
                print 'Invalid word, please try again.\n'
            else:
                total_score+=getWordScore(word, n)
                print '"'+word+'" earned', getWordScore(word, n), 'points. Total:', total_score, '\n'
                temphand = updateHand(temphand, word)
                if calculateHandlen(temphand) == 0:
                    break
    if buf == True:
        print 'Goodbye! Total score:', total_score, 'points.'
    else:
        print 'Run out of letters. Total score:', total_score, 'points.'

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    hand = {}
    buf = False
    while True:
        mode = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if mode == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            buf = True
        elif mode == 'r':
            if buf == True:
                playHand(hand, wordList, HAND_SIZE)
            else:
                print 'You have not played a hand yet. Please play a new hand first!\n'
        elif mode == 'e':
            break
        else:
            print 'Invalid command.'



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
