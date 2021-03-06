# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:10:09 2017

@author: Abhi-Win10
"""

import tweepy
import csv
import sys
import re
from textblob import TextBlob

consumer_key = "[YOUR_CONSUMER_KEY]"
consumer_secret = "[YOUR_CONSUMER_SECRET]"
access_token = "[YOUR_ACCESS_TOKEN]"
access_token_secret = "[YOUR_ACCESS_TOKEN]_SECRET"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("RedmiNote4")

def csv_tweet(tweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
    #print ('AFTER regex: \n ',tweet,'\n')
    return tweet

for i in public_tweets:
    #print(i.text)
    cleaned_tweet = csv_tweet(i.text)
    analysis = TextBlob(i.text)
    #print analysis.sentiment
    if(analysis.sentiment.polarity>0):
        sentiment = 'POSITIVE'
    elif (analysis.sentiment.polarity==0):
        sentiment = 'NEUTRAL'
    else :
        sentiment = 'NEGATIVE'
    print cleaned_tweet,sentiment
