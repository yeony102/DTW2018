import tweepy
from fortune import get_horoscope

consumer_key = 'RDvnWA1u8IIMgBXyc7aODKVec'
consumer_secret = '625iD3UlnynJ1voHk3uIRiev2UeUFb4jjxQHiOcvnNLWvaUPWk'
access_token = '929630331191390208-5hLp7gdWlmuFwNWMdxG9sXcINAi8cvS'
access_secret = 'nA3448zoS9gF3RK4WynvxLgQ2y8C470SuZWRdj3hYMqPP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

text = get_horoscope()
# print text
api.update_status(text)
