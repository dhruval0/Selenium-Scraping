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

driver = webdriver.Chrome(PATH)

searchId = "mobile"

try:
    driver.get("https://www.amazon.in/")
    loginBox = driver.find_element_by_xpath(SEARCH_PATH)
    # loginBox = driver.find_element(By.XPATH, SEARCH_PATH)
    loginBox.send_keys(searchId)

    nextButton = driver.find_elements_by_xpath(SEARCH_CLICK_PATH)
    # nextButton = driver.find_element(By.XPATH, SEARCH_CLICK_PATH)
    nextButton[0].click()

    mob_vars = driver.find_elements_by_xpath(MOBILE_HREF_PATH)
    # mob_vars = driver.find_elements(By.XPATH, MOBILE_HREF_PATH)
    
    linked_list = []
    for mob_var in mob_vars:
        linked = mob_var.get_attribute("href")
        linked_list.append(linked)
    
    for url in linked_list:
        driver.get(url)
        print("============================================================")
        print("Mobile Information")
        print(driver.find_element_by_xpath('//*[@id="productTitle"]').text)
        print("============================================================")
        
    print('Search Successful...!!')
    # driver.implicitly_wait(15)
except:
    print('Search Failed')
    
# print("sample test case started") 
#driver=webdriver.firefox()  
#driver=webdriver.ie()

# maximize the window size  
# driver.maximize_window()  

#navigate to the url
# driver.get("https://www.amazon.in/")
# search_var = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
# driver.findElement(By.xpath("//*[@id='twotabsearchtextbox']")).sendKeys(Keys.ENTER)
# print(search_var)

# driver.close()

#identify the Google search text box and enter the value  
# driver.find_element_by_xpath('//*[@class="gLFyf gsfi"]').send_keys("javatpoint")  

#click on the Google search button  
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  

#close the browser  
# print("sample test case successfully completed") 

# myvar = driver.find_element_by_class_name("ml-2").text 
# driver.findElement(By.id("main"))
# mainText = driver.find_elements_by_xpath('//*[@class="ml-2"]/span')