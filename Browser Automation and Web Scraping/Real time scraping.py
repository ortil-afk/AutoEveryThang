from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):

    # url we want to go and cleaning up the request with text
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text

    # boiling the soup to make it cleaner
    soup = BeautifulSoup(content, 'html.parser')

    # "span" and it's class is the tag.get_text only gives the text with no html
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])   # only displays the number, and turns to float
    return rate

# input any currency you want to check between
current_rate = get_currency('INR', 'USD')
print(current_rate)
