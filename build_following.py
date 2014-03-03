### build_following.py
import tweepy
import json

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

#Opens the JSON file and calls it as congressPeople
json_file = open('./congressDB/congress.txt')
congressPeople = json.load(json_file)
json_file.close()

#Makes a list of all Congressional Twitter handles, excluding the Veep and removing all the nulls
congressFriends= [] 
for congressPersonFact in congressPeople ['objects']:
	if congressPersonFact ['role_type']=='vicepresident':
		pass
	else:
		congressTwit = congressPersonFact ['person']['twitterid']
		if congressTwit != None: 
			congressFriends.append(congressTwit)

#Making a loop of the congressFriends and creating a friendship via the Tweepy wrapper	
me='mytwitterid'
for congressFriend in congressFriends:
	api.create_friendship(congressFriend)
	except:
		pass


