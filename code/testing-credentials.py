import os
import tweepy

# pylint: disable=C0103

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    credentials = open("keys-DO-NOT-COMMIT.txt", "w")
    consumerkey = raw_input("Enter your Consumer Key: ")
    consumerkey = (consumerkey) + '\n'
    credentials.write(consumerkey)
    consumersecret = raw_input("Enter your Consumer Secret Key: ")
    consumersecret = (consumersecret) + '\n'
    credentials.write(consumersecret)
    accesstoken = raw_input("Enter your Access Token: ")
    accesstoken = (accesstoken) + '\n'
    credentials.write(accesstoken)
    accesstokensecret = raw_input("Enter your Access Token Secret Key: ")
    accesstokensecret = (accesstokensecret)
    credentials.write(accesstokensecret)
    credentials.close()

else:
    keylist = []
    credentials = open("keys-DO-NOT-COMMIT.txt", "r")
    for line in credentials:
        line.split()
        keylist.append(line)
    consumerkey = (keylist[0])
    consumersecret = (keylist[1])
    accesstoken = (keylist[2])
    accesstokensecret = (keylist[3])
    credentials.close()

print "Consumer Key =", consumerkey
print "Consumer Secret =", consumersecret
print "Access Token =", accesstoken
print "access Token Secret =", accesstokensecret

print "Hello World"
print "Hello World"

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)

api = tweepy.API(auth)

print api.me().name

# keylist = []
# credentials = open("keys-DO-NOT-COMMIT.txt", "r")
#
#for line in credentials:
#    keylist.append(line)
#credentials.close()
