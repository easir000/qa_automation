
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTest1():
    def placeorder(self):
        s=Service('C:\browedriver\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        
        
        url="https://training.nop-station.com/"


        driver.get(url)
        driver.maximize_window()
        hover = driver.find_element("xpath", '/html/body/div[6]/div[2]/ul[1]/li[6]/a')
        actions = ActionChains(driver)
        actions.move_to_element(hover).perform()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[6]/div[2]/ul[1]/li[6]/ul/li[2]/a').click()
        time.sleep(1)
        
        # electronics  = driver.find_element("xpath", '/html/body/div[6]/div[2]/ul[1]/li[6]/a')
        # electronics.click()
        # Cell_phones   = driver.find_element("xpath", '/html/body/div[6]/div[2]/ul[1]/li[6]/ul/li[2]/a').click()
        phones  = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/h2/a').click()
        time.sleep(1)
        quantity  = driver.find_element("id", 'product_enteredQuantity_20').clear()
        quantity  = driver.find_element("id", 'product_enteredQuantity_20').send_keys("2")
        time.sleep(1)
        # cart  = driver.find_element("id", "add-to-cart-button-20").click()
         
        add_to_cart  = driver.find_element("xpath", '//*[@id="add-to-cart-button-20"]').click()
        time.sleep(1)
        
        
        
        # go_to_cart  = driver.find_element("id", 'flyout-cart').click()
        
        # cart = driver.find_element ("xpath",'/html/body/div[5]/div/span').click()
        cart  = driver.find_element("xpath", '/html/body/div[5]/div/span').click()
        
        # go_to_cart  = driver.find_element("xpath", '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[4]/a/span[1]').click()
        
        hover = driver.find_element("xpath", '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[4]/a/span[1]')
        actions = ActionChains(driver)
        actions.move_to_element(hover).perform()
        time.sleep(1)
        
        
        go_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", "/html/body/div[6]/div[1]/div[1]/div[2]/div[2]/div/div[4]/button"))).click()
        # action = ActionChains(driver)
        service  = driver.find_element("id",'termsofservice').click()
        service  = driver.find_element("id", 'checkout').click()
        guests  = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/button[1]').click()

        
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_FirstName"]').send_keys("Easir")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_LastName"]').send_keys("Maruf")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_Email"]').send_keys("easir956@gmail.com")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_Company"]').send_keys("rapid lodgements")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_CountryId"]').send_keys("Australia")
        time.sleep(5)
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_StateProvinceId"]').send_keys("New South Wales")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_City"]').send_keys("Alexandria ")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_Address1"]').send_keys("Alexandria NSW 2015, Australia ")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_Address2"]').send_keys("same ")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_ZipPostalCode"]').send_keys("2599 ")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_PhoneNumber"]').send_keys("+61480049741 ")
        element = driver.find_element(by=By.XPATH, value= '//*[@id="BillingNewAddress_FaxNumber"]').send_keys(" (02) 8202 2209 ")
        continues = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[2]/ol/li[1]/div[2]/div/button[4]').click()
        time.sleep(1)
        
        
        cross = driver.find_element("id", 'shippingoption_1').click()
        
        cont = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[2]/ol/li[3]/div[2]/form/div[2]/button').click()
        
        time.sleep(1)
        
        element = driver.find_element("id", 'paymentmethod_1').click()
        element = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[2]/ol/li[4]/div[2]/div/button').click()
        time.sleep(1)
        
        card = driver.find_element("id", 'CreditCardType').send_keys("Visa")
        card = driver.find_element("xpath", '//*[@id="CardholderName"]').send_keys("Maruf")
        card = driver.find_element("xpath", '//*[@id="CardNumber"]').send_keys("4242424242424242")
        card = driver.find_element("id", 'ExpireMonth').send_keys("02")
        card = driver.find_element("id", 'ExpireYear').send_keys("2024")
        card = driver.find_element("id", 'CardCode').send_keys("1234")
        time.sleep(1)
        confirms  = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[2]/ol/li[5]/div[2]/div/button').click()
        
        time.sleep(1)
        order = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[2]/ol/li[6]/div[2]/div[2]/button').click()
        
        time.sleep(1)
        pdf = driver.find_element("xpath", '/html/body/div[6]/div[3]/div/div/div/div[1]/a[2]').click()
        
        
        time.sleep(2)
        
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
              
        
        
        
       
        time.sleep(10)
        
        
        driver.close() 

test = MyTest1()
test.placeorder()
# test.query()