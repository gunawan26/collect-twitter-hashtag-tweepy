import tweepy
import json


consumer_key = "MF9HGJHix7aH40oel8O9zbc7k"
consumer_secret = "Rd97ibI3rtXTAeyQOqpnVhIWNnCJknRF5wifLw7aoFDY9O586a"
access_token ="1222006003-KZffuFWbvIZvMFYuNQDGvAQyqdo3UmPVue2bmmQ"
access_token_secret = "97GvmsPUzASgkLDEAhzhIf6nholUc3JpiYEUre8nXjj4t"

searching_variable = "#oppo"
jumlah_data = 100


def connectData(ArgsConsKey,ArgsConsSecret,ArgsToken,ArgsTokenSecret):
    auth = tweepy.OAuthHandler(ArgsConsKey,ArgsConsSecret)
    auth.set_access_token(ArgsToken,ArgsTokenSecret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    return api

def getData(ArgsApi):
    x = []
    count = 0

    for status in tweepy.Cursor(ArgsApi.search,q=searching_variable,geocode="-6.16920,106.82526,1000km" ).items(jumlah_data):

        # x.update(status._json)
        print(status._json)
        x.append(status._json)
        count+=1
        print(count)




    with open(searching_variable+'.json', 'a') as f:
        json.dump(x, f,indent=2)




def main():

    myApi = connectData(consumer_key,consumer_secret,access_token,access_token_secret)
    getData(myApi)
    pass


if __name__ == "__main__":
    main()