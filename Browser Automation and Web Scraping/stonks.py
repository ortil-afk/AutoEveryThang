# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests
from datetime import datetime
import time

# take input from a user for when they want the data
ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

# convert to human readable date time
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

# convert the time to epoch
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

#download link for all the stonks
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

#make us look like a computer and not a bot
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# make the request
content = requests.get(url, headers=headers).content
print(content)

# save data to a file. wb provides binary and non-binary
with open('data.csv', 'wb') as file:
  file.write(content)
