from YSRCPTwitterBot import YSRCPTwitterBot


ysrcptwitterbot=YSRCPTwitterBot()

'''
********************POST NEW TWEETS*******************
Below is the sample to show how to post the new tweets. Change the text in the tweet_texts and replace it with your own text and run the program again. You can see
the tweets posted.
'''
tweet_texts = ['YSRCP is the only party which is fighting for Special status @YSRCP @YSJagan. Thanks.',
               'Only YSRCP can help us get the special status for AP @YSRCP @YSJagan']

ysrcptwitterbot.postTweets(tweet_texts)

'''
********************RETWEET TWEETS WITH TWITTER HANDLE NAMES*******************
Below is the sample to show how to post the new tweets. Change the text in the tweet_texts and replace it with your own text and run the program again. You can see
the tweets posted.
'''
twitter_handles_list = ['YSJagan', 'YSRCParty']
ysrcptwitterbot.postRetweets(twitter_handles_list)

