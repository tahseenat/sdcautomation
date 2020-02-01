import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import autoit
import keyboard


def login():
    driver.find_element(By.XPATH, '//*[@id="btn_login" or onclick="OnLoginBtnClick();"]').click()
    # enter credentials
    time.sleep(soft_wait)
    driver.find_element(By.ID, 'accountID').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="header_btn_login_form"]').click()
    time.sleep(long_wait)


def invite():
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Invite')]").click()
    time.sleep(soft_wait)
    party_xpath = "//*[contains(text(), '{}')]".format(name_of_party)
    driver.find_element(By.XPATH, party_xpath).click()
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Cancel')]").click()
    time.sleep(soft_wait)


def mail():
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Email')]").click()
    time.sleep(long_wait)
    driver.find_element(By.XPATH, '//*[@class="ql-editor ql-blank"]').click()
    time.sleep(soft_wait)
    keyboard.write(message)
    time.sleep(soft_wait)

    # click on Add photo
    time.sleep(soft_wait)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Add Photo')]").click()
    time.sleep(soft_wait)

    # enter the location of the image file you want send in next line
    autoit.control_set_text("Open", "Edit1", r"D:\ME\c dfrive\New folder\557421.jpg")
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(soft_wait)

    driver.find_element(By.XPATH, "//*[contains(text(), 'Send')]").click()
    time.sleep(long_wait + soft_wait + long_wait)


if __name__ == "__main__":
    # credentials
    username = "IUNCTUS"
    password = "OURPROFILE"
    website_URL = "https://www.sdc.com/"

    # content to send
    message = "Hello, sexies!!!"

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

    for index in range(len(user_id)):
        # open tab
        driver.switch_to.window((driver.window_handles[0]))
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(soft_wait)
        id_url = "https://www.sdc.com/react/#/profile?idUser={}".format(user_id.at[index, 'User_id'])
        print("processing -> {} user".format(index))
        driver.get(id_url)
        time.sleep(long_wait)
        mail()
        time.sleep(soft_wait)
        invite()
        driver.close()
