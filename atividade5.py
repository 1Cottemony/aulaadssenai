from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://google.com")
search_box = driver.find_element("name", "q")
time.sleep(10)
search_box.send_keys("Automação com Python")
search_box.send_keys(Keys.RETURN)
time.sleep(30)
driver.quit()