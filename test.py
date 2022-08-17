from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


"""
    Changes by Mukesh :-
        we can use below three line of code as well in order to install updated chrome driver version based on you'r system chrome
"""
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

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

"""
    Changes by Mukesh :-
        We need to apply wait in order to achieve this scenario, You can learn more about different type of waits in selenium using below link
        https://selenium-python.readthedocs.io/waits.html
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_gender1')))

#Enter personal info, address info and contact info
driver.find_element(By.ID,'id_gender1').click()                               #first radio button