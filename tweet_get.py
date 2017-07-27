# -*- coding: utf-8 -*-
# suggested name: tweepyFlujoArchivo
import time
import tweepy
from tweepy.api import API

# replace 'xxxxxxx' values with your credentials
API_KEY = 'xxxxxxxxx'
API_SECRET = 'xxxxxx'
ACCESS_TOKEN = 'xxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxx'
key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class Stream2File(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 10
        self.output = open('text.txt', 'r+')


    def on_status(self, status):
        print (status.text.encode('utf8'))
        text = (status.text)
        head, sep, tail = text.partition('http')
        self.output.write(head)
        self.output.write("\n")
        self.n = self.n+1
        if self.n < self.m: return True
        else:
            self.output.close()
            #return False
            time.sleep(1)
            self.n = 0
            self.output = open('text.txt', 'r+')


stream = tweepy.streaming.Stream(key, Stream2File())
# replace --------------KEYWORD------------------ with whatever you eant
stream.filter(track=['--------------KEYWORD------------------'], languages=['en'])
