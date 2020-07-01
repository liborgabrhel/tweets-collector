#!/usr/bin/python3
#
# Author: Libor Gabrhel
# Program Name: Tweets Collector

# Python libraries
import tweepy
import json
import timeit
import os

twitter_settings_file_path = './twitter-settings.json'

# Loads search query parameters from external file
with open('search-query-parameters.json', 'r', encoding='utf8') as search_query_parameters_content:
    search_query_parameters = json.load(search_query_parameters_content)

# Setup process
def setup():
    do_twitter_settings_exist = os.path.isfile(twitter_settings_file_path)

    if do_twitter_settings_exist:
        # Loads twitter settings from external file
        with open(twitter_settings_file_path, 'r', encoding='utf8') as twitter_settings_content:
            twitter_settings = json.load(twitter_settings_content)

        # Return twitter settings
        return twitter_settings
    else:
        api_key = input('Enter your API key: ')
        api_secret_key = input('Enter your API secret key: ')
        access_token = input('Enter your Access token: ')
        access_token_secret = input('Enter your Access token secret: ')

        with open(twitter_settings_file_path, 'w', encoding='utf8') as twitter_settings_file:
            twitter_settings = {
                'api_key': api_key,
                'api_secret_key': api_secret_key,
                'access_token': access_token,
                'access_token_secret': access_token_secret,
            }
            twitter_settings_file.write(json.dumps(twitter_settings))
            print('\nSettings file was successfully created.\n')

        # Return twitter settings
        return twitter_settings

# Main application function
def main():
    twitter_settings = setup()

    auth = tweepy.OAuthHandler(twitter_settings['api_key'], twitter_settings['api_secret_key'])
    auth.set_access_token(twitter_settings['access_token'], twitter_settings['access_token_secret'])
    api = tweepy.API(auth_handler=auth, )

    query_keywords = search_query_parameters['keywords']
    query_from = ('from:' + search_query_parameters['from_user']) if search_query_parameters['from_user'] else ""
    language = search_query_parameters['language']
    since = search_query_parameters['since']
    until = search_query_parameters['until']
    tweets_limit = search_query_parameters['tweets_limit']

    separator = ' '

    filtered_query_parameters= [query_parameter for query_parameter in [query_keywords, query_from] if query_parameter]
    query = separator.join(filtered_query_parameters)

    for status in tweepy.Cursor(api.search, q=query, tweet_mode='extended', lang=language, since=since, until=until).items(tweets_limit):
        file_path = 'collected-tweets/' + str(status.id) + '.txt'
        text = ''

        if hasattr(status, 'retweeted_status'):  # Check if it is a retweet
            text = status.retweeted_status.full_text
        else:
            text = status.full_text

        with open(file_path, 'w', encoding='utf8') as file:
            print('💬 ' + str(status.created_at))
            file.write(text)

# Set execution start time
start_time = timeit.default_timer()

# Runs main application function
main()

# Set execution end time
end_time = timeit.default_timer()

# Show execution time
print('\n✨ Done in ' + str(round(end_time - start_time, 1)) + 's')
