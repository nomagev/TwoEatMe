# The following is an extract from "Hello Tweepy" example provided by https://github.com/tweepy/tweepy repository (see https://github.com/tweepy/tweepy/blob/master/docs/getting_started.rst) for full reference

# Import tweepy library. Check https://github.com/nomagev/nomagev-twtt/blob/master/README.md for pre-requisits to run this code.
import tweepy

# Import time library. This will allow us to do time related operations while running the code.
import time

# Import os library. This will allow us to do some os related operations while running the code.
import os

# Let's first clean the screen running a cls instruction 
clear = lambda: os.system('cls')
clear()

# Let's display a first disclaimer indicating the required things that will be needed to execute the program
while True:
    print "As this is just a first test, I am preparing the code to use your own API credentials: please check https://apps.twitter.com to create an App and gain the related details"
    print "Please make sure you have available your Twitter consumer_key, consumer_secret_key, your access_token and your access_token_secret API keys provided by your Twitter App"
    print "Once you have all of those details, press a key to continue:"
    # Pause the Program
    os.system("pause")

# We clear the screen again 
clear()

# Let's then request the different Twitter API keys required to run the experiment
consumer_key = raw_input("Enter your Consumer Key: ")
consumer_secret = raw_input("Enter your Consumer Secret Key: ")
access_token = raw_input("Enter your Access Token: ")
access_token_secret = raw_input("Enter your Access Token Secret Key: ")

# Let's then request the different Twitter API keys required to run the code
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
