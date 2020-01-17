#! /usr/bin/python3

import argparse
import os
import sys
import praw
import prawcore
import urllib

# Initialize reddit using your credentials:
# http://www.storybench.org/how-to-scrape-reddit-with-python/
reddit = praw.Reddit("scraperr")

parser = argparse.ArgumentParser()

subredditArgHelp = 'The subreddit from which you wish to download the pictures'
limitArgHelp = 'Limit the number of posts to download (default: 10)'
periodArgHelp = ("The period from when to "
                 "download the pictures (default: day) -- options: day,"
                 " month, year, all")
directoryArgHelp = ('The directory for the pictures'
                    'to be downloaded into (default: reddit-wallpapers/)')

parser.add_argument('subreddit', help=subredditArgHelp, action='store')
parser.add_argument('-l', '--limit', default=10, help=limitArgHelp,
                    type=int, action='store')
parser.add_argument('-p', '--period', default='day', help=periodArgHelp,
                    action='store')
parser.add_argument('-d', '--directory', default='reddit-wallpapers/',
                    help=directoryArgHelp, action='store')

args = parser.parse_args()

hot_subreddit = reddit.subreddit(args.subreddit).top(args.period,
                                                     limit=args.limit)

try:
    url = [post.url for post in hot_subreddit]
except prawcore.ResponseException:
    print('An error occurred during authorisation. Please check that'
          'your Reddit app credentials are set correctly and try again.')
    sys.exit(-1)
except prawcore.OAuthException:
    print('An error occurred during authorisation. Please check that'
          'your Reddit account credentials are set correctly and try again.')
    sys.exit(-2)
except prawcore.NotFound:
    print('Failed to find a subreddit called "{}". Please check that'
          'the subreddit exists and try again.'.format(args.subreddit))
    sys.exit(-3)

# https://stackoverflow.com/a/3173388


def download_wallpaper():
    for value in url:
        name = os.path.basename(value)  # taking only the value after '/' from the url as name # noqa: E501

        os.makedirs(os.path.dirname(args.directory), exist_ok=True)  # makes the directory where the photos are saved if it doesn't exist https://stackoverflow.com/a/12517490 # noqa: E501

        filename = os.path.join(args.directory, name)  # combine the name and the downloads directory to get the local filename # noqa: E501

        # makes the directory where the photos are saved if it doesn't exist https://stackoverflow.com/a/12517490 # noqa: E501
        os.makedirs(os.path.dirname(args.directory), exist_ok=True)
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(value, filename)  # if the file doesn't exist, it gets downloaded # noqa: E501


download_wallpaper()
