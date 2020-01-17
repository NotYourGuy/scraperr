#! /usr/bin/python3

import argparse
import sys
import praw
import prawcore
import shutil
import subprocess
import os

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


def main():
    # check if wget is installed on the system
    if shutil.which("wget") is None:
        print('wget not found on system')
        sys.exit(-4)
    # check if ripme is in the cwd
    if os.path.isfile(os.path.join(os.getcwd(), "ripme.jar")) is False:
        print('ripme not in working directory')
        sys.exit(-5)
    # check if some form of openjdk is installed
    if shutil.which("java") is None:
        print('java not found on system')
        sys.exit(-6)
    download_urls()


def download_urls():
    for value in url:
        # skip on self posts
        if "www.reddit.com" in value:
            print('reddit selfpost detected, skipping...')
            continue
        # wget on reddit images or imgur
        if "i.redd.it" in value or "i.imgur.com" in value:
            subprocess.call(["wget",
                             value,
                             "--directory-prefix",
                             args.directory])
            continue
        # ripme for everything else
        subprocess.call(["java",
                         "-jar",
                         "ripme.jar",
                         "--ripsdirectory",
                         args.directory,
                         "--url",
                         value])


if __name__ == "__main__":
    main()
