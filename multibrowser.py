from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


#driver = webdriver.Chrome(executable_path="D:\Miscellaneous\Selenium\drivers\ChromeDriver\chromedriver.exe")

driver = webdriver.Firefox(executable_path="D:\Miscellaneous\Selenium\drivers\GeckoDriver\geckodriver.exe")
driver.get("https://npskengeri.edchemy.com/")

print(driver.title)
print(driver.current_url)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sn_login_id")))
    emailId = driver.find_element_by_id("sn_login_id")
    pwd     = driver.find_element_by_id("sn_login_password")

    emailId.send_keys("muttu2244@yahoo.com")
    pwd.send_keys("May2020*")

    #driver.find_element_by_class_name("glyphicon glyphicon-log-in").click()
    #driver.find_element_by_xpath("//*[@id='sn_login_form']/button/text()").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='sn_login_form']/button"))).click()
    elementAfterLogin = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"sn_dashboard_title")))
    print(elementAfterLogin.is_displayed())
    time.sleep(5)
    driver.find_element(By.ID, "menu-toggle").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='sn_features']/ul/li[4]/a").click()

    drpElement = driver.find_element_by_xpath("//select[@name='publication_datagrid_length']")
    time.sleep(5)
    drpObj = Select(drpElement)
    time.sleep(5)
    drpObj.select_by_visible_text('12')
    time.sleep(5)
    drpObj.select_by_value('48')
    time.sleep(5)

    #Logout
    driver.find_element(By.XPATH, "//*[@id='sn_logout']").click()
    time.sleep(5)
    #driver.switch_to_alert().accept() #accept presses OK
    #driver.find_element((By.ID, "sn_logout")).click()
    driver.switch_to_active_element()
    driver.find_element_by_id("button-0").click()

finally:
    pass
    #driver.close() # close current browser window only
    #driver.quit() #closes all the browser windows

