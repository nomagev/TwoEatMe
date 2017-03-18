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

# This ones work for yourself, but they give a
# lot of info, so it's better to keep them off
# until we find the # way to work with them.
# print(api.me())
# print(api.me().status)


# These ones retrieve specific data-points from
# the selected user

print "Account has Contributors Enabled:", api.me().contributors_enabled
print "Account Creation Date:", api.me().created_at
print "Account Uses Default Profile:", api.me().default_profile
print "Account Uses Default Profile Image:", api.me().default_profile_image
print "Account Personal Description:", api.me().description
print "Account Entities:", api.me().entities
print "Account # of Twitts favoured:", api.me().favourites_count
print "Account # of Followers:", api.me().followers_count
print "Account is following:", api.me().following
print "Account # of Friends:", api.me().friends_count
print "Account is Geo-enabled:", api.me().geo_enabled
print "Account has extended profile:", api.me().has_extended_profile
print "Account Raw Id:", api.me().id
print "Account Raw Id (Legacy):", api.me().id_str
print "Account Set Language:", api.me().lang
print "Account Listed Count:", api.me().listed_count
print "Account User Location:", api.me().location
print "Account User Name:", api.me().name
print "Account Needs Phone Verification:", api.me().needs_phone_verification
print "Account has notifications enabled:", api.me().notifications
print "Account Profile Background Color:", api.me().profile_background_color
print "Account Profile Background Image URL:", api.me().profile_background_image_url
print "Account Profile Background Image URL (https):", api.me().profile_background_image_url_https
print "Account Profile Uses Background Tile:", api.me().profile_background_tile
print "Account Profile Banner Image URL:", api.me().profile_banner_url
print "Account Profile Image URL:", api.me().profile_image_url
print "Account Profile Image URL (https):", api.me().profile_image_url_https
print "Account Profile Link Color:", api.me().profile_link_color
print "Account Profile Location:", api.me().profile_location
print "Account Profile Sidebar Border Color:", api.me().profile_sidebar_border_color
print "Account Profile Sidebar Fill Color:", api.me().profile_sidebar_fill_color
print "Account Profile Text Color:", api.me().profile_text_color
print "Account Profile Used Background Image:", api.me().profile_use_background_image
print "Account is Protected:", api.me().protected
print "Account Screen Name:", api.me().screen_name
print "Account # of Published Twitts:", api.me().statuses_count
print "Account is suspended:", api.me().suspended
print "Account Time Zone:", api.me().time_zone
print "Account uses Translator Type:", api.me().translator_type
print "Account Profile has a URL:", api.me().url
print "Account UTC Offset (in Seconds):", api.me().utc_offset
print "Account is verified:", api.me().verified

# AttributeError: 'User' object has no attribute 'hashtags'
#----------------------------------
# print(api.me().coordinates)
# print(api.me()._json)
# print(api.me().favorite_count)
# print(api.me().favorited)
# print(api.me().geo)
# print(api.me().hashtags)
# print(api.me().in_reply_to_screen_name)
# print(api.me().in_reply_to_status_id)
# print(api.me().in_reply_to_status_id_str)
# print(api.me().in_reply_to_user_id)
# print(api.me().in_reply_to_user_id_str)
# print(api.me().indices)
# print(api.me().is_quote_status)
# print(api.me().is_translation_enabled)
# print(api.me().is_translator)
# print(api.me().place)
#print(api.me().retweet_count)
#print(api.me().retweeted)
# print(api.me().source)
# print(api.me().source_url)
# print(api.me().text)
# print(api.me().truncated)
# print(api.me().urls)
# print(api.me().user_mentions)
# print(api.me().User(follow_request_sent))
#----------------------------------
# print(api.me()._api)