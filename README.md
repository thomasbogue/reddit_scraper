# reddit_scraper
language study

# purpose
This repository includes a set of utilities for downloading a sample of reddit posts and comments for the purposes of language analysis.

# files
* my_praw.py: a library for using praw
* key.py: username and password for reddit credentials
* get_refresh_token: opens up a webpage to authorize reddit credentials with a refresh token
* list_popular_subreddits: lists the N most popular subreddits, outputting to subreddit_list.json
* leech_reddit.py: views the top N posts of the subreddits stored in the subreddit_list.json, outputting the results to reddit_texts.json
* word_counts reads in the reddit_text.json file and counts how often each word appears
