from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.curseforge.com/minecraft/modpacks/rlcraft")
# elem = driver.find_element_by_name("q")
# elem.send_keys("iu wallpaper 4k")
# elem.send_keys(Keys.RETURN)

# SCROLL_PAUSE_TIME = 2
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     time.sleep(SCROLL_PAUSE_TIME)

#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count = 1
# for image in images:
#     image.click()
#     time.sleep(3)
#     imgURL = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
#     urllib.request.urlretrieve(imgURL, str(count) + ".jpg")
#     count += 1



# assert "Python" in driver.title
# elem.clear()
# assert "No results found." not in driver.page_source
# driver.close()