import tweepy
import json, datetime, csv
import twitter_credentials
import harvester_constants
import gps_conversion


# writes the output from the twitter api to a file
class TwitterHarvester():

    # creates an array of tweets coming in
    def __init__(self, api):
        self.api = api
        self.db = setup_db()

    # writing tweets to the file from the API
    def setup_db(self):
        server = couchdb.Server("http://172.26.132.56:5984")
        server.resource.credentials = ("admin", "data-miner!")
        db = server['twitter']
        return db

    # writes the tweets fro the API search to a CSV file
    def collect_tweets_to_file(self, csvWriter):
        for tweet in tweepy.Cursor(self.api.search, q= harvester_constants.SEARCH_KEYWORDS, \
        lang = 'en', count=500, tweet_mode='extended', \
        geocode = harvester_constants.MELB_GEOCODE).items():
            self.db.save(tweet)


if __name__ == '__main__':
    # Authentication process setup
    authenticator = tweepy.AppAuthHandler(twitter_credentials.API_KEY, \
    twitter_credentials.API_SECRET_KEY)
    api = tweepy.API(authenticator, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # getting tweets from the Twitter API
    harvester = TwitterHarvester(api)
    print("Writing tweets to db")
    file_writer.collect_tweets()
