
import tweepy
from pprint import pprint
import json
import networkx as nx
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
graph=nx.DiGraph()

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(2 * 60)


print("Loading followers of me into a List")
followers = []

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    followers.append(follower)

print("Loading people I follow into a list")
friends = []
for friend in limit_handler(tweepy.Cursor(api.friends).items()):
    friends.append(friend)

print "Adding followers relationships..."
for user in followers:
	graph.add_edge(user.name,"arnav")
	
print "Adding following relationships..."
for user in friends:
	graph.add_edge("arnav",user.name)
	
# Save graph
print ""
print "The personal profile was analyzed succesfully."
print ""
print "Saving the file as "+"arnav"+"-personal-network.gexf..."
nx.write_gexf(graph,"arnav"+"-personal-network.gexf")