
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
  
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
#driver.get("https://www.bestbuy.com/site/marvels-spider-man-miles-morales-standard-launch-edition-playstation-5/6430146.p?skuId=6430146")
def checkStock():
    button = driver.find_element_by_class_name("fulfillment-add-to-cart-button")
    button.click()
    time.sleep(1.5)
    cart = driver.find_element_by_class_name("cart-link")
    if cart.get_attribute("aria-label") == "Cart, 1 item":
        print("Woohoo")
        driver.close()
    else:
        print("no luck")
        driver.close()
        exec(open("selen.py").read())

checkStock()
    
