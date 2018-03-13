from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://crossbrowsertesting.github.io/drag-and-drop.html")
dragfrom = driver.find_element_by_id("draggable")
dropto = driver.find_element_by_id("droppable")
ActionChains(driver).drag_and_drop(dragfrom, dropto).perform()
driver.quit()
