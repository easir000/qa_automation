import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select



class MyTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def register_process(self):
        
        self.driver.get("https://training.nop-station.com/") 
        
        self.driver.maximize_window()
        # self.driver.get("https://training.nop-station.com/register?returnUrl=%2F")
        #successfully navigated to URL_1
        

        elem  =  self.driver.find_element(by=By.XPATH, value= '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="gender-male"]').click()
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="FirstName"]').send_keys("Maruf")
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="LastName"]').send_keys("Easir")
        elem  =  self.driver.find_element(by=By.XPATH, value= '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]').send_keys("20")
        elem  =  self.driver.find_element(by=By.XPATH, value= '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]').send_keys("May")
        elem  =  self.driver.find_element(by=By.XPATH, value= '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]').send_keys("1995")
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="Email"]').send_keys("easir9566@gmail.com")
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="Company"]').send_keys("Rapid_Lodgment")
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="Newsletter"]').get_attribute('checked')
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="Password"]').send_keys("hellobrain")
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="ConfirmPassword"]').send_keys("hellobrain")
        elem  =  self.driver.find_element(by=By.XPATH, value= '//*[@id="register-button"]').click()
        elem  =  self.driver.find_element(by=By.XPATH, value= '/html/body/div[6]/div[3]/div/div/div/div[2]/div[2]/a').click()
        
        

        time.sleep(10)
        self.driver.close() 

test = MyTest()
test.register_process()
# test.query()
        
        
     
