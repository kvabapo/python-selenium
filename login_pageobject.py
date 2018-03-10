from selenium import webdriver
from selenium.webdriver.common.by import By

'''Object style of code'''

class LoginPage(object):

    #locator fields
    un = (By.ID, "username")
    pw = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button")


    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self,url):
        self.driver.get(url)

    def input_credentials(self,username,password):
        self.driver.find_element(*self.un).send_keys(username)
        self.driver.find_element(*self.pw).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()



login_page = LoginPage(webdriver.Firefox())
login_page.go_to_url("http://the-internet.herokuapp.com/login")
login_page.input_credentials("tomsmith", "SuperSecretPassword!")
login_page.click_login_btn()
login_page.driver.quit()
