import os, sys, tweepy

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    credentials = open("keys-DO-NOT-COMMIT.txt", "w")
    consumer_key = raw_input("Enter your Consumer Key: ")
    consumer_key = (consumer_key) + '\n'
    credentials.write(consumer_key),
    consumer_secret = raw_input("Enter your Consumer Secret Key: ")
    consumer_secret = (consumer_secret) + '\n' 
    credentials.write(consumer_secret)
    access_token = raw_input("Enter your Access Token: ")
    access_token = (access_token) + '\n'
    credentials.write(access_token)
    access_token_secret = raw_input("Enter your Access Token Secret Key: ")
    access_token_secret = (access_token_secret)
    credentials.write(access_token_secret)
    credentials.close()

else:
    keylist = []
    credentials = open("keys-DO-NOT-COMMIT.txt", "r")
    for line in credentials:
        line.split
        keylist.append(line)
    consumer_key = (keylist[0])
    consumer_secret = (keylist[1])
    access_token = (keylist[2])
    access_token_secret = (keylist[3])
    credentials.close()

print "Consumer Key =", consumer_key
print "Consumer Secret =", consumer_secret
print "access_token =", access_token
print "access_token_secret =", access_token_secret

print "Hello World"
print "Hello World"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api.me().name)

# keylist = []
# credentials = open("keys-DO-NOT-COMMIT.txt", "r")
#
#for line in credentials:
#    keylist.append(line)
#credentials.close()
