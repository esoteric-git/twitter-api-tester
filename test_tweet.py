import tweepy

# OAuth 1.0a credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
# Authenticate
client = tweepy.Client(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

# Post a tweet
tweet_text = "Testing Twitter API v2 Oauth1.0 with Tweepy!"
try:
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted successfully. Tweet ID: {response.data['id']}")
except tweepy.TweepyException as e:
    print(f"An error occurred: {e}")