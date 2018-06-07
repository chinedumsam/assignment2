# classes to import 
import tweepy
import pandas
import csv

# Our Twitter app credentials
consumer_key = 'aVkcpSWdXuKNgJieilohqIzy9'
consumer_secret = '3pcc9epFo8zUDSVAl9Sq2tsKgxIESCKnZviewv6O3oBOBI2Fdn'
access_token = '1001168145007173632-HHlCsq2EXXGCACnl6q6eDwuG9i8l6E'
access_token_secret = 'MOJKidLhtprFDa0brCA4nKarFNCKDcpY0mGEDwuafCXvt'

# Authenctication process 

twitterauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
twitterauth.set_access_token(access_token, access_token_secret)

twitterapi = tweepy.API(twitterauth,wait_on_rate_limit=True)
tweetcsvFile = open('tweetextra.csv', 'a')
twittercsvWriter = csv.writer(tweetcsvFile)
for tweet in tweepy.Cursor(twitterapi.search,q="#exam",count=100,
lang="en",
since="2018-01-06").items():
    print (tweet.created_at, tweet.text)
    twittercsvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


