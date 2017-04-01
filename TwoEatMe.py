'''
TwoEatMe.py  is  a  simple, prompt-based
Python-written program, to  use  Twitter
through  Python's   Tweepy  library  and
Twitter Apps Credentials.
'''

__version__ = "2.0.2"
__author__ = "nomagev"
__maintainer__ = "nomagev"
__license__ = "GPL 2.0"
__email__ = "vegamontesino@msn.com"
__status__ = "Testing"

# ---- TO BE DELETED BEFORE RELEASE ----
# Working Notes: New Menu Reworked.
# All Installation Steps are now normalized
# ---- TO BE DELETED BEFORE RELEASE ----


import sys
import os
import pickle
import subprocess

# -*- coding: utf-8 -*-

try:
    import tweepy
except ImportError:
    print " ---------------------------------------------------- "
    print "|       Tweepy method is missing on your system!     |"
    print "|      Install it by using the following command:    |"
    print "|                  pip install tweepy                |"
    print "|     Note:Use Admin Rights may be needed to do so   |"
    print " ---------------------------------------------------- "
    sys.exit()

if sys.platform == "linux" or sys.platform == "linux2":
    CLEAR = lambda: os.system('clear')
    PAUSE = lambda: os.system('read -p "$*"')
elif sys.platform == "darwin":
    CLEAR = lambda: os.system('clear')
    PAUSE = lambda: os.system('read -p "$*"')
elif sys.platform == "win32":
    CLEAR = lambda: os.system('cls')
    PAUSE = lambda: os.system('pause')

CLEAR()

FILE_NAME = os.path.basename(__file__)

FILE_EXISTS = os.path.exists("keys-DO-NOT-COMMIT.txt")

if FILE_EXISTS is False:
    print " ---------------------------------------------------- "
    print "|             Hi! Welcome to TwoEat.me!              |"
    print "|        It seems this is your first time here!      |"
    print "|     To use this program, we need to work on some   |"
    print "|                  necessary data...                 |"
    print " ---------------------------------------------------- "
    PAUSE()
    CLEAR()
    print " ---------------------------------------------------- "
    print "|    You need to use your own API credentials!       |"
    print "|     Please visit  https://apps.twitter.com         |"
    print "|    to create an App & get the required details:    |"
    print "|                                                    |"
    print "|             -  Twitter Consumer Key                |"
    print "|        -  Twitter Consumer Secret Key              |"
    print "|            -  Twitter Access Token                 |"
    print "|          -  Twitter Access Token Secret            |"
    print "|                                                    |"
    print "|       Note: This will be a one-off exercise!       |"
    print "|   If everything works, you will not see me again   |"
    print "|                                                    |"
    print "|         Once you have all of those details,        |"
    print "|           Please press a key to continue:          |"
    print " ---------------------------------------------------- "
    PAUSE()
    CLEAR()
    print ""
    print " ---------------------------------------------------- "
    print "|        We will store those keys into a file.       |"
    print "|      This file is 'keys-DO-NOT-COMMIT.txt' and     |"
    print "|     it will be located into the directory where    |"
    print "|              you copied this program...            |"
    print " ---------------------------------------------------- "
    print ""
    PAUSE()
    CLEAR()
    print ""
    print "------------------------------------------------------"
    print "|                     PLEASE NOTE:                   |"
    print "|         If you share this program, remember:       |"
    print "|   DON'T share keys-DO-NOT-COMMIT.txt with anyone!  |"
    print "|           Just share the", FILE_NAME, "file          |"
    print "------------------------------------------------------"
    print ""
    PAUSE()
    CLEAR()
    print ""
    print "Okay! Let's do it then!"
    print ""
    CONSUMER_KEY = raw_input("1 - Enter your Consumer Key: ")
    CONSUMER_SECRET = raw_input("2 - Enter your Consumer Secret Key: ")
    ACCESS_TOKEN = raw_input("3 - Enter your Access Token: ")
    ACCESS_TOKEN_SECRET = raw_input("4 - Enter your Access Token Secret Key: ")
    KEYLIST = [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]
    with open('keys-DO-NOT-COMMIT.txt', "wb") as keyloader:
        pickle.dump(KEYLIST, keyloader)
    CLEAR()

