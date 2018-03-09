from selenium import webdriver

'''Procedural style of code'''

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
driver.find_element_by_css_selector("button").click()
