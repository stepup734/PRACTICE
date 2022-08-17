from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Users\Admin\\Desktop\\QA\\Selenium\\Drivers\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#Launch URL
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

#Click on signin link
driver.find_element(By.LINK_TEXT,"Sign in").click()

# #Enter email address in "CREATE AN ACCOUNT" section
# driver.find_element(By.XPATH,"//*[@id='email_create']").send_keys("shivaninegi75@yahoo.in")
#
# #Click on create an account button
# driver.find_element(By.XPATH,"//*[@id='SubmitCreate']").click()
#
# #Enter personal info, address info and contact info
# element = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, 'id_gender1')))
# driver.find_element(By.ID,'id_gender1').click()                               #first radio button
# driver.find_element(By.XPATH,"//*[@id='customer_firstname']").send_keys("Shivani")
# driver.find_element(By.XPATH,"//*[@id='customer_lastname']").send_keys("Negi")
# driver.find_element(By.XPATH,"//*[@id='passwd']").send_keys("1234455666")
# days = WebDriverWait(driver, 20).until(
#        EC.presence_of_element_located((By.XPATH,"//*[@id='days']")))
# days=Select(days)
# days.select_by_value("1")
# month=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@id='months']")))
# month=Select(month)
# month.select_by_value("2")
# year=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@id='years']")))
# year=Select(year)
# year.select_by_value("2022")
# driver.find_element(By.XPATH,"//*[@id='firstname']").send_keys("Shivani")
# driver.find_element(By.XPATH,"//*[@id='lastname']").send_keys("Negi")
# driver.find_element(By.XPATH,"//*[@id='address1']").send_keys("12529 State Road 535")
# driver.find_element(By.XPATH,"//*[@id='city']").send_keys("Orlando")
# state=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@id='id_state']")))
# state=Select(state)
# state.select_by_visible_text("Florida")
# driver.find_element(By.XPATH,"//*[@id='postcode']").send_keys("32836")
# country=WebDriverWait(driver,20).until((EC.presence_of_element_located((By.XPATH,"//*[@id='id_country']"))))
# country=Select(country)
# country.select_by_value("21")
# driver.find_element(By.XPATH,"//*[@id='phone_mobile']").send_keys("8744677856")
# driver.find_element(By.XPATH,"//*[@id='alias']").send_keys("Robert Robertson")
#Click on register button
# driver.find_element(By.XPATH,"//*[@id='submitAccount']").
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("shivaninegi75@yahoo.in")
driver.find_element(By.XPATH,"//*[@id='passwd']").send_keys("1234455666")
driver.find_element(By.ID,'SubmitLogin').click()













