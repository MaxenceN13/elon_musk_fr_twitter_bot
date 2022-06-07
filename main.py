import tweepy
import config
import myStreamingClient
import translateDeeplAPI

def getMyClient():
	return tweepy.Client(consumer_key=config.API_KEY,
				 consumer_secret=config.API_SECRET,
				 access_token=config.ACCESS_TOKEN,
				 access_token_secret=config.ACCESS_TOKEN_SECRET)


if __name__ == "__main__":
	print("⭐ Lancement du programme ⭐")

	client = getMyClient()

	def tweetTranslatedText(response):
		print("New Tweet Detected !")
		translated_text = translateDeeplAPI.translate(response.data.text)
		client.create_tweet(text=translated_text, quote_tweet_id=response.data.id, user_auth=1)
		print(f"Original tweet : {response.data}\nTweet published : {translated_text}")
	
	streaming_client = myStreamingClient.myStreamingClient(config.BEARER_TOKEN, tweetTranslatedText)

	print("Waiting for tweet... 🦻")

	streaming_client.filter()
						
	print("Fin du programme!")