import requests
import sys
import os

# import the creds that are not being pushed to github
sys.path.insert(1, '../..')
import creds


# the api page, where everything is html showing json
r = requests.get(f'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-6-10&to=2022-6-12&sortBy=popularity&language=en&apiKey={creds.api_key}')
content = r.json()

# content is converted to json. we look for the article dictionary, then
# the first article, and then just the title
print(content['articles'][0]['title'])
os.system("pyclean . -q")
