import requests
import sys
import os

# import the creds that are not being pushed to github
sys.path.insert(1, '../..')
import creds

def get_news(topic, from_date, to_date, language='en', api_key=creds.api_key):
    # the api page, where everything is html showing json
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()

    # content is converted to json. we look for the article dictionary, then
    # the first article, and then just the title. json is how apis mostly talk
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")

        # # prints title and description
        # print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])

    return results

# print and call the function. set parameters
print(get_news(topic='space', from_date='2022-5-27', to_date='2022-5-28'))

# cleanup
os.system("pyclean ../.. -q")
