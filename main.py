import tweepy
import time

auth = tweepy.OAuthHandler('--api key buraya--', '--secret api key buraya--')
auth.set_access_token('--access token buraya--', '--secret access token buraya--')

api = tweepy.API(auth)
user = api.me()

# limite takılırsa bekleyeceği süre.
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(10000)


# Kaç tweet beğenilecek. Şuan: 50
for tweet in tweepy.Cursor(api.home_timeline).items(50):
    try:
        limit_handle(tweet.favorite())
    except tweepy.TweepError as e:
        error = True
        print(e.reason)
