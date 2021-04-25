from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
def class_open():
    PATH ="E:\HACATHON\JIBO\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.set_window_size(1024,600)
    driver.maximize_window()
    driver.get("https://cuchd.blackboard.com/")

    username = driver.find_element_by_id("user_id")
    username.send_keys("20bcs6717")
    password = driver.find_element_by_id("password")
    password.send_keys("Karan@7017")
    submit = driver.find_element_by_id("entry-login")
    submit.send_keys(Keys.RETURN)

    time.sleep(10)

    driver.find_element_by_link_text("BIOLOGY FOR ENGINEERS").click()

    time.sleep(5)

    driver.find_element_by_id("sessions-list-dropdown").click()
    driver.find_element_by_link_text("Course Room").click()
    
""" driver.find_element_by_css_selector("button[class*='status-selector__toggle']").click()
time.sleep(5)
driver.find_element_by_link_text("Leave session").click()
driver.close() """