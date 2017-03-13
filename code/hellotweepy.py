# The following is an extract from "Hello Tweepy" example
# provided by https://github.com/tweepy/tweepy repository
# (see https://github.com/tweepy/tweepy/blob/master/docs/getting_started.rst)
# for full reference

# -*- coding: utf-8 -*-

# Check https://github.com/nomagev/nomagev-twtt/blob/master/README.md
# for pre-requisits to run this code.

# Import tweepy library.
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

os.system("pause") # Pause the Program

clear() # We clear the screen again

# Next step: validate whether keys.txt file exists.
# keys.txt: file where Twitter Credentials will be stored.
# Why do that?, program can be distributed without the keys in it.

fileexists = os.path.exists("keys.txt")

# We then create a decision-making tree based on keys.txt existing or not.

if fileexists is False: # If Keys.txt does not exists, create it and store values.
    credentials = open("keys.txt", "w")
    consumerkey = raw_input("Enter your Consumer Key: ")
    consumerkey = str(consumerkey) + '\n'
    credentials.write(consumerkey)
    consumersecret = raw_input("Enter your Consumer Secret Key: ")
    consumersecret = str(consumersecret) + '\n'
    credentials.write(consumersecret)
    accesstoken = raw_input("Enter your Access Token: ")
    accesstoken = str(accesstoken) + '\n'
    credentials.write(accesstoken)
    accesstokensecret = raw_input("Enter your Access Token Secret Key: ")
    accesstokensecret = str(accesstokensecret) + '\n'
    credentials.write(accesstokensecret)
    credentials.close()

else:
    keylist = [] # Let's create a list to store the values contained in keys.txt
    credentials = open("keys.txt", "r") # Open keys.txt in Read Mode and
    for line in credentials: # run a loop into the content of the file
        keylist.append(line) # add each value into keys.txt into the keylist
    consumerkey = str(keylist[0]) # assign 1st value in list to this variable
    consumersecret = str(keylist[1]) # assign 2nd value in list to this variable
    accesstoken = str(keylist[2]) # assign 3rd value in list to this variable
    accesstokensecret = str(keylist[3]) # assign 4th value in list to this variable
    credentials.close() # Close the file (it's no longer needed)

# For the purpose of testing, I will display the content of the variables

print consumerkey
print consumersecret
print accesstoken
print accesstokensecret

# Let's then request the different Twitter API keys required to run the code

#authentication = tweepy.OAuthHandler(consumerkey, consumersecret)
#authentication.set_access_token(accesstoken, accesstokensecret)

#twitteraccess = tweepy.API(authentication)

#public_tweets = twitteraccess.home_timeline()
#for tweet in public_tweets:
#    print tweet.text
