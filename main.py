import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import json

BASE_DIR = os.getcwd()

# Chrome driver version= 98.0
PATH = os.path.join(BASE_DIR, "chromedriver")
SEARCH_PATH = '//*[@id="twotabsearchtextbox"]'
SEARCH_CLICK_PATH = '//*[@id="nav-search-submit-button"]'
MOBILE_HREF_PATH = '//*[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]'
GET_MOBILE_NAME = '//*[@id="productTitle"]'
GET_MOBILE_INFO = '//*[@id="productOverview_feature_div"]/div'
GET_ABOUT_PRODUCT = '//*[@id="feature-bullets"]'
NEXT_PAGE = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[28]/div/div/span/a[3]'


WEBSITE = "https://www.amazon.in/"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(PATH, options=options)

searchId = "mobile"

# try:
#     driver.get(WEBSITE)
#     # loginBox = driver.find_element_by_xpath(SEARCH_PATH)
#     loginBox = driver.find_element(By.XPATH, SEARCH_PATH)
#     loginBox.send_keys(searchId)
        
#     # nextButton = driver.find_elements_by_xpath(SEARCH_CLICK_PATH)
#     nextButton = driver.find_element(By.XPATH, SEARCH_CLICK_PATH).click()
#     # nextButton[0].click()

#     # mob_vars = driver.find_elements_by_xpath(MOBILE_HREF_PATH)
#     mob_vars = driver.find_elements(By.XPATH, MOBILE_HREF_PATH)

#     linked_list = []
#     for mob_var in mob_vars:
#         linked = mob_var.get_attribute("href")
#         linked_list.append(linked)

#     for url in linked_list:
#         driver.get(url)
#         print("============================================================")
#         print("Mobile Information")
#         print(driver.find_element(By.XPATH, GET_MOBILE_NAME).text)
#         print(driver.find_element(By.XPATH, GET_MOBILE_INFO).text)
#         print(driver.find_element(By.XPATH, GET_ABOUT_PRODUCT).text)
#         print("============================================================")
    
#     # import pdb
#     # pdb.set_trace()
#     # driver.find_element(By.XPATH, NEXT_PAGE).click()
    

#     print('Search Successful...!!')
    
#     driver.close()
#     # driver.implicitly_wait(15)
# except Exception as e:
#     print('Search Failed')
#     print("ERROR" + str(e))

MODEL_NAME = '//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span'
REVIEW_STAR = '//*[@id="customer_review-R2I5U0Y5LLTHM9"]/div[2]/a[1]/i'
ALL_REVIEW_CLICK = '//*[@id="reviews-medley-footer"]/div[2]/a'
REVIEWS = '//*[@class="a-size-base review-text review-text-content"]'
REVIEW_NEXT_CLICK = '//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a'

mobile_review_dict = {}
mobile_review_list = []
try:
    driver.get(WEBSITE)
    
    loginBox = driver.find_element(By.XPATH, SEARCH_PATH)
    loginBox.send_keys(searchId)
    
    nextButton = driver.find_element(By.XPATH, SEARCH_CLICK_PATH).click()
    
    mob_vars = driver.find_elements(By.XPATH, MOBILE_HREF_PATH)
    
    linked_list = []
    for mob_var in mob_vars:
        linked = mob_var.get_attribute("href")
        linked_list.append(linked)
    
    for url in linked_list:
        driver.get(url)
        # print("============================================================")
        print("Mobile Information")
        mobile_review_dict.update({"mobile_name" : driver.find_element(By.XPATH, MODEL_NAME).text })
        
        driver.find_element(By.XPATH, ALL_REVIEW_CLICK).click()
        for i in range(17): 
            try:
                if i != 0:
                    driver.find_element(By.XPATH, REVIEW_NEXT_CLICK).click()
                    time.sleep(2)
                reviews = driver.find_elements(By.XPATH, REVIEWS)
                print(f"=====================Customer Review : {i}========================")
                for review in reviews:
                    mobile_review_dict.update({"reviews" : review.text})
            except:
                print("No next page")
        mobile_review_list.append(mobile_review_dict)
        # print("============================================================")
    print(mobile_review_list)
    
except Exception as e:
    print(e)