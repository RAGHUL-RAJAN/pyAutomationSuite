# from selenium import webdriver
# from chromedriver_py import binary_path
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# svc = webdriver.ChromeService(executable_path = binary_path)
# driver = webdriver.Chrome(service = svc)

# driver.get("https://www.yatra.com/flights")

# from_destination = driver.find_element(By.XPATH,"//*[@title='New Delhi']")
# from_destination.click()
# time.sleep(2)
# inputfield = driver.find_element(By.XPATH,"//*[@id='input-with-icon-adornment']")
# inputfield.send_keys("Chennai")
# inputfield.send_keys(Keys.ENTER)

# time.sleep(2)
# to_destination = driver.find_element(By.XPATH,"//*[text()='Mumbai']")
# to_destination.click()

# time.sleep(5)
# inputfield = driver.find_element(By.XPATH,"//*[@id='input-with-icon-adornment']")
# inputfield.send_keys("Dubai")
# inputfield.send_keys(Keys.ENTER)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # ✅ Corrected import
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

svc = Service(executable_path=binary_path)  # ✅ Corrected
driver = webdriver.Chrome(service=svc)
driver.maximize_window()

driver.get("https://www.yatra.com/flights")

wait = WebDriverWait(driver, 10)

# Click on "From" location
from_destination = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@title='New Delhi']")))
from_destination.click()

# Enter "Chennai"
inputfield = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='input-with-icon-adornment']")))
inputfield.send_keys("Chennai")
inputfield.send_keys(Keys.ENTER)

# Select "Mumbai"
to_destination = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='mumbai']")))
to_destination.click()

# Enter "Dubai"
inputfield = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='input-with-icon-adornment']")))
inputfield.send_keys("Dubai")
inputfield.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
