from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
import time 

svc = webdriver.ChromeService(executable_path = binary_path)
driver = webdriver.Chrome(service = svc)

driver.get('https://www.flipkart.com/')
time.sleep(3)

search_bar = driver.find_element("xpath","//*[@placeholder='Search for Products, Brands and More']")

search_bar.send_keys('iphone')

search_bar.send_keys(Keys.ENTER)

prod = driver.find_element("class","_4WELSP")

prod.click()
time.sleep(5)

print(driver.current_url)

driver.close()