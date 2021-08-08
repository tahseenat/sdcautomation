from selenium import webdriver

url = 'https://zety.com/mycv/tahseenat'
path = 'ss.png'

driver = webdriver.Chrome()
driver.get(url)
el = driver.find_element_by_tag_name('body')
el.screenshot(path)
driver.quit()