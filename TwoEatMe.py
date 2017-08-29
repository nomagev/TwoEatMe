'''
TwoEatMe.py  is  a  simple, prompt-based
Python-written program, to  use  Twitter
through  Python's   Tweepy  library  and
Twitter Apps Credentials.
'''

__version__ = '2.0.1'
__author__ = 'nomagev'
__maintainer__ = "nomagev"
__license__ = "GPL 2.0"
__email__ = "vegamontesino@msn.com"
__status__ = "Production"

import sys
import os
import pickle
import subprocess

# -*- coding: utf-8 -*-

try:
    import tweepy
except ImportError:
    print "-------------------------------------------------"
    print "|    Tweepy method is missing on your system!   |"
    print "|   Install it by using the following command:  |"
    print "|               pip install tweepy              |"
    print "|  Note:Use Admin Rights may be needed to do so |"
    print "-------------------------------------------------"
    sys.exit()

if sys.platform == "linux" or sys.platform == "linux2":
    clear = lambda: os.system('clear')
    pause = lambda: os.system('read -p "$*"')
elif sys.platform == "darwin":
    clear = lambda: os.system('clear')
    pause = lambda: os.system('read -p "$*"')
elif sys.platform == "win32":
    clear = lambda: os.system('cls')
    pause = lambda: os.system('pause')

clear()

filename = os.path.basename(__file__)

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    print "-------------------------------------------------"
    print "|           Hi! Welcome 2 TwoEat.me!            |"
    print "|     It seems this is your first time here!    |"
    print "|    To use this program, we need to work on    |"
    print "|            some necessary data...             |"
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
    print "|      Once you have all of those details,      |"
    print "|        Please press a key to continue:        |"
    print "-------------------------------------------------"
    pause()
    clear()
    print ""
    print "-------------------------------------------------"
    print "|      We will store those keys into a file.    |"
    print "|   This file is 'keys-DO-NOT-COMMIT.txt' and   |"
    print "|  it will be located into the directory where  |"
    print "|           you copied this program...          |"
    print "-------------------------------------------------"
    print ""
    pause()
    clear()
    print ""
    print "-------------------------------------------------"
    print "|                  PLEASE NOTE:                 |"
    print "|      If you share this program, remember:     |"
    print "|DON'T share keys-DO-NOT-COMMIT.txt with anyone!|"
    print "|        Just share the", filename, "file        |"
    print "-------------------------------------------------"
    print ""
    pause()
    clear()
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
    clear()

else:
    with open('keys-DO-NOT-COMMIT.txt', "rb") as keyloader:
        keylist = pickle.load(keyloader)
        consumer_key = keylist[0]
        consumer_secret = keylist[1]
        access_token = keylist[2]
        access_token_secret = keylist[3]

