from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get("http://seiyria.com/bootstrap-slider/")
source_element = driver.find_element_by_class_name('slider-track')
slider = driver.find_element_by_css_selector(".round[style='left: 76%;']")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(40, 0).release().perform()
driver.close()