else:
    with open('keys-DO-NOT-COMMIT.txt', "rb") as keyloader:
        KEYLIST = pickle.load(keyloader)
        CONSUMER_KEY = KEYLIST[0]
        CONSUMER_SECRET = KEYLIST[1]
        ACCESS_TOKEN = KEYLIST[2]
        ACCESS_TOKEN_SECRET = KEYLIST[3]

def chcp_verification():
    '''
    Triggers an analysis on the console code
    page number via chcp.com prompt command.
    If chcp is set to 65001, program doesn't
    take any action: any other number and it
    will be changed to "65001", keeping  the
    original number for re-establishment.
    '''

    chcp_command = subprocess.Popen("chcp.com", stdout=subprocess.PIPE, shell=True)
    (output, err) = chcp_command.communicate()
    #p_status = chcp_command.wait()

    global chcp_code_original #We make this variable global
    chcp_code_original = output.split()[-1]

    if chcp_code_original == '65001':
        print ""
    else:
        chcp = os.popen('chcp.com 65001')
        chcp.read()

chcp_verification()

def chcp_reset():
    '''
    Triggers  a  reset  to  re-establish the
    original  "chcp table"  in the OS before
    the program changed it to "chcp 65001".
    '''

    chcp_original = "chcp.com " + chcp_code_original
    chcp = os.popen(chcp_original)
    chcp.read()

# Let's then request the different Twitter API keys required to run the code

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(AUTH)
# stream = tweepy.StreamListener()

def about_me():
    '''
    Triggers a  basic  reading on  the  main
    attributes from the logging user.
    '''

    print "-------------------- ABOUT USER ----------------------"
    print "|   User Name:", API.me().name.encode("utf-8")
    print "| Account (@):", API.me().screen_name.encode("utf-8")
    print "| Description:", API.me().description.encode("utf-8")
    print "|    Location:", API.me().location.encode("utf-8")
    print "|   Followers:", API.me().followers_count
    print "|   Following:", API.me().friends_count
    print "| # of Tweets:", API.me().statuses_count
    print "|    Creation:", API.me().created_at
    print "|   Time Zone:", API.me().time_zone.encode("utf-8")
    print "|    Language:", API.me().lang.encode("utf-8")
    print "|Listed Count:", API.me().listed_count
    print "|    Verified:", API.me().verified
    print "------------------------------------------------------"

