from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get("http://seiyria.com/bootstrap-slider/")
slider = driver.find_element_by_css_selector("div#example-1 div.slider-handle.min-slider-handle.round")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(40, 0).release().perform()
driver.close()
