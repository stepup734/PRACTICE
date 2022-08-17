from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#Launch URL
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#Click on signin link
driver.find_element(By.LINK_TEXT,"Sign in").click()

driver.find_element(By.XPATH,"//*[@id='email']").send_keys("shivaninegi75@ya.in")
driver.find_element(By.XPATH,"//*[@id='passwd']").send_keys("12345666")
driver.find_element(By.ID,'SubmitLogin').click()
error=driver.find_element(By.XPATH,"//*[@id='center_column']/div[1]/ol")
# print(error.text)
error_text=error.text
if error_text=="Authentication failed.":
    print("invalid email address")




