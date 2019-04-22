import tweepy
import json
import datetime


consumer_key = "__consumer key__"
consumer_secret = "__consumer secret__"
access_token ="__ acccess token__"
access_token_secret = "__token secret___"

name_var = ""
jumlah_data = 100
x = {}

def connectData(ArgsConsKey,ArgsConsSecret,ArgsToken,ArgsTokenSecret):
    auth = tweepy.OAuthHandler(ArgsConsKey,ArgsConsSecret)
    auth.set_access_token(ArgsToken,ArgsTokenSecret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    return api

def getData(ArgsApi,hashtagArgs):
    global x
    count = 0

    for status in tweepy.Cursor(ArgsApi.search,q=hashtagArgs).items(2):

        # x.update(status._json)
        print(status._json)

        x[hashtagArgs] = status._json

        count+=1
        print(count)



def save_to_json():
    with open(name_var+'.json', 'a+') as f:
        print("create file")
        json.dump(x, f,indent=2)





def main():
    global x
    global  name_var
    myApi = connectData(consumer_key, consumer_secret, access_token, access_token_secret)
    f= open("hashtag.txt","r")

    for i in f:
        x = {}
        tgl_skrng = datetime.datetime.now()
        hashtags = i.split(",")
        judul = hashtags[0]+'%s'%(tgl_skrng.microsecond)
        name_var = judul
        for ht in hashtags:
            print(ht)
            getData(myApi,ht)

        save_to_json()

    pass


if __name__ == "__main__":
    main()
