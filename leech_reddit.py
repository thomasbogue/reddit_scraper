import pprint
import json

import praw

import my_praw

reddit = my_praw.get_reddit()

subreddits = [ "jokes" ]
N = 1

texts = []

for subreddit in subreddits:
  submissions = reddit.subreddit(subreddit).top(limit=N)
  for submission in submissions:
      print(submission)
      print(submission.title)
      pprint.pprint(submission.__dict__,indent=4)
      pprint.pprint(vars(submission))
      submission.comments.replace_more(limit=2)
      texts.append(submission.selftext)
      for comment in submission.comments.list():
          pprint.pprint(comment.body)
          texts.append(comment.body)

outfile = open("reddit_texts.json", "w")
json.dump(texts, outfile)
outfile.close()

print(len(texts))
word_counts = {}
for text in texts:
    for splitchar in ",;!?@$#":
        text.replace(splitchar, " ")
    for word in text.lower().split():
        if (len(word) >=2):
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

sorted_word_counts = {k:v for k,v in sorted(word_counts.items(), key=lambda item:item[1])}

for word in sorted_word_counts:
    print(f"{word}: {word_counts[word]}")
