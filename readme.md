YSRCP Twitter Bot: Twitter bot for YSRCP helping to post new tweets and retweets!
======
YSRCP Twitter Bot is open source program which can be used by any one who wants to help YSRCP to publish new tweets and
retweet the tweets which can help YSRCP.

Installation
------------
Please install below requirements:

1. Install python by following this video link. https://www.youtube.com/watch?v=dX2-V2BocqQ
    install python 2.7 or 3.6 (https://www.python.org/downloads/)
2. After python is installed, pip install
```
    pip install tweepy
```
3. Git repo for YSRCP is https://github.com/pythonforysrc/pythonforysrc.git download the file from this repository
   or git clone to use on your local

4. Create dev account for Twitter and get access_key, access_token, customer_key and customer_access_key. Here is the
   link for the youtube video https://www.youtube.com/watch?v=1p8veF-sIIo.

5. After you get the above keys, navigate to credentials.py and replace the below keys with the corresponding values.
```
    consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    consumer_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token_key='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
```
How to use and run this program?
--------------------------------
In the YSRCPTwitterBot we have two functions(which will increase as we grow)

**YSRCPTwitterBot.postTweets**
For posting new tweets. Please change the text in inside tweet_texts and replace it with your own and run the program. Please include @YSRCP and @YSJagan in every post for more
retweeting. Below is the example of tweet_texts.

```
    tweet_texts=['YSRCP is the only party which is fighting for Special status @YSRCP @YSJagan. Thanks.', 'Only YSRCP can help us get the special status for AP @YSRCP @YSJagan']
    ysrcptwitterbot=YSRCPTwitterBot()
    ysrcptwitterbot.postTweets(tweet_texts)
```

**YSRCPTwitterBot.postRetweets**
For posting retweets of any twitter handler that you interested. It will get the all the recent tweets from that twitter handler and will retweet for you
in the below example, I'm using YSJagan and YSRCParty as they are official twitter handles for YSRCP. You populate the names of the handles and populate in the code snippet.
```
    ysrcptwitterbot=YSRCPTwitterBot()
    twitter_handles_list=['YSJagan','YSRCParty']
    ysrcptwitterbot.postRetweets(tweet_handles_list)
```

Questions on Installation or running the program?
-------------------------------------------------
*Email: pythonforysrc@gmail.com







