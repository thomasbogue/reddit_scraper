import json
import pprint
import praw
import my_praw

reddit = my_praw.get_reddit()

subreddits = []

for subreddit in reddit.subreddits.popular(limit=10):
    if (subreddit.subreddit_type == "public"):
      subreddits.append(subreddit.display_name)
      print(subreddit.display_name)

outfile = open("subreddit_list.json", "w")
json.dump(subreddits, outfile)
outfile.close()
