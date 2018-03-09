from selenium import webdriver

'''Function style of code'''

def login_a_page(url, username, password):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_css_selector("button").click()

login_a_page("http://the-internet.herokuapp.com/login", "tomsmith", "SuperSecretPassword!")
