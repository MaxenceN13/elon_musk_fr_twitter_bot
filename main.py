import tweepy
import config
from translateDeeplAPI import translateDeeplAPI
import time

def getClient():
	return tweepy.Client(consumer_key=config.API_KEY,
			     consumer_secret=config.API_SECRET,
			     access_token=config.ACCESS_TOKEN,
			     access_token_secret=config.ACCESS_TOKEN_SECRET)


client = getClient()

while 1:
	# Get the last tweet of Elon Musk (44196397)
	# 774932906468835329
	lastTweets = client.get_users_tweets("774932906468835329", user_auth=True)

	lastTweetId = ""
	newLastTweetId = str(lastTweets.data[0].id)
	newLastTweetText = lastTweets.data[0].text
	namefile = "lastTweetId.txt"

	# Check if Elon Musk has make a new tweet
	# And save the id tweet in a file
	try:
		with open(namefile, "r") as file:
			lastTweetId = file.read()
	except Exception as e:
		print(f"File '{namefile}' not existing")
	finally:
		if lastTweetId != newLastTweetId:
			print(f"New tweet detected : {newLastTweetId}")
			with open(namefile, "w") as file:
				file.write(newLastTweetId)
				# Tweet the translation of the new tweet
				t = translateDeeplAPI(newLastTweetText)
				print(t)
				response = client.create_tweet(text=t)
			print(response)
		else:
			print("No update !")
	time.sleep(10)
