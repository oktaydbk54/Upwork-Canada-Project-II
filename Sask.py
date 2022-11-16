import pandas as pd

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
name = "ab"
url = "https://srna.ca.thentiacloud.net/webs/srna/register/#/search/{}/0/10".format(name)

### create_urls Test

def create_urls(url):

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    
    driver.get(url)
    time.sleep(3)
    results_number = driver.find_element(By.XPATH,value = '/html/body/div[3]/div/div[2]/div[2]/div/div[2]/div/span').text
    results_number = int(results_number.split(' ')[2])
    
    
    create_all_links = list()
    for item in range(0,results_number,10):
        url = f"https://srna.ca.thentiacloud.net/webs/srna/register/#/search/{name}/{item}/10"
        create_all_links.append(url)
    return create_all_links






#####test find_each_person_url function


def find_each_person_url(url):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    
    time.sleep(3)
    all_links = list()

    elems = driver.find_elements(By.TAG_NAME,'a')
    for elem in elems:
        try:
            href = elem.get_attribute('href')
            if '#registrant/' in href:
                all_links.append(href)
        except:
            pass
    return all_links



def collect_each_info(link):
    new_url = link.split('/')[-1]

    new_url_1 = f"https://srna.ca.thentiacloud.net/rest/public/registrant/get/?id={new_url}"

    r = requests.get(new_url_1)
    soup = BeautifulSoup(r.content,'html.parser')

    json_ = r.json()

    values_dict = {'First Name':json_['firstName'],
                   'Last Name':json_['lastName'],
                   'Registration Category':json_['registrationExpirationDate'],
                   'Registration Number':json_['registrationNumber'],
                   'Registration Status':json_['registrationStatus'],
                   'Registration Expiration Date':json_['registrationExpirationDate'],
                   'Initial Registration Date':json_['initialRegistrationDate']
                   }
    return values_dict


if __name__ == '__main__':
    
    
    name = "ab"
    url = "https://srna.ca.thentiacloud.net/webs/srna/register/#/search/{}/0/10".format(name)
    run_1 = create_urls(url)
    
    each_user_link_list = list()
    
    for item in run_1:
        run_2 = find_each_person_url(item)
        each_user_link_list.append(run_2)
    
    flatten_list = sum(each_user_link_list,[])
    uz = len(flatten_list)
    information_all_nurse_list = list()
    for item in flatten_list:
        run_3 = collect_each_info(item)
        information_all_nurse_list.append(run_3)
    
    df = pd.DataFrame(information_all_nurse_list)
    df.to_excel('Sask.xlsx',index = False)
    

    