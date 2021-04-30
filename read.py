#!/usr/bin/python
import praw
import re
import random
import time

reddit = praw.Reddit('albus')

subreddit = reddit.subreddit("cricket")
post = 'n1t70x'
bots = ['CricketMatchBot', 'TheCricBot', 'OwOfier']

for comment in subreddit.stream.comments():
    if comment.author.name not in bots and post in comment.permalink:
        file1 = open("rcb-pbks.txt", "a")
    # 	print(comment)
    # 	print(comment.permalink)
        file1.write(comment.body.encode('utf-8'))
        file1.write("\n")
        file1.close()
