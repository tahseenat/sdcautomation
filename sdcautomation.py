import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import csv
from selenium.webdriver.common.keys import Keys
import autoit
import keyboard
from tqdm import tqdm


def login():
    driver.find_element(By.XPATH, '//*[@id="btn_login" or onclick="OnLoginBtnClick();"]').click()

    elem = driver.find_element_by_tag_name("body")

    no_of_pagedowns = 1
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(soft_wait)
        no_of_pagedowns -= 1
    # enter credentials
    time.sleep(soft_wait)
    driver.find_element(By.ID, 'LoginaccountID').send_keys(username)
    driver.find_element(By.ID, 'Loginpassword').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login_btn_login_form"]').click()
    time.sleep(long_wait)


def invite():
    try:
        time.sleep(soft_wait)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Invite')]").click()
        time.sleep(soft_wait)
        party_xpath = "//*[contains(text(), '{}')]".format(name_of_party)
        driver.find_element(By.XPATH, party_xpath).click()
        time.sleep(soft_wait)
        driver.find_element(By.XPATH, "//*[contains(text(), 'Cancel')]").click()
        time.sleep(soft_wait)
    except:
        pass


def mail():
    try:
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
        time.sleep(long_wait)
    except:
        pass


if __name__ == "__main__":
    # enter credentials
    username = "IUNCTUS"
    password = "TahirDoesMagic2000"
    website_URL = "https://www.sdc.com/"

    # enter content to send
    message = "Hello, sexies!!!"

    name_of_party = "Saint Valentine Party | Friday, February 14, 2020"

    # specify waits in sec
    soft_wait = 2
    long_wait = 8

    # load database
    file_name = 'Database.csv'
    csvFile = open(file_name, 'r', newline='')
    csvWriter = csv.writer(csvFile)

    # reading file in pandas DataFrame
    user_id = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 2))

    # driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome()
    driver.get(website_URL)
    time.sleep(long_wait)

    # login
    login()

    start_sending_from_user = 0
    for index in tqdm(range(start_sending_from_user, len(user_id))):
        # open tab
        if user_id.at[index, 'Flag'] == "Not Sent":
            driver.switch_to.window((driver.window_handles[0]))
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            id_url = "https://www.sdc.com/react/#/profile?idUser={}".format(user_id.at[index, 'User_id'])
            driver.get(id_url)
            time.sleep(long_wait)
            mail()
            time.sleep(soft_wait)
            invite()
            driver.close()
            user_id.at[index, 'Flag'] = "Sent"
            user_id.to_csv(file_name, index=False)
    driver.close()
