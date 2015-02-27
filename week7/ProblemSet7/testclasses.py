#!/usr/bin/env python
# encoding: utf-8

import grab
import sqlite3 as lite
from string import punctuation

class NewsStory(object):

    def __init__(self, g_guid, g_title, g_subject, g_summary, g_link):
        self.guid = g_guid
        self.title = g_title
        self.subject = g_subject
        self.summary = g_summary
        self.link = g_link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):
        return self.word in text.replace("'", ' ').translate(None, punctuation).lower().split(' ')


class TitleTrigger(WordTrigger):

    def __init__(self, ttrig):
        self.word = ttrig.lower()

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

def main():
    koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
    pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
    soda      = NewsStory('', 'Soft drinks are great', '', '', '')
    pink      = NewsStory('', "Soft's the new pink!", '', '', '')
    football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
    microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
    nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
    caps      = NewsStory('', 'soft things are soft', '', '', '')
#    trig  = TitleTrigger('SOFT')
#    print trig.evaluate(pink)
    print 'New York City' in 'asfdNew York Cityasfdasdfasdf'
    print 'New York City' in "asdfasfdNew York Cityasfdasdfasdf"
    print 'New York City' in "asdfasfdNew York Cityasfdasdfasdf"


if __name__ == '__main__':
    main()

