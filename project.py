import tweepy
import json

consumer_key = "MF9HGJHix7aH40oel8O9zbc7k"
consumer_secret = "Rd97ibI3rtXTAeyQOqpnVhIWNnCJknRF5wifLw7aoFDY9O586a"
access_token ="1222006003-KZffuFWbvIZvMFYuNQDGvAQyqdo3UmPVue2bmmQ"
access_token_secret = "97GvmsPUzASgkLDEAhzhIf6nholUc3JpiYEUre8nXjj4t"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
count = 0
File = open("data2.json","a")
File.write("[")
a
for status in tweepy.Cursor(api.search,'#2019gantipresiden').items(1):
    x = status
    list_data = []
    count+=1
    print(count)
    print(json.dumps(x._json))
    newval = x+list_data
    with open('data2.json', 'a') as f:
        json.dump(newval._json, f,indent=2)


File.write("]")

