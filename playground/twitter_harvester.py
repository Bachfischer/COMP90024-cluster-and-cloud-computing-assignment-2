import tweepy
import json
import twitter_credentials


# This will print out the tweets that it receives
class TweepyStream(tweepy.StreamListener):

    # loads JSON tweet and prints it out
    def on_data(self, data):
        tweet = json.loads(data)
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

    # prints out the error message
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = TweepyStream()

    print('Print tweets:')

    # Authentication process
    authenticator = tweepy.OAuthHandler(twitter_credentials.API_KEY, \
    twitter_credentials.API_SECRET_KEY)

    authenticator.set_access_token(twitter_credentials.ACCESS_TOKEN, \
    twitter_credentials.ACCESS_TOKEN_SECRET)

    # Connect the stream to our listener
    stream = tweepy.Stream(authenticator, listener)
    stream.filter(track=['Climate Change'])