def about_me_extended():
    '''
    Triggers an extended reading on the rest
    of  attributes, from the  logging  user,
    via Twitter Apps Credentials.
    '''

    print "------------------ ALL ABOUT USER --------------------"
    print "            User Name:", API.me().name.encode("utf-8")
    print "          Account (@):", API.me().screen_name.encode("utf-8")
    print "          Description:", API.me().description.encode("utf-8")
    print "             Location:", API.me().location.encode("utf-8")
    print "            Followers:", API.me().followers_count
    print "            Following:", API.me().friends_count
    print "          # of Tweets:", API.me().statuses_count
    print "             Creation:", API.me().created_at
    print "            Time Zone:", API.me().time_zone.encode("utf-8")
    print "             Language:", API.me().lang.encode("utf-8")
    print "         Listed Count:", API.me().listed_count
    print "             Verified:", API.me().verified
    print "------------------------------------------------------"
    print " Contributors Enabled:", API.me().contributors_enabled
    print "    User Default Prof:", API.me().default_profile
    print "   Uses Default Image:", API.me().default_profile_image
    print "             Entities:", API.me().entities
    print "            Following:", API.me().following
    print "     Tweets favorited:", API.me().favourites_count
    print "       is Geo-enabled:", API.me().geo_enabled
    print "    has extended Prof:", API.me().has_extended_profile
    print "               Raw Id:", API.me().id
    print "      Raw Id (Legacy):", API.me().id_str.encode("utf-8")
    print "Notifications enabled:", API.me().notifications
    print "             BG Color:", API.me().profile_background_color.encode("utf-8")
    print "               BG URL:", API.me().profile_background_image_url.encode("utf-8")
    print "       BG URL (https):", API.me().profile_background_image_url_https.encode("utf-8")
    print "         Uses BG Tile:", API.me().profile_background_tile
    print "     Banner Image URL:", API.me().profile_banner_url.encode("utf-8")
    print "            Image URL:", API.me().profile_image_url.encode("utf-8")
    print "    Image URL (https):", API.me().profile_image_url_https.encode("utf-8")
    print "           Link Color:", API.me().profile_link_color.encode("utf-8")
    print "             Location:", API.me().profile_location
    print " Sidebar Border Color:", API.me().profile_sidebar_border_color.encode("utf-8")
    print "   Sidebar Fill Color:", API.me().profile_sidebar_fill_color.encode("utf-8")
    print "           Text Color:", API.me().profile_text_color.encode("utf-8")
    print "        Used BP Image:", API.me().profile_use_background_image
    print "            Protected:", API.me().protected
    print "           Suspended?:", API.me().suspended
    print "      Translator Type:", API.me().translator_type.encode("utf-8")
    print "    Profile has a URL:", API.me().url
    print " UTC Offset (Seconds):", API.me().utc_offset
    print "      Verified Phone?:", API.me().needs_phone_verification
    print "------------------------------------------------------"

def current_tweet():
    '''
    Triggers a  basic  reading  on  the main
    attributes from  last published tweet by
    the user.
    '''

    print "------------------ YOUR LATEST TWEET -----------------"
    print "|   Status:", API.me().status.text.encode("utf-8")
    print "|Truncated:", API.me().status.truncated
    print "|     Date:", API.me().status.created_at
    print "|  Reply 2:", API.me().status.in_reply_to_screen_name.encode("utf-8")
    print "|   Source:", API.me().status.source.encode("utf-8")
    print "|     Favs:", API.me().status.favorite_count
    print "| Retweets:", API.me().status.retweet_count
    print "|    Place:", API.me().status.place
    print "------------------------------------------------------"

def current_tweet_extended():
    '''
    Triggers a command to set the right  set
    Triggers  an  extended  reading  on  the
    additional  attributes   from  the  last
    published tweet by the user.
    '''

    print "------------ ALL ABOUT YOUR LATEST TWEET -------------"
    print "           Status:", API.me().status.text.encode("utf-8")
    print "        Truncated:", API.me().status.truncated
    print "             Date:", API.me().status.created_at
    print "         Reply to:", API.me().status.in_reply_to_screen_name.encode("utf-8")
    print "           Source:", API.me().status.source.encode("utf-8")
    print "             Favs:", API.me().status.favorite_count
    print "         Retweets:", API.me().status.retweet_count
    print "            Place:", API.me().status.place
    print "------------------------------------------------------"
    print "      Contributor:", API.me().status.contributors
    print "     Quote Status:", API.me().status.is_quote_status
    print "  Reply 2 User Id:", API.me().status.in_reply_to_user_id
    print "Reply 2 Status Id:", API.me().status.in_reply_to_status_id
    print "        Status Id:", API.me().status.id
    #print       status JSON:", API.me().status._json
    print "      Coordinates:", API.me().status.coordinates
    #print   Status entities:", API.me().status.entities
    print "     Tweet is Fav:", API.me().status.favorited
    print "       Source URL:", API.me().status.source_url.encode("utf-8")
    print "  Geolocalization:", API.me().status.geo
    print "   Tweet Language:", API.me().status.lang.encode("utf-8")
    print "        Retweeted:", API.me().status.retweeted
    print "------------------------------------------------------"
    print ""

