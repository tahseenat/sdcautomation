import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def navigate():
    # go to contacts
    time.sleep(long_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Explore')]").click()
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Connect')]").click()
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Contacts')]").click()
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, """//*[@id="app-bar"]/div[2]/div/button""").click()

    # click on the likes given manually
    time.sleep(long_wait + soft_wait)



def login():
    driver.find_element(By.XPATH, '//*[@id="btn_login" or onclick="OnLoginBtnClick();"]').click()
    # enter credentials
    time.sleep(soft_wait)
    driver.find_element(By.ID, 'accountID').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="header_btn_login_form"]').click()
    time.sleep(long_wait)


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # driver.manage().window().maximize()
    username = "IUNCTUS"
    password = "OURPROFILE"
    website_URL = "https://www.sdc.com/"

    # waits in sec
    soft_wait = 2
    long_wait = 4

    # INITIALIZE driver
    driver.get(website_URL)
    time.sleep(1)

    # login
    login()
    # navigate()
    time.sleep(10)
    elem = driver.find_element_by_tag_name("body")

    no_of_pagedowns = 10
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(soft_wait)
        no_of_pagedowns -= 1

    time.sleep(long_wait)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    ids = []
    mydivs = soup.findAll('div', class_="member-img", id=True)
    # post_elems = driver.find_elements_by_class_name("member-img")
    # temp = [x for x in soup.find_all("div", attrs={"class": "member-img"})]

    for div in mydivs:
        ids.append(div['id'])

    # print(ids)
    print("User Fetched:", len(ids))
    ids = list(map(int, ids))
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

    # reading file in pandas dataframe
    user_id = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 1))

    # storing data in list
    user_array = [x for x in user_id["User_id"]]

    # open file for appending
    csvFile = open(file_name, 'a', newline='')
    csvWriter = csv.writer(csvFile)

    # appending new user ids
    c = 0
    for i in range(len(ids)):
        if ids[i] not in user_array:
            csvWriter.writerow([ids[i]])
            c += 1
    csvFile.close()
    print("New User appended:", c)
    driver.close()
