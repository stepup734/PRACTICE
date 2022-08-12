from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#Launch URL
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#Click on signin link
driver.find_element(By.LINK_TEXT,"Sign in").click()

#Enter email address in "CREATE AN ACCOUNT" section
driver.find_element(By.XPATH,"//*[@id='email_create']").send_keys("shivaninegi75@yahoo.in")

#Click on create an account button
driver.find_element(By.XPATH,"//*[@id='SubmitCreate']").click()

#Enter personal info, address info and contact info
driver.find_element(By.ID,'id_gender1').click()                               #first radio button
