import os
import sys
import pickle

# pylint: disable=C0103
# -*- coding: utf-8 -*-

try:
    import tweepy
except ImportError:
    print "-------------------------------------------------"
    print "|    Tweepy method is missing on your system!    |"
    print "|   Install it by using the following command:   |"
    print "|               pip install tweepy               |"
    print "|  Note:Use Admin Rights may be needed to do so  |"
    print "-------------------------------------------------"
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

filename = os.path.basename(__file__)

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    print "-------------------------------------------------"
    print "|                      Hi!                      |"
    print "|     It seems this is your first time here!    |"
    print "|  To use this program, there is a requirement  |"
    print "-------------------------------------------------"
    pause()
    clear()
    print "-------------------------------------------------"
    print "|  You need to use your own API credentials     |"
    print "|   Please visit https://apps.twitter.com       |"
    print "| to create an App & get the required details:  |"
    print "|                                               |"
    print "|           - Twitter Consumer Key              |"
    print "|       - Twitter Consumer Secret Key           |"
    print "|          - Twitter Access Token               |"
    print "|        - Twitter Access Token Secret          |"
    print "|                                               |"
    print "|    Note: This will be a one-off exercise!     |"
    print "|If everything works, you will not see me again |"
    print "|                                               |"
    print "|    Once you have all of those details,        |"
    print "|      Please press a key to continue:          |"
    print "-------------------------------------------------"
    print ""
    print "-------------------------------------------------"
    print "|      We will store those keys into a file.    |"
    print "|   This file is 'keys-DO-NOT-COMMIT.txt' and   |"
    print "|  it will be located into the directory where  |"
    print "|           you copied this program...          |"
    print "-------------------------------------------------"
    print ""
    print "-------------------------------------------------"
    print "|                  PLEASE NOTE:                 |"
    print "|      If you share this program, remember:     |"
    print "|DON'T share keys-DO-NOT-COMMIT.txt with anyone!|"
    print "|      Just share  the", filename, "file      |"
    print "-------------------------------------------------"
    print ""
    pause()
    print ""
    print "Okay! Let's do it then!"
    print ""
    consumer_key = raw_input("1 - Enter your Consumer Key: ")
    consumer_secret = raw_input("2 - Enter your Consumer Secret Key: ")
    access_token = raw_input("3 - Enter your Access Token: ")
    access_token_secret = raw_input("4 - Enter your Access Token Secret Key: ")
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