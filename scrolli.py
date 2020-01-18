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

no_of_pagedowns = 20

while no_of_pagedowns:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    no_of_pagedowns -= 1

# post_elems = driver.find_elements_by_class_name("member-img")

page_source = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
ids = []
mydivs = soup.findAll('div', class_="member-img", id=True)
for div in mydivs:
    ids.append(div['id'])
print(ids)
print(len(ids))
