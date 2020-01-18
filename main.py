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

self = webdriver.Chrome()

website_URL = "https://www.sdc.com/"
self.get(website_URL)

time.sleep(10)
self.find_element(By.XPATH, "//*[@id="btn_login" or onclick="OnLoginBtnClick();"]").click();






# self.close()
# for i in range(l):
#     print("Processing code num: ", i)
#     self.find_element(By.ID, "twotabsearchtextbox").click()
#     element = self.find_element(By.CSS_SELECTOR, ".nav-search-submit > .nav-input")
#     actions = ActionChains(self)
#     actions.move_to_element(element).perform()
#     self.find_element(By.ID, "twotabsearchtextbox").clear()
#     url = "url not found"
#     price = "price_not_found"
#     rank = "rank not found"
#     asin = "asin code not available"
#     tempupc = upc[i]
#     tempupc = str(tempupc)
#     tempupc = "0"*(13 - len(tempupc)) + tempupc
#
#     try:
#         self.find_element(By.ID, "twotabsearchtextbox").send_keys(tempupc)
#         self.find_element(By.CSS_SELECTOR, ".nav-search-submit > .nav-input").click()
#
#         # temp = str(upc[i])
#         # temp.replace("+","%2B")
#
#         # click on the product
#         try:
#             self.find_element(By.XPATH,
#                               "//*[@class ='a-link-normal a-text-normal' and contains(@href,'keywords=" + tempupc +
#                               "&')][1]").click()
#             price = self.find_element(By.XPATH, "(//*[contains(@class, 'a-color-price')])[1]").text
#             url = self.current_url
#         except:
#             try:
#                 self.find_element(By.XPATH,
#                                   "//*[@class ='a-link-normal a-text-normal' and contains(@href,'keywords={}')]".
#                                   format(tempupc)).click()
#                 price = self.find_element(By.XPATH, "(//*[contains(@class, 'a-color-price')])[1]").text
#                 url = self.current_url
#             except:
#                 print("")
#         time.sleep(2)
#
#         # Paperback edition
#         try:
#             self.find_element(By.XPATH, "(//*[contains(text(), 'Paperback')])[2]").click()
#             time.sleep(2)
#         except:
#             print("no paperback edition")
#         # ASIN code
#         try:
#
#
