from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#will timeout for after 5 seconds because element is not found.
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.airasia.com/')
el = driver.find_element(By.NAME, 'query')
