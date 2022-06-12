from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def get_driver():
    #setting options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("disable-blink-features=AutomationControlled")

    # start the driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    '''Extract only the temperature from text'''
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()

    #Find and fill in username and password
    driver.find_element(by="id", value="id_username").send_keys("automated") #typing username
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN) #typing password and hitting Enter for us (IMPORTANT)
    time.sleep(1)

    # Click on home link and wait 2 sec
    driver.find_element(by="xpath", value="html/body/nav/div/a").click()
    time.sleep(2)

    # Scrape the temperature value
    text = driver.find_element(by="xpath", value='/html/body/div[1]/div/h1[2]').text
    outext = clean_text(text)

    #write the output to a text file with time and date
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, "w+") as f:
        f.write(str(outext))
        
    #print current url for funsies
    print(driver.current_url)


print(main())
