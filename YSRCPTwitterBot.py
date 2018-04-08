import tweepy
from credentials import *

class YSRCPTwitterBot(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
        auth.set_access_token(secret=access_token_secret, key=access_token_key)
        self.api = tweepy.API(auth_handler=auth)

    def postTweets(self,tweet_text_list):
        '''
        :param tweet_text_list:
        :return: None
        This method will post new tweets.
        '''
        tweet_text=tweet_text_list
        for each in tweet_text:
            try:
                if self.api.update_status(status=each):
                    print('Tweet with text '+each +' is posted succesfully.')
            except Exception as e:
                print('Tweeting failed because of this error message '+str(e.message))

    def postRetweets(self,twitter_handles_list):
        '''

        :param twitter_handles_list:
        :return:
         This method will post retweets for the twitter handles provided in the arguments.
        '''
        twitter_handles = twitter_handles_list
        for tweach in twitter_handles:
            for each in self.api.user_timeline(tweach, count=10):
                try:
                    if self.api.retweet(each.id):
                        print('Retweeting is sucessful for the id ' + str(each.id))
                except Exception as e:
                    print 'Retweeting failed for the id ' + str(each.id)
