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
print "|                 Public Log                |"
print "|                 ----------                |"
print "|              Date: 2017-03-14             |"
print "|          Code is not completed yet        |"
print "|        Code is Windows Ready Only         |"
print "|     Storing Twitter keys is now ready     |"
print "|Working on tweepy code to make it work now |"
#print "|  You need to use your own API credentials |"
#print "|   Please visit https://apps.twitter.com   |"
#print "| to create an App & gain required details  |"
print "---------------------------------------------"
print ""
#print "---------------------------------------------"
#print "|      To use this tool, we will need:      |"
#print "|           - Twitter Consumer Key          |"
#print "|       - Twitter Consumer Secret Key       |"
#print "|          - Twitter Access Token           |"
#print "|        - Twitter Access Token Secret      |"
#print "---------------------------------------------"
#print ""
#print "---------------------------------------------"
#print "|    Once you have all of those details,    |"
#print "|      Please press a key to continue:      |"
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
    print "-------------------------------------------------"
    print "|     It seems you have no keys stored...       |"
    print "|We are going to write & store your Twitter Keys|"
    print "| so you do no have to worry about it anymore.  |"
    print "-------------------------------------------------"
    print ""
    print "-------------------------------------------------"
    print "|      We will store those keys into a file.    |"
    print "|    This file will be called 'keys.txt' and    |"
    print "|  it will be located into the directory where  |"
    print "|           you copied this program...          |"
    print "-------------------------------------------------"
    print ""
    print "-------------------------------------------------"
    print "|                  PLEASE NOTE:                 |"
    print "|      If you share this program, remember:     |"
    print "|       DO NOT share keys.txt with anyone!      |"
    print "| You only need to share the", filename, "file|"
    print "-------------------------------------------------"
    print ""
    os.system("pause") # Pause the Program
    print ""
    print "Let's go then"
    print ""
    credentials = open("keys.txt", "w")
    consumer_key = raw_input("Enter your Consumer Key: ")
    consumer_key = str(consumer_key) + '\n'
    credentials.write(consumer_key)
    consumer_secret = raw_input("Enter your Consumer Secret Key: ")
    consumer_secret = str(consumer_secret) + '\n'
    credentials.write(consumer_secret)
    access_token = raw_input("Enter your Access Token: ")
    access_token = str(access_token) + '\n'
    credentials.write(access_token)
    access_token_secret = raw_input("Enter your Access Token Secret Key: ")
    access_token_secret = str(access_token_secret) + '\n'
    credentials.write(access_token_secret)
    credentials.close()

else:
    keylist = [] # Let's create a list to store the values contained in keys.txt
    credentials = open("keys.txt", "r") # Open keys.txt in Read Mode and
    for line in credentials: # run a loop into the content of the file
        keylist.append(line) # add each value stored @ keys.txt into the keylist
    consumer_key = str(keylist[0]) # assign 1st value in keylist to this variable
    consumer_secret = str(keylist[1]) # assign 2nd value in keylist to this variable
    access_token = str(keylist[2]) # assign 3rd value in keylist to this variable
    access_token_secret = str(keylist[3]) # assign 4th value in keylist to this variable
    credentials.close() # Close the file (it's no longer needed)

# For testing purposes, I display the content of the variables

print "For testing purposes, I display the content of the variables"
print ""
print "The Stored Consumer Key is", consumer_key
print "The Stored Consumer Secret is", consumer_secret
print "The Stored Access Token is", access_token
print "The Stored Access Token Secret is", access_token_secret

# Let's then request the different Twitter API keys required to run the code

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text