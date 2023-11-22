import pprint
import json

import praw

import my_praw

reddit = my_praw.get_reddit()

subreddit_list_filename = "subreddit_list.json"
try:
  subreddits = json.load(open(subreddit_list_filename, "r"))
except:
  print(f"error loading {subreddit_list_filename}")
  exit(1)
N = 20

texts = []

for subreddit in subreddits:
  print(f"loading r/{subreddit}                                                                ")
  submissions = reddit.subreddit(subreddit).top(limit=N)

  for submission in submissions:
      print(f"loading r/{subreddit}/{submission.title}                              ",end="\r")
      submission.comments.replace_more(limit=2)
      texts.append(submission.selftext)
      for comment in submission.comments.list():
          texts.append(comment.body)

outfile = open("reddit_texts.json", "w")
json.dump(texts, outfile)
outfile.close()
