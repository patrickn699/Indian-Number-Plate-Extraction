from bs4 import BeautifulSoup as bs
import urllib
from pprint import pprint
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pandas as pd


def fetch( numb):

    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('headless')
    #options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    chrome_path = r'E:/Chrome Downloads/chromedriver_win32/chromedriver.exe'
    options.binary_location = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
    driver = webdriver.Chrome(executable_path=chrome_path,chrome_options=options)

    #pas = 'vehicledetails@1'
    #bro = webdriver.Chrome()
    #url = 'https://vahan.nic.in/nrservices/faces/user/citizen/citizenlogin.xhtml'
    #url1 = 'https://vahaninfos.com/vehicle-details-by-number-plate'
    url2 = 'https://www.drivespark.com/rto-vehicle-registration-details/'
    
    try:
        driver.get(url2)
        time.sleep(5)
        print(numb)

        box = driver.find_element_by_xpath('//*[@id="reg_num"]')
        #box1 = driver.find_element_by_id('fuelcalculatebtn')
        box.send_keys(numb)
        #WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fuelcalculatebtn"]')))
        #driver.find_element_by_xpath('//*[@id="fuelcalculatebtn"]').click()
        driver.find_element_by_id('fuelcalculatebtn').click()
        time.sleep(5)
        get_url = driver.current_url
        #pg = driver.page_source(get_url)
        #print(get_url)
        ds = pd.read_html(get_url)
        
        ds = ds[1]
        print(ds)
        return ds

    except Exception as e:
        print(e)