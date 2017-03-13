# The following is an extract from "Hello Tweepy" example
# provided by https://github.com/tweepy/tweepy repository
# (see https://github.com/tweepy/tweepy/blob/master/docs/getting_started.rst)
# for full reference

# -*- coding: utf-8 -*-

# Check https://github.com/nomagev/nomagev-twtt/blob/master/README.md
# for pre-requisits to run this code.

# We will start importing the os library.
# This will allow os related operations.
import os

# We will then try to Import tweepy library.
# This will allow Twitter API related operations.
# We will try to call it: if missing, program stops.

try:
    import tweepy
except ImportError:
    print "--------------------------------------------"
    print " Tweepy library is missing on your system!  "
    print " Install it by using the following command: "
    print "             pip install tweepy             "
    print "Note:Use Admin Rights may be needed to do so"
    print "--------------------------------------------"
    os.abort()

# We will try to call it: if missing, program stops.
# Let's first clean the screen running a cls instruction
clear = lambda: os.system('cls')
clear()

# Let's display a first disclaimer
# We indicate the required things needed to execute the program
print "---------------------------------------------"
print "                 2017-03-13                  "
print "           Code is not completed             "
print "       Store Twitter keys is now ready       "
#print "   You need to use your own API credentials  "
#print "    Please visit https://apps.twitter.com    "
#print "to create an App and gain the related details"
print "---------------------------------------------"
#print ""
#print "---------------------------------------------"
#print "Please make sure you have the available info:"
#print "            Twitter Consumer Key             "
#print "        Twitter Consumer Secret Key          "
#print "         Your Twitter Access Token           "
#print "       your Twitter Access Token Secret      "
#print "---------------------------------------------"
#print ""
#print "---------------------------------------------"
#print "     Once you have all of those details,     "
#print "       Please press a key to continue:       "
#print "---------------------------------------------"

os.system("pause") # Pause the Program

clear() # We clear the screen again

# I want to identify the name of the file: it may be useful for users.
filename =  os.path.basename(__file__)

# Next step: validate whether keys.txt file exists.
# keys.txt is the file where Twitter Credentials will be stored.
# Why do that? So program can be distributed without the keys in it.

fileexists = os.path.exists("keys.txt")

# We then create a decision-making tree based on keys.txt existing or not.

if fileexists is False: # If Keys.txt does not exists, create it and store values.
    print "It seems you have no keys stored"
    print "We are going to store your Twitter Keys, so you do no have to worry about it anymore"
    print "We will store those keys into a file called keys.txt in the directory where your program is"
    print "If you share this program, DO NOT share keys.txt with anyone: only the", filename, "file"
    os.system("pause") # Pause the Program
    print "Let's go then"
    print ""
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
        keylist.append(line) # add each value stored @ keys.txt into the keylist
    consumerkey = str(keylist[0]) # assign 1st value in keylist to this variable
    consumersecret = str(keylist[1]) # assign 2nd value in keylist to this variable
    accesstoken = str(keylist[2]) # assign 3rd value in keylist to this variable
    accesstokensecret = str(keylist[3]) # assign 4th value in keylist to this variable
    credentials.close() # Close the file (it's no longer needed)

# For testing purposes, I display the content of the variables

print "For testing purposes, I display the content of the variables"
print ""
print "The Stored Consumer Key is ", consumerkey
print "The Stored Consumer Secret is ", consumersecret
print "The Stored Access Token is ", accesstoken
print "The Stored Access Token Secret is ", accesstokensecret

# Let's then request the different Twitter API keys required to run the code

#authentication = tweepy.OAuthHandler(consumerkey, consumersecret)
#authentication.set_access_token(accesstoken, accesstokensecret)

#twitteraccess = tweepy.API(authentication)

#public_tweets = twitteraccess.home_timeline()
#for tweet in public_tweets:
#    print tweet.text