def last_10_tweets_received():
    '''
    Triggers a quick  reading  over the last
    10 tweets received on the user timeline.
    '''

    twitter_home_timeline = API.home_timeline(count=10)
    for home_tweet in twitter_home_timeline:
        user_id = home_tweet.user.screen_name
        tweet_text = home_tweet.text
        tweet_favorite_count = home_tweet.favorite_count
        print "From: @" + user_id.encode("utf-8"), "------", "Favs:", tweet_favorite_count
        print tweet_text.encode("utf-8")
        print "------------------------------------------------------"
    print ""

def last_10_tweets_sent():
    '''
    Triggers a  quick  reading over the last
    10 tweets sent by the user.
    '''

    twitter_user_timeline = API.user_timeline(count=10)
    for user_tweet in twitter_user_timeline:
        tweets_user_timeline = user_tweet.text
        print tweets_user_timeline.encode("utf-8")
        print "------------------------------------------------------"
    print ""

def trends():
    '''
    Triggers a  search  over Twitter trends.
    '''

    twitter_trends = API.trends_place(1)
    twitter_trend_data = twitter_trends[0]
    twitter_trend = twitter_trend_data['trends']
    for trend in twitter_trend:
        names = trend['name']
        print names.encode('utf-8')
        print "------------------------------------------------------"
    print ""

def send_a_tweet():
    '''
    Triggers the Method to send a tweet.
    '''

    print ""
    write_a_tweet = raw_input("Write your Tweet: ")
    if 2 <= len(write_a_tweet) <= 140:
        API.update_status(write_a_tweet)
        print ""
        print "Your tweet:", write_a_tweet, \
        "- containing", len(write_a_tweet), \
        "characters, has been published."
        print ""
        print ""
    else:
        print ""
        print "Your tweet had", len(write_a_tweet), \
        "characters: please try again"
        print ""
        print ""

def menu_description():
    '''
    Triggers a menu  to  display to the user
    possible options he may want to execute.
    '''

    print ""
    print " -------------- TwoEatMe Main Commands -------------- "
    print "| 'S'  = Send a Tweet   | 'C'  = Check 10 last Tweets|"
    print "| 'T'  = Twitter Trends | 'H'  = Last 10 Tweets Sent |"
    print "|-------------------- About You ---------------------|"
    print "| 'Y'  = About You      | 'L'  = Your Last Tweet     |"
    print "| 'YY' = All about You  | 'LL' = All about Your Tweet|"
    print "|----------------- Program Options ------------------|"
    print "| 'X'  = Clear Screen   | 'Q'  = Quit Program        |"
    print "| 'M'  = Display Menu   |                            |"
    print " ---------------------------------------------------- "
    print ""

def menu_options():
    '''
    Triggers the prompt that will be use to
    Interact with the program.
    '''

    ans = True
    while ans:
        ans = raw_input("What would you like to do? ('M' to Display Menu) ")
        if ans == 'S' or ans == 's':
            print ""
            send_a_tweet()
            menu_options()
        elif ans == 'C' or ans == 'c':
            print ""
            last_10_tweets_received()
            menu_options()
        elif ans == 'T' or ans == 't':
            print ""
            trends()
            menu_options()
        elif ans == 'H' or ans == 'h':
            print ""
            last_10_tweets_sent()
            menu_options()
        elif ans == 'Y' or ans == 'y':
            print "Here are your Basic Twitter Details"
            about_me()
            menu_options()
        elif ans == 'L' or ans == 'l':
            print ""
            current_tweet()
            menu_options()
        elif ans == 'YY' or ans == 'yy':
            print ""
            about_me_extended()
            menu_options()
        elif ans == 'LL' or ans == 'll':
            print ""
            current_tweet_extended()
            menu_options()
        elif ans == 'X' or ans == 'x':
            CLEAR()
            menu_options()
        elif ans == 'Q' or ans == 'q':
            print ""
            chcp_reset()
            sys.exit("Thank you for using me: See you soon!")
        elif ans == 'M' or ans == 'm':
            CLEAR()
            menu_description()
            menu_options()
        else:
            print ""
            print "Wrong Option: Please Try Again"
            menu_options()

menu_description()
menu_options()

# End of Program
