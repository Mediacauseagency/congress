### stream_and_shout.py
import sys  
import tweepy 
import json
from tweepy import Stream 
from tweepy.streaming import StreamListener

#opens the dicktionary.txt and sets it to a list
dicktionary=[]
dicktionary = [line.strip() for line in open("./dicktionary.txt", 'r')]


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

	#def on_data(self, data):		
		#print data
		#return True

	def on_data(self, data):		
		tweet=json.loads(data)
		if tweet.has_key("text") and tweet.has_key("id"):
			for phrase in dicktionary:
				if tweet["text"].find(phrase) >=0:
					print tweet["text"]
					api.retweet(tweet["id"])
			#if tweet.has_key('id') and tweet.has_key("text"):
				#print("%s: %s" % (tweet['user']['screen_name'], tweet['text']))
		
		#print badTweet
		#for phrase in dicktionary:
		#	if tweet['text'].find(phrase) >= 0 :
		#		print tweet
		
		#print tweets
	#def on_error(self, status):
		#print status

twitterStream = Stream(auth, listener()) 
twitterStream.userstream("with=followings")
