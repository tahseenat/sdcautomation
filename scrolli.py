import csv
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.manage().window().maximize()
username = "IUNCTUS"
password = "OURPROFILE"

# content to send
message = "w"
name_of_party = "Saint Valentine Party | Friday, February 14, 2020"
no_of_contacts = 3000

# waits in sec
soft_wait = 2
long_wait = 4
driver.get("https://www.sdc.com/")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="btn_login" or onclick="OnLoginBtnClick();"]').click()

# enter credentials
time.sleep(soft_wait)
driver.find_element(By.ID, 'accountID').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="header_btn_login_form"]').click()

time.sleep(long_wait)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 100

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    no_of_pagedowns -= 1

# post_elems = driver.find_elements_by_class_name("member-img")
time.sleep(10)
page_source = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
ids = []
mydivs = soup.findAll('div', class_="member-img", id=True)
# temp = [x for x in soup.find_all("div", attrs={"class": "member-img"})]

for div in mydivs:
    ids.append(div['id'])

# print(ids)
print(len(ids))
# (//*[@class='member-img'])[]

file_name = 'Database.csv'
# try to open file to check existence
try:
    f = open(file_name)
    f.close()
except:
    csvFile = open(file_name, 'a', newline='')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['User_id'])

# open file for appending
csvFile = open(file_name, 'a', newline='')
csvWriter = csv.writer(csvFile)

# reading file in pandas DataFrame
user_id = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 1))

# storing data in list
user_array = [x for x in user_id["User_id"]]

# appending new user ids
for i in range(len(ids)):
    if ids[i] not in user_array:
        csvWriter.writerow([ids[i]])
