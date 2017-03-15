import os, sys

# -*- coding: utf-8 -*-

# from __future__ import absolute_import, print_function

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

if sys.platform == "linux" or sys.platform == "linux2":
    clear = lambda: os.system('clear')
    pause = lambda: os.system('read -p "$*"')
elif sys.platform == "darwin":
    clear = lambda: os.system('clear')
    pause = lambda: os.system('read -p "$*"')
elif sys.platform == "win32":
    clear = lambda: os.system('cls')
    pause = lambda: os.system("pause")

clear()

print "---------------------------------------------"
print "|                 Public Log                |"
print "|                 ----------                |"
print "|              Date: 2017-03-15             |"
print "|          Code is not completed yet        |"
print "|   Code is Windows, OSX and Linux Ready    |"
print "|     Storing Twitter keys is now ready     |"
print "| When bringing keys back, although working |"
print "|somehow values are not being recognized by |"
print "|  the tweepy credentials part of the code  |"
print "---------------------------------------------"

pause()
clear()

print "---------------------------------------------"
print "|  You need to use your own API credentials |"
print "|   Please visit https://apps.twitter.com   |"
print "| to create an App & gain required details: |"
print "|                                           |"
print "|           - Twitter Consumer Key          |"
print "|       - Twitter Consumer Secret Key       |"
print "|          - Twitter Access Token           |"
print "|        - Twitter Access Token Secret      |"
print "|                                           |"
print "|    Once you have all of those details,    |"
print "|      Please press a key to continue:      |"
print "---------------------------------------------"

pause()
clear()

filename =  os.path.basename(__file__) # Identify the name of the file

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt") # Check if keys file exists.

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
    pause()
    print ""
    print "Let's go then"
    print ""
    credentials = open("keys-DO-NOT-COMMIT.txt", "w")
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
    credentials = open("keys-DO-NOT-COMMIT.txt", "r") # Open keys.txt in Read Mode and
    for line in credentials: # run a loop into the content of the file
        keylist.append(line) # add each value stored @ keys.txt into the keylist
    consumer_key = str(keylist[0]) # assign 1st value in keylist to this variable
    consumer_secret = str(keylist[1]) # assign 2nd value in keylist to this variable
    access_token = str(keylist[2]) # assign 3rd value in keylist to this variable
    access_token_secret = str(keylist[3]) # assign 4th value in keylist to this variable
    credentials.close() # Close the file (it's no longer needed)

# Let's then request the different Twitter API keys required to run the code

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()
print user