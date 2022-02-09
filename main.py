import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

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

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(PATH, options=options)

searchId = "mobile"

try:
    driver.get("https://www.amazon.in/")
    # loginBox = driver.find_element_by_xpath(SEARCH_PATH)
    loginBox = driver.find_element(By.XPATH, SEARCH_PATH)
    loginBox.send_keys(searchId)
        
    # nextButton = driver.find_elements_by_xpath(SEARCH_CLICK_PATH)
    nextButton = driver.find_element(By.XPATH, SEARCH_CLICK_PATH).click()
    # nextButton[0].click()

    # mob_vars = driver.find_elements_by_xpath(MOBILE_HREF_PATH)
    mob_vars = driver.find_elements(By.XPATH, MOBILE_HREF_PATH)

    linked_list = []
    for mob_var in mob_vars:
        linked = mob_var.get_attribute("href")
        linked_list.append(linked)

    for url in linked_list:
        driver.get(url)
        print("============================================================")
        print("Mobile Information")
        print(driver.find_element(By.XPATH, GET_MOBILE_NAME).text)
        print(driver.find_element(By.XPATH, GET_MOBILE_INFO).text)
        print(driver.find_element(By.XPATH, GET_ABOUT_PRODUCT).text)
        print("============================================================")
    
    driver.find_elements(By.XPATH,)

    print('Search Successful...!!')
    
    driver.close()
    # driver.implicitly_wait(15)
except Exception as e:
    print('Search Failed')
    print("ERROR" + str(e))