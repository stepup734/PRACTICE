import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

##########################################   1  ########################################################################

# serv_obj=Service('C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\chromedriver.exe')
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://www.google.com")
# driver.maximize_window()
#
# print(driver.title)
# print(driver.current_url)

##########################################   2  ########################################################################

# serv_obj=Service('C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\chromedriver.exe')
# driver=webdriver.Chrome(service=serv_obj)
# serv_obj=Service('C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\geckodriver.exe')
# driver=webdriver.Firefox(service=serv_obj)
# serv_obj=Service('C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\msedgedriver.exe')
# driver=webdriver.Edge(service=serv_obj)
# driver.get("https://www.google.co.in")

##########################################   3  ########################################################################
# from selenium.webdriver.common.by import By
#
# serv_obj=Service('C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\chromedriver.exe')
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.get("https://opensource-demo.orangehrmlive.com/")    #open first browser window
# driver.maximize_window()
#
# driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()  #open second browser window
# window_ids=driver.window_handles
# print(window_ids)
#
# for windid in window_ids:
#     driver.switch_to.window(windid)
#     time.sleep(5)
#     driver.close()


