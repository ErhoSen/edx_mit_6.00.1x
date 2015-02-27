import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    word_list = []
    for ch in secretWord:
        if not(ch in word_list):
            word_list.append(ch)
    for ch in lettersGuessed:
        if ch in word_list:
            word_list.remove(ch)

        if len(word_list) == 0:
            return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    word_list = []
    empty_list = []
    result = ''
    for elem in secretWord:
        word_list.append(elem)
        empty_list.append('_ ')
    for ch in lettersGuessed:
        if ch in word_list:
            if word_list.count(ch) > 1:
                while word_list.count(ch) != 0:
                    empty_list[word_list.index(ch)] = ch
                    word_list[word_list.index(ch)] = '_ '
            else:
                empty_list[word_list.index(ch)] = ch
    for ch in empty_list:
        result += ch
    return result

def getAvailableLetters(lettersGuessed):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in lettersGuessed:
        alphabet.remove(letter)
    result = ''
    for elem in alphabet:
        result+=elem
    return result

def devide():
    print '-'*13

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(secretWord),"letters long."
    while guesses > 0:
        devide()
        print 'You have', guesses,'guesses left.'
        print "Available letters:", getAvailableLetters(lettersGuessed)
        letter = raw_input('Please guess a letter: ').lower()
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
            continue
        lettersGuessed.append(letter)
        if letter in secretWord:
            print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed):
                devide()
                print 'Congratulations, you won!'
                break
        else:
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
            guesses-=1
    else:
        devide()
        print "Sorry, you ran out of guesses. The word was else."

hangman('tact')