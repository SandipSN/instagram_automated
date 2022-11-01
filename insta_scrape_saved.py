from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget
import pandas as pd
import re
from dotenv import load_dotenv

# Password for the Instagram account being used is stored in .env
load_dotenv('.env')
password = os.getenv("ui_expo_password")

def insta_scraper(folder, make_new_directory):

    driver = webdriver.Edge('C:/Users/aksc7/Documents/Websites/auto_soc_med/msedgedriver.exe')

    #open the webpage
    driver.get("https://www.instagram.com/ui.expo/saved/to-post/17954144813066298/")
    driver.maximize_window()

    #target the cookies button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]'))).click()
    
    

    #target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    #enter username and password
    username.clear()
    username.send_keys("ui.expo")
    password.clear()
    password.send_keys(password)

    #target the login button and click it
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #handle NOT NOW
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    #not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    
    # Wait for 5 seconds
    time.sleep(5)

    #scroll down to scrape more images
    #driver.execute_script("window.scrollTo(0, 10000)")
    #time.sleep(1)
        

    #target all images links on the page
    images = driver.find_elements(By.TAG_NAME, 'a')
    images = [image.get_attribute('href') for image in images]
    images = images[1:-2]
    print('Number of scraped images: ', len(images))
    print(images)
   
    posts = []
    captions = []

    path = os.getcwd()
    path = os.path.join(path, folder)

    #create the directory
    if make_new_directory == 1:
        os.mkdir(path)
    elif make_new_directory == 0:
        pass
      
    for link in images:
        driver.get(link)
        time.sleep(3)
        post = driver.find_elements(By.TAG_NAME, 'img')
        try:
            post_link = post[1].get_attribute('src')
        except:
            continue
        try:
            designer = driver.find_element(By.NAME, 'twitter:title').get_attribute('content')
        except:
            continue
        designer_cleaned =  re.findall('@([a-zA-Z0-9\d*\.\_]+)', designer)

        posts.append(post_link)
        captions.append(designer_cleaned)
        print(posts)
               
        # download images
        
        save_as = os.path.join(path, str(designer_cleaned) + '.jpg')
        wget.download(post_link, save_as)
        

insta_scraper("to_be_posted", 0)