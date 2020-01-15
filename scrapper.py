#! /usr/bin/python3

import argparse
import os
import sys
import praw
import prawcore
import urllib

# Initialize reddit using your credentials http://www.storybench.org/how-to-scrape-reddit-with-python/
reddit = praw.Reddit("scraperr")

parser = argparse.ArgumentParser()

parser.add_argument('subreddit', help='The subreddit from which you wish to download the pictures', action='store')
parser.add_argument('-l', '--limit', default=10, help='Limit the number of posts to download (default: 10)', type=int, action='store')
parser.add_argument('-p', '--period', default='day', help='The period from when to download the pictures (default: day) -- options: day, month, year, all', action='store')
parser.add_argument('-d', '--directory', default='reddit-wallpapers/', help='The directory for the pictures to be downloaded into (default: reddit-wallpapers/)', action='store')
parser.add_argument(
    'subreddit', help='The subreddit from which you wish to download the pictures', action='store')
parser.add_argument('-l', '--limit', default=10,
                    help='Limit the number of posts to download (default: 10)', type=int, action='store')
parser.add_argument('-p', '--period', default='day',
                    help='The period from when to download the pictures (default: day) -- options: day, month, year, all', action='store')
parser.add_argument('-d', '--directory', default='reddit-wallpapers/',
                    help='The directory for the pictures to be downloaded into (default: reddit-wallpapers/)', action='store')

args=parser.parse_args()
args = parser.parse_args()


hot_subreddit = reddit.subreddit(args.subreddit).top(args.period, limit=args.limit)
hot_subreddit = reddit.subreddit(args.subreddit).top(
    args.period, limit=args.limit)

try:
    url = [post.url for post in hot_subreddit]
except prawcore.ResponseException:
    print('An error occurred during authorisation. Please check that your Reddit app credentials are set correctly and try again.')
    sys.exit(-1)
except prawcore.OAuthException:
    print('An error occurred during authorisation. Please check that your Reddit account credentials are set correctly and try again.')
    sys.exit(-2)
except prawcore.NotFound:
    print('Failed to find a subreddit called "{}". Please check that the subreddit exists and try again.'.format(args.subreddit))
    sys.exit(-3)

# https://stackoverflow.com/a/3173388

def main():
    download_wallpaper()

def download_wallpaper():
    for value in url:
        name = os.path.basename(value) # taking only the value after '/' from the url as name
        
        os.makedirs(os.path.dirname(args.directory), exist_ok=True) # makes the directory where the photos are saved if it doesn't exist https://stackoverflow.com/a/12517490
        
        filename = os.path.join(args.directory, name) # combine the name and the downloads directory to get the local filename
        
        # makes the directory where the photos are saved if it doesn't exist https://stackoverflow.com/a/12517490
        os.makedirs(os.path.dirname(args.directory), exist_ok=True)
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(value, filename) # if the file doesn't exist, it gets downloaded

download_wallpaper()
if __name__ == "__main__":
    main()
