import pprint
import json

import praw

import my_praw

try:
  text_filename = "reddit_texts.json"
  texts = json.load(open(text_filename, "r"))
except:
  print(f"could not open {text_filename}")
  exit(1)

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

sorted_word_counts = {k:v for k,v in sorted(word_counts.items(), key=lambda item:item[1], reverse=True)}

for word in sorted_word_counts:
    print(f"{word}: {word_counts[word]}")
