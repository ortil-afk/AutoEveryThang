from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# browser config to allow the webdriver to run smoothly
def get_driver():
    #setting options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("disable-blink-features=AutomationControlled")

    # start the driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    '''Extract only the temperature from text'''
    output = float(text.split(": ")[1]) # use float for error handling, can also use int
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    aristotle = "/html/body/div[1]/div/h1[1]"
    avg_temp = "/html/body/div[1]/div/h1[2]"
    #element = driver.find_element(by="xpath", value=aristotle) #static data
    element = driver.find_element(by="xpath", value=avg_temp) #dynamic data
    return clean_text(element.text)

print(main())
