import json
import praw
import requests
 
subr = 'pythonprogramtrials'
credentials = 'client_secrets.json'
 
with open(credentials) as f:
    creds = json.load(f)
 
reddit = praw.Reddit(client_id=creds['reddit_app_id'],
                     client_secret=creds['reddit_app_secret'],
                     user_agent=creds['user_agent'],
                     redirect_url=creds['redirect_url'],
                     refresh_token=creds['refresh_token'])
 
subreddit = reddit.subreddit(subr)
 
title = 'Just Made My first Post on Reddit Using Python.'
selftext = '''
I am learning how to use the Reddit API with Python using the PRAW wrapper.
By following the tutorial on https://www.jcchouinard.com/post-on-reddit-with-python-praw/
This post was uploaded from my Python Script
'''
reddit.validate_on_submit = True
subreddit.submit(title,selftext=selftext)