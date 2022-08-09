from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome("c:/Chromedriver/chromedriver.exe")
    browser.get(link)
    x_element = browser.find_element(By.XPATH, "//img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    option2.click()
    
    button1 = browser.find_element(By.XPATH, "//button[text()='Submit']")    
    
    button1.click()

finally:

    
    time.sleep(30)
    
    browser.quit()
