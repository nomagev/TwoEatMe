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
print "            Twitter consumer Key             "
print "        Twitter consumer secret Key          "
print "         Your Twitter accesstoken            "
print "      And your Twitter accesstokensecret     "
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

# Let's then request the different Twitter API keys required to run the experiment

consumerkey = raw_input("Enter your Consumer Key: ")
consumersecret = raw_input("Enter your Consumer Secret Key: ")
accesstoken = raw_input("Enter your Access Token: ")
accesstokensecret = raw_input("Enter your Access Token Secret Key: ")

# The next step is to create a file to store the Twitter key.

credentials = open("keys.txt", "w")
credentials(len)

if credentials(len) == 0:
    credentials.write(consumerkey,)
    credentials.write(consumersecret,)
    credentials.write(accesstoken,)
    credentials.write(accesstokensecret,)
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
