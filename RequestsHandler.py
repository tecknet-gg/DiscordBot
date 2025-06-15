from random import random

import praw
import requests
import json
import random

def requestHandler(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    joke = joke["value"]
    return joke

def getInsult():
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    insult = requestHandler(url)
    if insult == None:
        print("Error retrieving insult. API failure")
        return None
    insult = insult["insult"]
    return insult

def getMum():
   url = "https://www.yomama-jokes.com/api/v1/jokes/random/"
   joke = requestHandler(url)
   if joke == None:
       print("Error retrieving joke. API failure")
       return None
   joke = joke["joke"]
   return joke

def getDad():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Tecknet"
    }
    joke = requestHandler(url,headers)
    if joke == None:
        print("Error retrieving joke. API failure")
        return None
    joke = joke["joke"]
    return joke

def getRedditLongJoke():
    reddit = initialiseReddit()

    subreddit = reddit.subreddit("Jokes")
    posts = list(subreddit.new(limit=250))
    filtered = [post for post in posts
                if not post.stickied and (post.selftext or post.title)]
    joke = random.choice(filtered)
    jokeTitle = joke.title
    jokeText = joke.selftext
    joke = f"{jokeTitle} {jokeText}"
    print(joke)
    print(len(joke))
    if len(joke) <= 150:
        getRedditLongJoke()
    else:
        return joke

def getRedditJoke(subreddit):
    reddit = initialiseReddit()

    subreddit = reddit.subreddit(subreddit)
    posts = list(subreddit.new(limit=250))
    filtered = [post for post in posts
                if not post.stickied and (post.selftext or post.title)]
    joke = random.choice(filtered)
    jokeTitle = joke.title
    jokeText = joke.selftext
    joke = f"{jokeTitle} {jokeText}"
    print(joke)
    #logic to check usage and prevent repeats (within last 1000)
    #call cache manager to prune size
    return joke

def initialiseReddit():
    with open("apitokens.json", "r") as tokens:
        data = json.load(tokens)

    reddit = praw.Reddit(
        client_id = data["client_id"],
        client_secret = data["client_secret"],
        user_agent = data["user_agent"]
    )
    return reddit


getRedditJoke("dadjokes")
getRedditLongJoke()