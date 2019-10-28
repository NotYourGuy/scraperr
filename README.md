<h1 align="center">Welcome to scraperr 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/NotYourGuy/scraperr/blob/master/LICENSE" target="_blank">
    <img alt="License: GNU General Public License v3.0" src="https://img.shields.io/badge/License-GNU General Public License v3.0-yellow.svg" />
  </a>
</p>

> Subreddit image scraper made in Python

### 🏠 [Homepage](https://git.io/Jeun2)

## Pre-requisites
PRAW (https://praw.readthedocs.io/en/latest/) is required for this script to run. To install it:
```sh 
$ pip3 install praw
```
Also, inside the script you need to modify the access lines (as described [here](http://www.storybench.org/how-to-scrape-reddit-with-python/))
```sh
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME',
                     username='YOUR_USERNAME',
                     password='YOUR_PASSWORD')
```

## Usage

```sh
$ python3 scrapper.py

usage: scrapper.py [-h] [-l LIMIT] [-p PERIOD] subreddit

positional arguments:
  subreddit             The subreddit from which you wish to download the
                        pictures

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        Limit the number of posts to download (default: 10)
  -p PERIOD, --period PERIOD
                        The period from when to download the pictures
                        (default: day) -- options: day, month, year, all
```

## Author

👤 **Lucian Vasile**

* Github: [@NotYourGuy](https://github.com/NotYourGuy)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/NotYourGuy/scraperr/issues).

## Show your support

Give a ⭐️ if this project helped you!

<a href="https://www.patreon.com/NotYourGuy">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2019 [Lucian Vasile](https://github.com/NotYourGuy).<br />
This project is [GNU General Public License v3.0](https://github.com/NotYourGuy/scraperr/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
