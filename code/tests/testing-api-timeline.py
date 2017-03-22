import os
import sys
import pickle
import tweepy

# pylint: disable=C0103
# -*- coding: utf-8 -*-

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

# Authorization and Credentials

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Timeline

twitter_home_timeline = api.home_timeline(count=10)
for home_tweet in twitter_home_timeline:
    tweets_home_timeline = home_tweet.text.encode("utf-8")
    print tweets_home_timeline
    print "------------------------------------------------------------------------"

twitter_user_timeline = api.user_timeline(count=10)
for user_tweet in twitter_user_timeline:
    tweets_user_timeline = user_tweet.text
    print tweets_user_timeline.encode("utf-8")
    print "------------------------------------------------------------------------"

twitter_trends = api.trends_available

# Search

twitter_search = tweepy.Cursor(api.search, q='Madrid').items(10)
#for tweet in twitter_search:
#   print tweet.created_at, tweet.text, tweet.lang


#twitter_home_timeline = api.home_timeline(count=10)
#for home_tweet in twitter_home_timeline:
#    tweets_home_timeline = home_tweet.created_at, home_tweet.text.encode("utf-8"), home_tweet.lang
#    print tweets_home_timeline
#    print "-------------"

#twitter_user_timeline = api.user_timeline(count=10)
#for user_tweet in twitter_user_timeline:
#    tweets_user_timeline = user_tweet.created_at, user_tweet.text.encode("utf-8"), user_tweet.lang
#    print tweets_user_timeline
#    print "-------------"
