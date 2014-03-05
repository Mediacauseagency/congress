### stream_and_shout.py
import sys  
import tweepy 
import json
import re
from tweepy import Stream 
from tweepy.streaming import StreamListener

#opens the dicktionary.txt and sets it to a list
alerts=[]
alerts = [line.strip() for line in open("./yourlist.txt", 'r')]


# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

class listener(StreamListener):

	#Check tweet text against the dictionary and retweet if a match is made (while preventing crash for self retweets)		
		if tweet.has_key("text") and tweet.has_key("id"):
			if tweet["user"]["screen_name"] in congressFriends: 
				for phrase in dicktionary:
						pattern = re.compile(r'\b' +phrase+ r'\b')
						if re.search(pattern, tweet["text"].lower()):
							print tweet
							api.retweet(tweet["id"])
							return True
	
	
	def on_error(self, status):
		return True

twitterStream = Stream(auth, listener()) 
twitterStream.userstream("with=followings")
