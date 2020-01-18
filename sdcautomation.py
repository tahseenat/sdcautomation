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

    # content to send
    message = "w"
    name_of_party = "Saint Valentine Party | Friday, February 14, 2020"
    no_of_contacts = 900

    # waits in sec
    soft_wait = 2
    long_wait = 4

    driver = webdriver.Chrome()
    website_URL = "https://www.sdc.com/"
    driver.get(website_URL)

    time.sleep(long_wait)
    login()

    file_name = 'Database.csv'
    csvFile = open(file_name, 'r', newline='')
    csvWriter = csv.writer(csvFile)

    # reading file in pandas DataFrame
    user_id = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 1))


    # go to contacts
    # time.sleep(long_wait)
    # driver.find_element(By.XPATH, "//*[contains(text(), 'Explore')]").click()
    # time.sleep(soft_wait)
    # driver.find_element(By.XPATH, "//*[contains(text(), 'Connect')]").click()
    # time.sleep(soft_wait)
    # driver.find_element(By.XPATH, "//*[contains(text(), 'Contacts')]").click()
    # time.sleep(soft_wait)
    # driver.find_element(By.XPATH, '//*[@id="app-bar"]/div[2]/div/button').click()

    # click on the likes given manually
    # time.sleep(long_wait + soft_wait)
    # element = driver.find_element(By.XPATH, "//*[contains(text(), 'Likes given')]")
    # driver.execute_script("arguments[0].click();", element)

