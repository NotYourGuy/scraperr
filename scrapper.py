#! /usr/bin/python3

import argparse
import os
import praw
import urllib

# Initialize reddit using your credentials http://www.storybench.org/how-to-scrape-reddit-with-python/
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID', 'YOUR_CLIENT_ID'),
                     client_secret=os.getenv('CLIENT_SECRET', 'YOUR_CLIENT_SECRET'),
                     user_agent=os.getenv('USER_AGENT', 'YOUR_APP_NAME'),
                     username=os.getenv('USERNAME', 'YOUR_USERNAME'),
                     password=os.getenv('PASSWORD', 'YOUR_PASSWORD'))

DOWNLOADS_DIR = 'reddit-wallpapers/'


parser = argparse.ArgumentParser()

parser.add_argument('subreddit', help='The subreddit from which you wish to download the pictures', action='store')
parser.add_argument('-l', '--limit', default=10, help='Limit the number of posts to download (default: 10)', type=int, action='store')
parser.add_argument('-p', '--period', default='day', help='The period from when to download the pictures (default: day) -- options: day, month, year, all', action='store')

args=parser.parse_args()


hot_subreddit = reddit.subreddit(args.subreddit).top(args.period, limit=args.limit)

url = [post.url for post in hot_subreddit]

# https://stackoverflow.com/a/3173388
def download_wallpaper():
    for value in url:
        name = os.path.basename(value) # taking only the value after '/' from the url as name
        
        os.makedirs(os.path.dirname(DOWNLOADS_DIR), exist_ok=True) # makes the directory where the photos are saved if it doesn't exist https://stackoverflow.com/a/12517490
        
        filename = os.path.join(DOWNLOADS_DIR, name) # combine the name and the downloads directory to get the local filename
        
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(value, filename) # if the file doesn't exist, it gets downloaded

download_wallpaper()