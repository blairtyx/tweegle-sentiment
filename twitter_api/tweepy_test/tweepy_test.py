import tweepy
import twitter_credentials as tc 


auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKON_SECRET)

api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name = "JoeBiden", count = 10, lang = "en", tweet_mode = "extended")


for tweet in public_tweets:
    print(tweet.full_text + "\n")
    
