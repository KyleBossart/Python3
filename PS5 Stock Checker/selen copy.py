
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')

#driver.get("https://www.bestbuy.com/site/marvels-spider-man-miles-morales-standard-launch-edition-playstation-5/6430146.p?skuId=6430146")

button = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
cart = driver.find_element_by_class_name("cart-link")
while cart.get_attribute("aria-label") != "Cart, 1 item":
    try:
        button = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
        cart = driver.find_element_by_class_name("cart-link")
        cart.get_attribute("aria-label")
        button.click()
        driver.close()
        time.sleep(2)
    except:
        button = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
        cart = driver.find_element_by_class_name("cart-link")
        cart.get_attribute("aria-label")
        print("fail")

print("in stock")


    

