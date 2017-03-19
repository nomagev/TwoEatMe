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

# This will be the part where we will work on the API interaction.

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
stream = tweepy.StreamListener()

def aboutme():
    print "----------------------- USER -------------------------"
    print "|      User Name:", api.me().name
    print "|Screen Name (@):", api.me().screen_name
    print "|    Description:", api.me().description
    print "|  User Location:", api.me().location
    print "|      Followers:", api.me().followers_count
    print "|      Following:", api.me().friends_count
    print "|    # of Twitts:", api.me().statuses_count
    print "|  Creation Date:", api.me().created_at
    print "|      Time Zone:", api.me().time_zone
    print "|       Language:", api.me().lang
    print "|   Listed Count:", api.me().listed_count
    print "|Verified Phone?:", api.me().needs_phone_verification
    print "------------------------------------------------------"

def aboutmeextended():
    print "------------------ MORE ABOUT USER -------------------"
    print "          Contributors Enabled:", api.me().contributors_enabled
    print "          Uses Default Profile:", api.me().default_profile
    print "    Uses Default Profile Image:", api.me().default_profile_image
    print "                      Entities:", api.me().entities
    print "                     Following:", api.me().following
    print "          # of Twitts favoured:", api.me().favourites_count
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
    print "                   is verified:", api.me().verified
    print "------------------------------------------------------"

# Long format of latest status
# print api.me().status

def currentstatus():
    print "-------------------- LATEST TWEET --------------------"
    print "Twitt Content:", api.me().status.text
    print "    Truncated:", api.me().status.truncated
    print "   Created at:", api.me().status.created_at
    print "  In reply to:", api.me().status.in_reply_to_screen_name
    print "       Source:", api.me().status.source
    print "         Favs:", api.me().status.favorite_count
    print "     Retweets:", api.me().status.retweet_count
    print "        Place:", api.me().status.place
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

def twittertimeline():
    #print api.user_timeline(api.me().screen_name)
    #print api.home_timeline()

aboutme()
print "-------------------------------------"
currentstatus()
print "-------------------------------------"
twittertimeline()

#----------------------------------
# print api.me().hashtags
# print api.me().indices
# print api.me().is_quote_status
# print api.me().is_translation_enabled
# print api.me().is_translator
# print api.me().place
# print api.me().urls
# print api.me().user_mentions
# print api.me().User(follow_request_sent)
#----------------------------------