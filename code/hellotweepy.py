# The following is an extract from "Hello Tweepy" example
# provided by https://github.com/tweepy/tweepy repository
# (see https://github.com/tweepy/tweepy/blob/master/docs/getting_started.rst)
# for full reference

# -*- coding: utf-8 -*-

# Import tweepy library.
# Check https://github.com/nomagev/nomagev-twtt/blob/master/README.md
# for pre-requisits to run this code.
# We will also import the os library, to do some os related operations while running the code.
import tweepy
import os

# Let's first clean the screen running a cls instruction
clear = lambda: os.system('cls')
clear()

# Let's display a first disclaimer
# We indicate the required things needed to execute the program
print "---------------------------------------------"
print "            This is a first test             "
print "   You need to use your own API credentials  "
print "    Please visit https://apps.twitter.com    "
print "to create an App and gain the related details"
print "---------------------------------------------"
print ""
print "---------------------------------------------"
print "Please make sure you have the available info:"
print "            Twitter Consumer Key             "
print "        Twitter Consumer Secret Key          "
print "         Your Twitter Access Token           "
print "       your Twitter Access Token Secret      "
print "---------------------------------------------"
print ""
print "---------------------------------------------"
print "     Once you have all of those details,     "
print "       Please press a key to continue:       "
print "---------------------------------------------"

# Pause the Program
os.system("pause")

# We clear the screen again
clear()

# The next step is to validate whethere keys.txt file exists.
# keys.txt is the file where we will store the Twitter Credentials.

credentials = open("keys.txt", "r")
filesize = os.path.getsize("keys.txt")
credentials.close()

if filesize = "0":
    credentials = open("keys.txt", "r")
    consumerkey = raw_input("Enter your Consumer Key: ")
    consumerkey = str(consumerkey)
    credentials.write(consumerkey)
    consumersecret = raw_input("Enter your Consumer Secret Key: ")
    consumersecret = str(consumersecret)
    credentials.write(consumersecret)
    accesstoken = raw_input("Enter your Access Token: ")
    accesstoken = str(accesstoken)
    credentials.write(accesstoken)
    accesstokensecret = raw_input("Enter your Access Token Secret Key: ")
    accesstokensecret = str(accesstokensecret)
    credentials.write(accesstokensecret)
    credentials.close()
else:
    credentials = open("keys.txt", "r")
    print credentials.readline(0)
    print credentials.readline(1)
    print credentials.readline(2)
    print credentials.readline(3)

# Let's then request the different Twitter API keys required to run the code
authentication = tweepy.OAuthHandler(consumerkey, consumersecret)
authentication.set_access_token(accesstoken, accesstokensecret)

twitteraccess = tweepy.API(authentication)

public_tweets = twitteraccess.home_timeline()
for tweet in public_tweets:
    print tweet.text
