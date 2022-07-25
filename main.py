from random import betavariate
import tweepy
import config
import myStreamingClient
import deepl

TWITTER_ACCOUNT_ID_TO_MONITOR = "44196397"

def getMyClient():
	return tweepy.Client(consumer_key=config.TWITTER_API_KEY,
				 consumer_secret=config.TWITTER_API_SECRET,
				 access_token=config.TWITTER_ACCESS_TOKEN,
				 access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET)


if __name__ == "__main__":
	print("⭐ Lancement du programme ⭐")

	client = getMyClient()
	translator = deepl.Translator(config.DEEPL_AUTH_KEY)

	# Search informations about twitter account related to id given
	twitter_account_to_monitor = client.get_user(id=TWITTER_ACCOUNT_ID_TO_MONITOR, user_auth=1)
	# Raise exception if no account match with the id
	if not twitter_account_to_monitor.data:
		raise Exception(f"The identifier {TWITTER_ACCOUNT_ID_TO_MONITOR} does not correspond to any twitter account !")

	def tweetTranslatedText(response):
		print(f"New Tweet Detected !\nOriginal tweet : {response.data}")

		# Get the translation of the tweet
		translated_text = translator.translate_text(response.data.text, source_lang="EN", target_lang="FR").text
		# Create a new tweet with the translated text and quote the tweet translated
		client.create_tweet(text=translated_text, quote_tweet_id=response.data.id, user_auth=1)
		
		print(f"Tweet published : {translated_text}")
	
	streaming_client = myStreamingClient.myStreamingClient(config.TWITTER_BEARER_TOKEN, TWITTER_ACCOUNT_ID_TO_MONITOR, tweetTranslatedText)

	print(f"Waiting for tweet from @{twitter_account_to_monitor.data.username} aka {twitter_account_to_monitor.data.name}... 🦻")

	streaming_client.filter()

	print("Fin du programme !")
