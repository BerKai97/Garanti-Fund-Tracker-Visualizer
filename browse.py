import os
from selenium import webdriver
import time

geckodriver_path = './geckodriver'
os.environ['webdriver.gecko.driver'] = geckodriver_path

driver : webdriver.Firefox = webdriver.Firefox()
driver.get('https://sube.garantibbva.com.tr/isube/login/mobiletokenverifynew')

# xpath = "/html/body/div[2]/header/div[2]/div/div/ul[1]/li[7]/ul/li[2]/ul/li[3]/a"
xpath = "/html/body/div/header/div/div/div[2]/ul[1]/li[2]/a"

while True:
    try:
        button = driver.find_element(by="xpath", value=xpath)
        if button:
            print("Element exists")
            button.click()
            time.sleep(10)
            # break
    except Exception as e:
        print("Element does not exist")
        print(e)
        time.sleep(1)

driver.quit()