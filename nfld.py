import pandas as pd


import requests as re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = "https://crnnl.ca/member-search/"

search_name = input("Enter your key word: ")


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

driver.get(url)
time.sleep(5)


member_search = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[2]/div/div/section/div/form/input').send_keys(search_name)

search_button = driver.find_element(By.XPATH, value = '//*[@id="main"]/article/div/div[2]/div[2]/div/div/section/div/form/button').click()

time.sleep(3)

# next_page = driver.find_element(By.CLASS_NAME,)

all_links = list()

elems = driver.find_elements(By.TAG_NAME,'a')
for elem in elems:
    try:
        href = elem.get_attribute('href')
        if '/member/' in href:
            all_links.append(href)
    except:
        pass

driver.close()

name_list = list()
registration_list = list()
license_year_list = list()
initial_registration_list = list()
rn_status_list = list()
rn_effective_list = list()

rn_expiry_list = list()
other_registrations_list = list()
initial_np_licensure_list = list()
np_status_list = list()
np_category_list = list()
np_effective_list = list()
np_expiry_list = list()

current_np_employment_list = list()


for item in all_links:
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)

    driver.get(item)
    time.sleep(1)
    ####
    name = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/h1').text
    name_list.append(name)
    ####
    try:                                  
        registration = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[2]/span[1]/span').text
        registration_list.append(registration)
    except:
        registration = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[3]/span[1]/span').text
        registration_list.append(registration)
    ####    
    try:
        license_year = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[2]/span[2]/span').text 
        license_year_list.append(license_year)
    except:
        license_year = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[3]/span[2]/span').text 
        license_year_list.append(license_year)
        
    ####
    try:
        initial_registration = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[2]/span[3]/time').text
        initial_registration_list.append(initial_registration)
    except:
        initial_registration = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[3]/span[3]/time').text
        initial_registration_list.append(initial_registration)
    ####
    try:
        status = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div/div[1]/a').text 
        rn_status_list.append(status)
    except:
        status = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div/div[1]/a').text 
        rn_status_list.append(status)
    ####
    try:
        rn_effective = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div/div[2]/span[2]' ).text
        rn_effective_list.append(rn_effective)
    except:
        
        rn_effective = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div/div[2]/span[2]' ).text
        rn_effective_list.append(rn_effective)
    ####                                            
    rn_expiry = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div/div[3]/span[2]').text 
    rn_expiry_list.append(rn_expiry)
    ####
    try:
        initial_np_licensure = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/header/div[2]/span[4]/time').text 
        initial_np_licensure_list.append(initial_np_licensure)
    except:
        initial_np_licensure_list.append('None')
    try:
        np_status = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/a').text 
        np_status_list.append(np_status)
    except:
        np_status_list.append('None')
    try:
        np_category = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/a').text 
        np_category_list.append(np_category)
    except:
        np_category_list.append('None')
    try:
        np_effective = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div[2]/div[3]/span[2]').text 
        np_effective_list.append(np_effective)
    except:
        np_effective_list.append('None')
    try:
        np_expiry = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[2]/div[2]/div[4]/span[2]').text
        np_expiry_list.append(np_expiry)
    except:
        np_expiry_list.append('None')
    
    
    try:
        current_np_employment = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[3]/div/div').text
        current_np_employment_list.append(current_np_employment)
    except:
        current_np_employment_list.append('None')
    try:                                            
        other = driver.find_element(By.XPATH,value = '//*[@id="main"]/article/div/div[2]/div[1]/div/div/div[3]/p').text 
        other_registrations_list.append(other)
    except:
        other_registrations_list.append("None")
    driver.close()

df = pd.DataFrame()
df['Name'] = name_list
df['Registration'] = registration_list
df['License Year'] = license_year_list
df['Initial Registration'] = initial_registration_list
df['RN Status'] = rn_status_list
df['RN Effective'] = rn_effective_list
df['RN Expiry'] = rn_expiry_list
df['Initial NP Licensure'] = initial_np_licensure_list
df['NP Status'] = np_status_list
df['NP Category'] = np_category_list
df['NP Effective'] = np_effective_list
df['NP Expiry'] = np_expiry_list
df['Current NP Employment'] = current_np_employment_list
df['Other Registrations'] = other_registrations_list

df.to_excel('NFLD Data.xlsx',index = False)



























