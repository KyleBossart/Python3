
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

driver = webdriver.Chrome()
#driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
driver.get("https://www.bestbuy.com/site/marvels-spider-man-miles-morales-standard-launch-edition-playstation-5/6430146.p?skuId=6430146")
def checkStock():
    button = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
    button.click()
    time.sleep(1.5)
    cart = driver.find_element_by_class_name("cart-link")
    while cart.get_attribute("aria-label") != "Cart, 1 item":
        print("Not in stock at Best Buy @ " + )
        driver.close()

checkStock()
    
