import tweepy

keylist = []
credentials = open("keys-DO-NOT-COMMIT.txt", "r")

for line in credentials:
    keylist.append(line)
credentials.close()

auth = tweepy.OAuthHandler(keylist[0], keylist[1])
auth.set_access_token(keylist[2], keylist[3])

api = tweepy.API(auth)

print(api.me().name)