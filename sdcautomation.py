import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import csv
from selenium.webdriver.chrome.options import Options
from directkeys import PressKey, ReleaseKey, W, A, S, D
import autoit


def login():
    driver.find_element(By.XPATH, '//*[@id="btn_login" or onclick="OnLoginBtnClick();"]').click()
    # enter credentials
    time.sleep(soft_wait)
    driver.find_element(By.ID, 'accountID').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="header_btn_login_form"]').click()
    time.sleep(long_wait)


def invite():
    driver.find_element(By.XPATH, "//*[contains(text(), 'Invite')]").click()
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, name_of_party).click()
    time.sleep(soft_wait)


def mail():
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Email')]").click()
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, '//*[@class="ql-editor ql-blank"]').click()

    # use direct keys module to type the content
    time.sleep(soft_wait)
    PressKey(W)

    # click on EMail
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Email')]").click()
    # click on Add photo
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Add Photo')]").click()

    # enter the location of the image file you want send in next line
    autoit.control_set_text("Open", "Edit1", r"D:\ME\c dfrive\New folder\557421.jpg")
    autoit.control_send("Open", "Edit1", "{ENTER}")


if __name__ == "__main__":
    # credentials
    username = "IUNCTUS"
    password = "OURPROFILE"
    website_URL = "https://www.sdc.com/"

    # content to send
    message = "w"
    name_of_party = "Saint Valentine Party | Friday, February 14, 2020"

    # waits in sec
    soft_wait = 2
    long_wait = 4

    # load database
    file_name = 'Database.csv'
    csvFile = open(file_name, 'r', newline='')
    csvWriter = csv.writer(csvFile)

    # reading file in pandas DataFrame
    user_id = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 1))
    print(user_id.head(5))

    driver = webdriver.Chrome()
    driver.get(website_URL)
    time.sleep(long_wait)

    # login
    login()

    # open tab
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    # You can use (Keys.COMMAND + 't') on MAC

    for index in range(1, len(user_id)):
        id_url = "https://www.sdc.com/react/#/profile?idUser={}".format(user_id.at[index, 'User_id'])
        driver.get(id_url)
        time.sleep(long_wait)
        # invite()
        # mail()
