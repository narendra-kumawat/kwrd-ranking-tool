from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException 

username='info@montaigne.co'
password='montaigne@123'

# check existance by xpath
def check_exists_by_xpath(xpath):
    global driver
    print("try catch block")
    try:
        driver.find_element_by_xpath(xpath)   
    except Exception:
        print("returned False from exception",xpath)
        return False
    except:
        print("returned False from except block",xpath)
        return False    
    print("returned True",xpath)
    return True

# check existance by xpath
def check_exists_by_xpath_(xpath):
    global driver
    print("try catch block")
    try:
        driver.find_element_by_xpath(xpath)   
    except ElementNotVisibleException:
        print("returned False",xpath)
        return False    
    print("returned True",xpath)
    return True

# check existance by css selector
def check_exists_by_css_selector(css_selector):
    global driver
    print("try catch block")
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        print("returned False",css_selector)
        return False
    print("returned True",css_selector)
    return True

def checkexistancebyxpath(xpath):
    found=False
    while(found==False):        
        found=check_exists_by_xpath(xpath)   
        print("found:",found)     
    return True

def checkexistancebyxpath_(xpath):
    found=False
    while(found==False):        
        found=check_exists_by_xpath_(xpath)   
        print("found:",found)     
    return True

def checkexistancebyCSSSelector(css_selector):
    found=False
    while(found==False):        
        found=check_exists_by_css_selector(css_selector)
        print("found:",found)
    return True

# open browser
driver = webdriver.Chrome('/home/gopal/Desktop/scrapper/chromedriver')
driver.get("https://www.wincher.com/")

# login to account
if(checkexistancebyxpath('//*[@id="navigation"]/div/a[5]')):
    driver.find_element_by_xpath('//*[@id="navigation"]/div/a[5]').click()

if(checkexistancebyxpath('//*[@id="userName"]')):
    driver.find_element_by_xpath('//*[@id="userName"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_css_selector('body > div.modal.fade.in > div > form > button').click()

# time.sleep(15)  
if(checkexistancebyxpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[9]/div[2]/select/optgroup[1]/option[1]')):
    driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[9]/div[2]/select/optgroup[1]/option[1]').click()
time.sleep(15)
kwranking=driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[19]/table')
# print(kwranking.text)
with open("./files/txt/titlekwr.txt",'w') as f:
    f.write(kwranking.text)


driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[9]/div[2]/select/optgroup[1]/option[2]').click()
time.sleep(10)
kwranking=driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[19]/table')
with open("./files/txt/sizekwr.txt","w") as f:
    f.write(kwranking.text)


driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[9]/div[2]/select/optgroup[1]/option[3]').click()
time.sleep(10)
kwranking=driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[19]/table')
with open("./files/txt/sharekwr.txt","w") as f:
    f.write(kwranking.text)


driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[9]/div[2]/select/optgroup[1]/option[4]').click()
time.sleep(10)
kwranking=driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[19]/table')
with open("./files/txt/forecastkwr.txt","w") as f:
    f.write(kwranking.text)


driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[9]/div[2]/select/optgroup[1]/option[5]').click()
time.sleep(10)
kwranking=driver.find_element_by_xpath('//*[@id="top"]/div[3]/div/article/div/div/div/div/div[19]/table')
with open("./files/txt/globalkwr.txt","w") as f:
    f.write(kwranking.text)
        








