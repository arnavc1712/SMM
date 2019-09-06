import tweepy
from pprint import pprint
import json
import time
consumer_key = "a3viE9zsnehj18AS37qvyGtls"
consumer_secret = "L07cOhvQuNt4W20R3AeSFuXmCiVdcyLfiFbeYlV7gq4m97unz7"
access_token = "724311312-Ynce64galfx3EBK3BMKirvkMhHtYxmImeEIbd0nG"
access_token_secret = "PVOdxleUDq9sfviPACiLydvTMAO8Esjf3PK37OlEk80mA"


# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 


# public_tweets = api.home_timeline()
# # foreach through all tweets pulled
# for tweet in public_tweets:
#    # printing the text stored inside the tweet object
#     pprint(tweet.user._json)


## Pagination

def pagination():
    for friend in limit_handler(tweepy.Cursor(api.friends).items()):
        pprint(friend)


## Limit handler

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

if __name__ == "__main__":
    pagination()