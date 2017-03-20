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
stream = tweepy.StreamListener()

def aboutme():
    print "----------------------- USER -------------------------"
    print "|   User Name:", api.me().name
    print "| Account (@):", api.me().screen_name
    print "| Description:", api.me().description
    print "|    Location:", api.me().location
    print "|   Followers:", api.me().followers_count
    print "|   Following:", api.me().friends_count
    print "| # of Twitts:", api.me().statuses_count
    print "|    Creation:", api.me().created_at
    print "|   Time Zone:", api.me().time_zone
    print "|    Language:", api.me().lang
    print "|Listed Count:", api.me().listed_count
    print "------------------------------------------------------"

def aboutmeextended():
    print "------------------ MORE ABOUT USER -------------------"
    print "          Contributors Enabled:", api.me().contributors_enabled
    print "          Uses Default Profile:", api.me().default_profile
    print "    Uses Default Profile Image:", api.me().default_profile_image
    print "                      Entities:", api.me().entities
    print "                     Following:", api.me().following
    print "              Twitts favorited:", api.me().favourites_count
    print "                is Geo-enabled:", api.me().geo_enabled
    print "          has extended profile:", api.me().has_extended_profile
    print "                        Raw Id:", api.me().id
    print "               Raw Id (Legacy):", api.me().id_str
    print "         Notifications enabled:", api.me().notifications
    print "      Profile Background Color:", api.me().profile_background_color
    print "        Profile Background URL:", api.me().profile_background_image_url
    print "Profile Background URL (https):", api.me().profile_background_image_url_https
    print "  Profile Uses Background Tile:", api.me().profile_background_tile
    print "      Profile Banner Image URL:", api.me().profile_banner_url
    print "             Profile Image URL:", api.me().profile_image_url
    print "     Profile Image URL (https):", api.me().profile_image_url_https
    print "            Profile Link Color:", api.me().profile_link_color
    print "              Profile Location:", api.me().profile_location
    print "  Profile Sidebar Border Color:", api.me().profile_sidebar_border_color
    print "    Profile Sidebar Fill Color:", api.me().profile_sidebar_fill_color
    print "            Profile Text Color:", api.me().profile_text_color
    print " Profile Used Background Image:", api.me().profile_use_background_image
    print "                     Protected:", api.me().protected
    print "                    Suspended?:", api.me().suspended
    print "          uses Translator Type:", api.me().translator_type
    print "             Profile has a URL:", api.me().url
    print "       UTC Offset (in Seconds):", api.me().utc_offset
    print "               Verified Phone?:", api.me().needs_phone_verification
    print "                   is verified:", api.me().verified
    print "------------------------------------------------------"

def currentstatus():
    print "-------------------- LATEST TWEET --------------------"
    print "|   Status:", api.me().status.text
    print "|Truncated:", api.me().status.truncated
    print "|     Date:", api.me().status.created_at
    print "| Reply to:", api.me().status.in_reply_to_screen_name
    print "|   Source:", api.me().status.source
    print "|     Favs:", api.me().status.favorite_count
    print "| Retweets:", api.me().status.retweet_count
    print "|    Place:", api.me().status.place
    print "------------------------------------------------------"

def currentstatusextended():
    print "-------------- MORE ABOUT LATEST TWEET ---------------"
    print "          Contributor:", api.me().status.contributors
    print "         Quote Status:", api.me().status.is_quote_status
    print "In reply to status Id:", api.me().status.in_reply_to_status_id
    print "            Status Id:", api.me().status.id
    print "                  API:", api.me().status._api
    #print "         status JSON:", api.me().status._json
    print "          Coordinates:", api.me().status.coordinates
    #print "     Status entities:", api.me().status.entities
    print "            Status Id:", api.me().status.id_str
    print "  In reply to user Id:", api.me().status.in_reply_to_user_id
    print "         Twitt is Fav:", api.me().status.favorited
    print "           Source URL:", api.me().status.source_url
    print "      Geolocalization:", api.me().status.geo
    print "  In reply to User Id:", api.me().status.in_reply_to_user_id_str
    print "       Twitt Language:", api.me().status.lang
    print "In reply to Status Id:", api.me().status.in_reply_to_status_id_str
    print "            Retweeted:", api.me().status.retweeted
    print "------------------------------------------------------"

aboutme()
print ""
currentstatus()
print ""
twittertimeline()
