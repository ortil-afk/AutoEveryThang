import requests
import sys
import os

# import the creds that are not being pushed to github
sys.path.insert(1, '../..')
import creds

def get_news(country, api_key=creds.api_key):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(country='us'))
