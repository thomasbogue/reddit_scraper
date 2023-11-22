import praw

import key

def get_reddit():
  return praw.Reddit(
    client_id=key.reddit_secrets["client_id"],
    client_secret=key.reddit_secrets["client_secret"],
    user_agent=key.reddit_secrets["user_agent"]
  )


