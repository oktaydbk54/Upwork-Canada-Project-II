import requests as re
from bs4 import BeautifulSoup

search_name = "aa"

url = f"https://www.nscn.ca/search-nurse?FirstName={search_name}&LastName=&RegNumber=&sort=&page=0"

r = re.get(url)
soup = BeautifulSoup(r.content,'html.parser')

pages_link = list()

for a in soup.find_all('a', href=True):
    if 'page' in a['href']:
        pages_link.append('https://www.nscn.ca/'+a['href'])

if len(pages_link) > 7:
    last_link = pages_link[-1]
    last_page_num = int(last_link.split('=')[-1])
else:
    last_page_num = 1

each_page = list()

for item in range(0,last_page_num):
    url = f"https://www.nscn.ca/search-nurse?FirstName={search_name}&LastName=&RegNumber=&sort=&page={item}"
    each_page.append(url)

all_links = list()
count = 0

for item in each_page:
    r = re.get(item)
    soup = BeautifulSoup(r.content,'html.parser')
    for a in soup.find_all('a', href=True):
        if 'licence-detail' in a['href']:
            all_links.append('https://www.nscn.ca/'+a['href'])
                
def collect_information_each_person(link):
    r = re.get(link)
    soup = BeautifulSoup(r.content,'html.parser')
    
    all_values = soup.find_all('div',class_ = 'col-sm-4 info-box')
    
    registration_number_list = ""
    name_list = ""
    last_list = ""
    register_list = ""
    
    category_of_licence_list = ""
    active_date_list = ""
    expiry_date_list = ""
    
    all_values_list = ""
    
    for item in all_values:
        all_values_list.append(item.text.strip().split('\n'))
    
    flatten_list = sum(all_values_list,[])
    
    all_values_list.clear()
    
    for item in flatten_list:
        all_values_list.append(item.strip())
    
    if len(all_values_list) == 9:
        
        if all_values_list[0] == 'Registration Number:':
            registration_number_list = all_values_list[1]
        if all_values_list[2] == 'Given Name(s):':
            name_list = all_values_list[3]
        if all_values_list[4] == 'Last Name(s):':
            last_list = all_values_list[5]
        if all_values_list[6] == 'Register:':
            register_list = all_values_list[7]
        if all_values_list[8] == 'Category of Licence:':
            category_of_licence_list = all_values_list[9]
        active_date_list = "None"
        expiry_date_list = "None"
        
    elif len(all_values_list) == 14:
        if all_values_list[0] == 'Registration Number:':
            registration_number_list = all_values_list[1]
        if all_values_list[2] == 'Given Name(s):':
            name_list = all_values_list[3]
        if all_values_list[4] == 'Last Name(s):':
            last_list = all_values_list[5]
        if all_values_list[6] == 'Register:':
            register_list = all_values_list[7]
        if all_values_list[8] == 'Category of Licence:':
            category_of_licence_list = all_values_list[9]
        if all_values_list[10] == 'Active Date:':
            active_date_list = all_values_list[11]
        if all_values_list[12] == 'Expiry Date:':
            expiry_date_list = all_values_list[13]
    res_dict = {'Registration Number':registration_number_list,
                'First Name':name_list,
                'Last Name':last_list,
                'Register':register_list,
                'Category of Licence':category_of_licence_list,
                'Active Date':active_date_list,
                'Expiry Date':expiry_date_list,
                'Link':link}
    return res_dict

results_list = list()

import pandas as pd

for item in all_links:
    run_1 = collect_information_each_person(item)
    results_list.append(run_1)

df = pd.DataFrame(results_list)
df.to_excel('NSCN.xlsx',index = False)









