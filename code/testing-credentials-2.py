import os
import tweepy
import pickle

# pylint: disable=C0103

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    consumerkey = raw_input("Enter your Consumer Key: ")
    consumersecret = raw_input("Enter your Consumer Secret Key: ")
    accesstoken = raw_input("Enter your Access Token: ")
    accesstokensecret = raw_input("Enter your Access Token Secret Key: ")
    keylist = [consumerkey, consumersecret, accesstoken, accesstokensecret]
    with open('keys-DO-NOT-COMMIT.txt', "wb") as keyloader:
        pickle.dump(keylist, keyloader)

else:
    with open('keys-DO-NOT-COMMIT.txt', "rb") as keyloader:
        keylist = pickle.load(keyloader)
        consumerkey = keylist[0]
        consumersecret = keylist[1]
        accesstoken = keylist[2]
        accesstokensecret = keylist[3]

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)

api = tweepy.API(auth)

print api.me().name