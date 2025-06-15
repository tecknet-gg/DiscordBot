import praw
import requests

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