def chcp_verification():
    '''
    Triggers an analysis on the console code
    page number via chcp.com prompt command.
    If chcp is set to 65001, program doesn't
    take any action: any other number and it
    will be changed to "65001", keeping  the
    original number for re-establishment.
    '''

    p = subprocess.Popen("chcp.com", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    global chcp_code_original
    chcp_code_original = output.split()[-1]

    if chcp_code_original == '65001':
        print ""
    else:
        chcp = os.popen('chcp.com 65001')
        chcp.read()

chcp_verification()

def chcp_reset():
    '''
    Triggers an analysis on the console code
    Triggers  a  reset for the required code
    page set to run the program (chcp 65001)
    by using "chcp_code_original" variable.
    '''

    chcp_original = "chcp.com " + chcp_code_original
    chcp = os.popen(chcp_original)
    chcp.read()

# Let's then request the different Twitter API keys required to run the code

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# stream = tweepy.StreamListener()

def about_me():
    '''
    Triggers a  basic  reading on  the  main
    attributes from the logging user.
    '''
    print "Here are your Basic Twitter Details"
    print "----------------------- USER -------------------------"
    print "|   User Name:", api.me().name.encode("utf-8")
    print "| Account (@):", api.me().screen_name.encode("utf-8")
    print "| Description:", api.me().description.encode("utf-8")
    print "|    Location:", api.me().location.encode("utf-8")
    print "|   Followers:", api.me().followers_count
    print "|   Following:", api.me().friends_count
    print "| # of Tweets:", api.me().statuses_count
    print "|    Creation:", api.me().created_at
    print "|   Time Zone:", api.me().time_zone.encode("utf-8")
    print "|    Language:", api.me().lang.encode("utf-8")
    print "|Listed Count:", api.me().listed_count
    print "------------------------------------------------------"

def about_me_extended():
    '''
    Triggers an extended reading on the rest
    of  attributes, from the  logging  user,
    via Twitter Apps Credentials.
    '''

    print "------------------ MORE ABOUT USER -------------------"
    print "     Contributors Enabled:", api.me().contributors_enabled
    print "        User Default Prof:", api.me().default_profile
    print "  Uses Default Prof Image:", api.me().default_profile_image
    print "                 Entities:", api.me().entities
    print "                Following:", api.me().following
    print "         Tweets favorited:", api.me().favourites_count
    print "           is Geo-enabled:", api.me().geo_enabled
    print "        has extended Prof:", api.me().has_extended_profile
    print "                   Raw Id:", api.me().id
    print "          Raw Id (Legacy):", api.me().id_str.encode("utf-8")
    print "    Notifications enabled:", api.me().notifications
    print "            Prof BG Color:", api.me().profile_background_color.encode("utf-8")
    print "              Prof BG URL:", api.me().profile_background_image_url.encode("utf-8")
    print "      Prof BG URL (https):", api.me().profile_background_image_url_https.encode("utf-8")
    print "        Prof Uses BG Tile:", api.me().profile_background_tile
    print "    Prof Banner Image URL:", api.me().profile_banner_url.encode("utf-8")
    print "           Prof Image URL:", api.me().profile_image_url.encode("utf-8")
    print "   Prof Image URL (https):", api.me().profile_image_url_https.encode("utf-8")
    print "          Prof Link Color:", api.me().profile_link_color.encode("utf-8")
    print "            Prof Location:", api.me().profile_location
    print "Prof Sidebar Border Color:", api.me().profile_sidebar_border_color.encode("utf-8")
    print "  Prof Sidebar Fill Color:", api.me().profile_sidebar_fill_color.encode("utf-8")
    print "          Prof Text Color:", api.me().profile_text_color.encode("utf-8")
    print "       Prof Used BP Image:", api.me().profile_use_background_image
    print "                Protected:", api.me().protected
    print "               Suspended?:", api.me().suspended
    print "     uses Translator Type:", api.me().translator_type.encode("utf-8")
    print "           Prof has a URL:", api.me().url
    print "  UTC Offset (in Seconds):", api.me().utc_offset
    print "          Verified Phone?:", api.me().needs_phone_verification
    print "              is verified:", api.me().verified
    print "------------------------------------------------------"

def current_tweet():
    '''
    Triggers a  basic  reading  on  the main
    attributes from  last published tweet by
    the user.
    '''

    print "-------------------- LATEST TWEET --------------------"
    print "|   Status:", api.me().status.text.encode("utf-8")
    print "|Truncated:", api.me().status.truncated
    print "|     Date:", api.me().status.created_at
    print "| Reply to:", api.me().status.in_reply_to_screen_name
    print "|   Source:", api.me().status.source.encode("utf-8")
    print "|     Favs:", api.me().status.favorite_count
    print "| Retweets:", api.me().status.retweet_count
    print "|    Place:", api.me().status.place
    print "------------------------------------------------------"

def current_tweet_extended():
    '''
    Triggers a command to set the right  set
    Triggers  an  extended  reading  on  the
    additional  attributes   from  the  last
    published tweet by the user.
    '''

    print "-------------- MORE ABOUT LATEST TWEET ---------------"
    print "          Contributor:", api.me().status.contributors
    print "         Quote Status:", api.me().status.is_quote_status
    print "In reply to status Id:", api.me().status.in_reply_to_status_id
    print "            Status Id:", api.me().status.id
    #print "         status JSON:", api.me().status._json
    print "          Coordinates:", api.me().status.coordinates
    #print "     Status entities:", api.me().status.entities
    print "            Status Id:", api.me().status.id_str.encode("utf-8")
    print "  In reply to user Id:", api.me().status.in_reply_to_user_id
    print "         Tweet is Fav:", api.me().status.favorited
    print "           Source URL:", api.me().status.source_url.encode("utf-8")
    print "      Geolocalization:", api.me().status.geo
    print "  In reply to User Id:", api.me().status.in_reply_to_user_id_str
    print "       Tweet Language:", api.me().status.lang.encode("utf-8")
    print "In reply to Status Id:", api.me().status.in_reply_to_status_id_str
    print "            Retweeted:", api.me().status.retweeted
    print "------------------------------------------------------"

def last_10_tweets_received():
    '''
    Triggers a quick  reading  over the last
    10 tweets received on the user timeline.
    '''

    twitter_home_timeline = api.home_timeline(count=10)
    for home_tweet in twitter_home_timeline:
        user_id = home_tweet.user.screen_name
        tweet_text = home_tweet.text
        tweet_favorite_count = home_tweet.favorite_count
        print "From: @" + user_id.encode("utf-8"), \
        "------", "Favs:", tweet_favorite_count
        print tweet_text.encode("utf-8")
        print "------------------------------------------------------"

def last_10_tweets_sent():
    '''
    Triggers a  quick  reading over the last
    10 tweets sent by the user.
    '''

    twitter_user_timeline = api.user_timeline(count=10)
    for user_tweet in twitter_user_timeline:
        tweets_user_timeline = user_tweet.text
        print tweets_user_timeline.encode("utf-8")
        print "------------------------------------------------------"

def trends():
    '''
    Triggers a  search  over Twitter trends.
    '''

    twitter_trends = api.trends_place(1)
    twitter_trend_data = twitter_trends[0]
    twitter_trend = twitter_trend_data['trends']
    for trend in twitter_trend:
        names = trend['name']
        print names.encode('utf-8')
        print "------------------------------------------------------"

def send_a_tweet():
    '''
    Triggers the Method to send a tweet.
    '''

    print ""
    write_a_tweet = raw_input("Write your Tweet: ")
    if 2 <= len(write_a_tweet) <= 140:
        api.update_status(write_a_tweet)
        print ""
        print "Your tweet:", write_a_tweet, \
        "- containing", len(write_a_tweet), \
        "characters, has been published."
        print ""
    else:
        print ""
        print "Your tweet had", len(write_a_tweet), \
        "characters: please try again"
        print ""

def menu_description():
    '''
    Triggers a menu to offer to the user the
    possible options he may want to execute.
    '''

    print ""
    print " ---------------- TwoEat   Commands ----------------- "
    print "| 'ST' = Send a Tweet    | 'TT' = Twitter Trends     |"
    print "| 'T'  = Last Tweet Sent | 'T+' = Last Tweet Sent +  |"
    print "| 'R'  = 10 latest Tweets| 'S'  = Your last 10 Tweets|"
    print "|-------------------- About You ---------------------|"
    print "| 'U'  = You @ Twitter   | 'U+' = You @ Twitter ++   |"
    print "|----------------- Program Options ------------------|"
    print "| 'C'  = Clear Screen    | 'Q'  = Quit Program       |"
    print " ---------------------------------------------------- "
    print ""

menu_description()

ans = True
while ans:
    ans = raw_input("What would you like to do? ")
    print ""

    if ans.lower() == 'st':        
        send_a_tweet()
    elif ans.lower() == 'tt':
        trends()
    elif ans.lower() == 't':
        current_tweet()
    elif ans.lower() == 't+':
        current_tweet_extended()
    elif ans.lower() == 'r':
        last_10_tweets_received()
    elif ans.lower() == 's':
        last_10_tweets_sent()
    elif ans.lower() == 'u':
        about_me()
    elif ans.lower() == 'u+':
        about_me_extended()
    elif ans.lower() == 'q':
        chcp_reset()
        sys.exit("See you soon!")
    elif ans.lower() == 'c':
        clear()
    else:
        print "Wrong instruction: please try again"

    menu_description()

# End of Program
