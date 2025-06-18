from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
import time

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

driver.get('https://www.python.org/')
print(driver.title)
search_bar = driver.find_element("xpath","//*[@placeholder='Search']")   
search_bar.send_keys("Getting start with python")

search_bar.send_keys(Keys.ENTER)

time.sleep(5)

