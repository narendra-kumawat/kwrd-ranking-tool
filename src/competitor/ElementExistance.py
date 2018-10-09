from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException 
# check existance by xpath
def check_exists_by_xpath(xpath,driver):    
    print("try catch block")
    try:
        driver.find_element_by_xpath(xpath)   
    except Exception:
        print("returned False",xpath)
        return False    
    print("returned True",xpath)
    return True

# check existance by css selector
def check_exists_by_css_selector(css_selector,driver):    
    print("try catch block")
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        print("returned False",css_selector)
        return False
    print("returned True",css_selector)
    return True

def checkexistancebyxpath(xpath,driver):
    found=False
    while(found==False):        
        found=check_exists_by_xpath(xpath,driver)   
        print("found:",found)     
    return True

def checkexistancebyCSSSelector(css_selector,driver):
    found=False
    while(found==False):        
        found=check_exists_by_css_selector(css_selector,driver)
        print("found:",found)
    return True