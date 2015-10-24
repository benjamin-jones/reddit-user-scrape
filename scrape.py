import praw
import time
import sys

args = sys.argv

if len(args) != 2:
    print("Usage: <username>)

username = args[1]

r = praw.Reddit(user_agent='python:reddit-user-scrape:v0.1 (by /u/xooxies)')
user = r.get_redditor(username)
comments = user.get_comments(limit=None)
flat_comments = praw.helpers.flatten_tree(comments)

for comment in flat_comments:
    print ("="*len(comment.submission.title))
    print(comment.submission.title.encode('utf-8').strip())
    print("="*len(comment.submission.title))
    print(comment.submission.permalink.encode('utf-8').strip())
    print
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(comment.created)))
    print
    print(comment.body.encode('utf-8').strip())
    print
    time.sleep(1)
