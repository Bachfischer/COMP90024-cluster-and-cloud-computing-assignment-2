import tweepy
import json, datetime, csv
import twitter_credentials
import harvester_constants
import gps_conversion


# writes the output from the twitter api to a file
class FileWriter():

    # creates an array of tweets coming in
    def __init__(self, api):
        self.api = api

    def write_tweets(self):

        file_name = 'twitter_data'+(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))+'.csv'
        with open (file_name, 'a+', newline='') as csvFile:
           csvWriter = csv.writer(csvFile)
           print("Opened file named: " + file_name)
           self.write_tweets_to_file(csvWriter)

        print("Finished writing tweets to file")

    # writes the tweets fro the API search to a CSV file
    def write_tweets_to_file(self, csvWriter):
        for tweet in tweepy.Cursor(self.api.search, q= harvester_constants.SEARCH_KEYWORDS, \
        lang = 'en', count=500, tweet_mode='extended', \
        geocode = harvester_constants.MELB_GEOCODE).items():
             tweets_encoded = tweet.full_text.encode('utf-8')
             tweets_decoded = tweets_encoded.decode('utf-8')

             #use json.dumps() instead of the csvWriter

             csvWriter.writerow([datetime.datetime.now().strftime("%Y-%m-%d  %H:%M"), \
             tweet.id, tweets_decoded, tweet.created_at, tweet.geo, \
             tweet.place.name if tweet.place else None, tweet.coordinates, \
             tweet._json["user"]["location"]],)


if __name__ == '__main__':
    # Authentication process
    authenticator = tweepy.OAuthHandler(twitter_credentials.API_KEY, \
    twitter_credentials.API_SECRET_KEY)
    authenticator.set_access_token(twitter_credentials.ACCESS_TOKEN, \
    twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(authenticator)

    file_writer = FileWriter(api)
    print("Writing tweets to file")
    file_writer.write_tweets()
