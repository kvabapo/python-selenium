from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

btn1 = "div#content li:nth-child(1) > button"
btn2 = "div#content li:nth-child(2) > button"
btn3 = "div#content li:nth-child(3) > button"

driver.find_element_by_css_selector(btn1).click()
driver.switch_to.alert
driver.switch_to.alert.accept()

result = driver.find_element_by_id("result").text
print(result)
assert result == "You successfuly clicked an alert"

driver.close()
