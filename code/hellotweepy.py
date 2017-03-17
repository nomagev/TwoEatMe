import os
import sys
import pickle

# pylint: disable=C0103
# -*- coding: utf-8 -*-

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

filename =  os.path.basename(__file__)

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
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
    consumer_key = raw_input("Enter your Consumer Key: ")
    consumer_secret = raw_input("Enter your Consumer Secret Key: ")
    access_token = raw_input("Enter your Access Token: ")
    access_token_secret = raw_input("Enter your Access Token Secret Key: ")
    keylist = [consumer_key, consumer_secret, access_token, access_token_secret]
    with open('keys-DO-NOT-COMMIT.txt', "wb") as keyloader:
        pickle.dump(keylist, keyloader)

else:
    with open('keys-DO-NOT-COMMIT.txt', "rb") as keyloader:
        keylist = pickle.load(keyloader)
        consumer_key = keylist[0]
        consumer_secret = keylist[1]
        access_token = keylist[2]
        access_token_secret = keylist[3]

# Let's then request the different Twitter API keys required to run the code

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me().name
print user