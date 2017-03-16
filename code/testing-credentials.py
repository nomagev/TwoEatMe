import os, sys, tweepy

fileexists = os.path.exists("keys-DO-NOT-COMMIT.txt")

if fileexists is False:
    credentials = open("keys-DO-NOT-COMMIT.txt", "w")
    consumer_key = raw_input("Enter your Consumer Key: ")
    consumer_key = str(consumer_key) + '\n'
    credentials.write(consumer_key)
    consumer_secret = raw_input("Enter your Consumer Secret Key: ")
    consumer_secret = str(consumer_secret) + '\n'
    credentials.write(consumer_secret)
    access_token = raw_input("Enter your Access Token: ")
    access_token = str(access_token) + '\n'
    credentials.write(access_token)
    access_token_secret = raw_input("Enter your Access Token Secret Key: ")
    access_token_secret = str(access_token_secret) + '\n'
    credentials.write(access_token_secret)
    credentials.close()

else:
    keylist = [] # Let's create a list to store the values contained in keys.txt
    credentials = open("keys-DO-NOT-COMMIT.txt", "r") # Open keys.txt in Read Mode and
    for line in credentials: # run a loop into the content of the file
        keylist.append(line) # add each value stored @ keys.txt into the keylist
    consumer_key = str(keylist[0]) # assign 1st value in keylist to this variable
    consumer_secret = str(keylist[1]) # assign 2nd value in keylist to this variable
    access_token = str(keylist[2]) # assign 3rd value in keylist to this variable
    access_token_secret = str(keylist[3]) # assign 4th value in keylist to this variable
    credentials.close() # Close the file (it's no longer needed)

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
