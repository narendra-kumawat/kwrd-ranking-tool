from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ElementExistance as ele
import csv
import sys
import os
from selenium.webdriver.chrome.options import Options


executable_path = "/home/gopal_admin/Music/chromedriver"
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
# chrome_options.add_argument('--proxy-server=45.77.218.171:8080')
# chrome_options.add_extension('/home/gopal_admin/Downloads/Browsec-VPN-Free-and-Unlimited-VPN_v3.19.6.crx')
chrome_options.add_extension('/home/gopal_admin/Downloads/Betternet-Unlimited-Free-VPN-Proxy_v5.2.1.crx')
# chrome_options.add_extension('/home/gopal_admin/Downloads/TunnelBear-VPN_v2.0.2.crx')
# chrome_options.add_extension('/home/gopal_admin/Downloads/Hotspot-Shield-VPN-Free-Proxy-–-Unblock-Sites_v3.3.21.crx')

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
time.sleep(15)
driver.get("https://www.google.com")
# driver.quit()

keyword="africa autoclaved aerated concrete market"   #96 dmi
dmi='www.datamintelligence.com'
 
rank=0

def webBrowser(keyword):          
    if(ele.checkexistancebyxpath('//*[@id="lst-ib"]',driver)):#ele.checkexistancebyxpath('//*[@id="lst-ib"]',driver)
        driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
        time.sleep(2)
        searchPagebyPage()
        for i in range(9):
            if(ele.checkexistancebyxpath('//*[@id="pnnext"]/span[2]',driver)):
                driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
                # if(i==0):
                #     continue
                time.sleep(2)
                searchPagebyPage()
        
        
def searchPagebyPage():
    global rank
    exp=0 
    try:
        if(driver.find_element_by_xpath('//*[@id="irl_r_a"]').is_displayed()):            
            for i in range(1,10):
                try: 
                    print(i,"try block")               
                    link_selector='return document.querySelectorAll("#rso > div:nth-child(1) > div > div:nth-child('+str(i)+') > div > div > div > div > div > cite")[0].innerHTML'
                    link=driver.execute_script(link_selector)
                    # print(link)
                    if(link.find(dmi)!=-1):
                        rank+=1
                        print("-------------------------"+str(rank)+"----------------------------------") 
                        sys.exit()      
                    else:
                        rank+=1
                        print(rank,". ",link)
                        continue
                        sys.exit()
                        # driver.quit() 
                except Exception:                
                    exp+=1
                    print("Exception raised:",exp)
                    link_selector='return document.querySelectorAll("#rso > div:nth-child(3) > div > div:nth-child('+str(exp)+') > div > div > div > div > div > cite")[0].innerHTML'
                    link=driver.execute_script(link_selector)
                    # print(link)
                    if(link.find(dmi)!=-1):
                        rank+=1
                        print("-------------------------"+str(rank)+"----------------------------------") 
                        sys.exit()      
                    else:
                        rank+=1
                        print(rank,". ",link)                    
                        # driver.quit()        
    except Exception:                 
        for i in range(1,11):
            link_selector='return document.querySelectorAll("#rso > div > div > div:nth-child('+str(i)+') > div > div > div > div > div > cite")[0].innerHTML'
            link=driver.execute_script(link_selector)
            # print(link)
            if(link.find(dmi)!=-1):
                rank+=1
                print("-------------------------"+str(rank)+"----------------------------------") 
                sys.exit()      
            else:
                rank+=1
                print(rank,". ",link)
                continue
                # driver.quit()           

# def readFromCSV():
#     with open('./files/csv/titlekwr.csv',newline='') as csvfile:
#         reader=csv.DictReader(csvfile)
#         for row in reader:
#             # print(row)
#             # print(row['Title']," : ",row['path'])
#             sys.exit()

if __name__=="__main__":
    # readFromCSV()
    webBrowser(keyword)
    


# document.querySelectorAll('#mKlEF')[0].click()