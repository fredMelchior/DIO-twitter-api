from secrets_1 import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET_TOKEN

import tweepy


BRAZIL_WOE_ID = 23424768

auth = tweepy.OAuth1UserHandler(
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET
)
auth_set_access = (ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)

trends = api.get_place_trends(BRAZIL_WOE_ID)

for t in trends:
    print(t)
