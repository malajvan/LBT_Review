from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs

import re,time
import logging

def do():
    driver=webdriver.Chrome()

    url= "https://www.google.com/maps/place/La+Belle+Tonki/@45.5405424,-73.6016345,17z/data=!4m7!3m6!1s0x4cc91938b54ff6a1:0xc2213cf2b19945f5!8m2!3d45.5405424!4d-73.5994458!9m1!1b1" #go straight to the review url of la belle tonki
    logging.info(f"Getting driver from url: {url}")
    driver.get(url)

    #find the total number of reviews the restaurant have
    number_of_reviews=int(re.findall(r'\b\d+\b',driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]').text)[0])
    logging.info(f'There are currently {number_of_reviews} reviews on Google')
    
    #scroll until end
    logging.info('Looking for scroll element...')
    scroll=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
    logging.info('Start scrolling...')
    for i in range(5): #number_of_reviews//10 +3): #sometimes scrolling in google go back to top so just in case
        driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight',scroll)
        time.sleep(3)
        logging.info(f'Scrolling for the {i+1} time')
    
    #expand comments by clicking the more button
    logging.info('Start expanding comments')
    revs=driver.find_elements(By.TAG_NAME,"button")
    logging.info('Start clicking "More" button...')
    for b in revs:
        if b.text == "More":
            b.click()

    # beautifulsoup html parser
    logging.info('Start parsing html with beautifulsoup')
    response = bs(driver.page_source, 'html.parser')
    reviews = response.find_all('div',class_="jftiEf fontBodyMedium")
    with open('source.html','w+') as f:
        for r in reviews:
            logging.info(f'Writting {r["aria-label"]}\'s review')
            f.write(str(r.prettify()))




"""
todo:
    * fix file structure: functions, rename etc.
    * organize, clean data
    * fix logging
"""

