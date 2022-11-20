#!/usr/bin/python3

import tweepy

"""
This script will delete all of the tweets in the specified account.

You will need to get a Twitter secret tokens to use this
script, you can do so here https://developer.twitter.com/en/portal/dashboard

@requirements: Python 3+, Tweepy
author: @chaignc
"""

BEARER_TOKEN = ""

API_KEY = ""
API_SECRET = ""

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

class Bot:

    def connectAPI(self):
        self.client = tweepy.Client(bearer_token=BEARER_TOKEN,
                                    consumer_key=API_KEY, consumer_secret=API_SECRET,
                                    access_token=ACCESS_TOKEN,
                                    access_token_secret=ACCESS_TOKEN_SECRET)
        self.user_id = self.client.get_me().data.id

    def delete_last_10_tweets(self):
        tweets = self.client.get_users_tweets(self.user_id)
        if tweets.data is not None:
            for tweet in tweets.data:
                print(f"[+] deleting tweet {tweet.id} {repr(tweet.text)}")
                self.client.delete_tweet(tweet.id)
        else:
            print("[+] No tweets to delete")

def main():
    bot = Bot()
    bot.connectAPI()
    bot.delete_last_10_tweets()

main()
