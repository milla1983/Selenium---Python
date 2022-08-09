from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
def calc(x,y):
   return str(int(x)+int(y))
  

try:

    browser = webdriver.Chrome("c:/Chromedriver/chromedriver.exe")
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR,"span#num1.nowrap").text
    

    y = browser.find_element(By.CSS_SELECTOR,"span#num2.nowrap").text
   
   
    rezult = calc(x,y)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    
    select.select_by_value(rezult)
    button1 = browser.find_element(By.XPATH, "//button[text()='Submit']")    
    
    button1.click()

   
finally:

    
    time.sleep(30)
    
    browser.quit()
