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

# chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
time.sleep(15)
driver.get("https://www.google.com")
# driver.quit()

# keyword="endoscopy devices market"   #96 dmi
dmi='www.datamintelligence.com'
 
rank=0

def webBrowser(keyword,i):  
    if(i==0):     
        if(ele.checkexistancebyxpath('//*[@id="lst-ib"]',driver)):#ele.checkexistancebyxpath('//*[@id="lst-ib"]',driver)
            driver.find_element_by_xpath('//*[@id="lst-ib"]').clear() #clear check box
            driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(keyword) #send keys
            driver.find_element_by_xpath('//*[@id="lga"]').click() # click outside of area
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click() #click on search button
    else:
        if(ele.checkexistancebyxpath('//*[@id="lst-ib"]',driver)):
            driver.find_element_by_xpath('//*[@id="lst-ib"]').clear() 
            driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(keyword)
            driver.find_element_by_xpath('//*[@id="mKlEF"]').click()
    time.sleep(2)
    #iterate over one page to another
    searchPagebyPage(keyword)
    for i in range(9):
        if(ele.checkexistancebyxpath('//*[@id="pnnext"]/span[2]',driver)):
            driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()        
            time.sleep(2)
            searchPagebyPage(keyword)
        
#operations withing the page      
def searchPagebyPage(keyword):
    global rank
    # exp=0 
    # try:
    #     if(driver.find_element_by_xpath('//*[@id="irl_r_a"]').is_displayed()):
    #         print("The report image page")            
            # for i in range(1,10):
            #     try: 
            #         print(i,"try block")               
            #         link_selector='return document.querySelectorAll("#rso > div:nth-child(1) > div > div:nth-child('+str(i)+') > div > div > div > div > div > cite")[0].innerHTML'
            #         link=driver.execute_script(link_selector)
            #         # print(link)
            #         if(link.find(dmi)!=-1):
            #             rank+=1
            #             print(rank,". ",link)
            #             print("-------------------------"+str(rank)+"----------------------------------")
            #             writeOnCSV(keyword,rank) 
            #             # break                                               
            #             # sys.exit()      
            #         else:
            #             rank+=1
            #             print(rank,". ",link)
            #             continue
            #             # sys.exit()
            #             # driver.quit() 
                    
            #     except Exception:                
            #         exp+=1
            #         print("Exception raised:",exp)
            #         link_selector='return document.querySelectorAll("#rso > div:nth-child(3) > div > div:nth-child('+str(exp)+') > div > div > div > div > div > cite")[0].innerHTML'
            #         link=driver.execute_script(link_selector)
            #         # print(link)
            #         if(link.find(dmi)!=-1):
            #             rank+=1
            #             print(rank,". ",link)
            #             print("-------------------------"+str(rank)+"----------------------------------") 
            #             writeOnCSV(keyword,rank)
            #             # break
            #             # sys.exit()      
            #         else:
            #             rank+=1
            #             print(rank,". ",link)                    
            #             # driver.quit()   
    length=driver.execute_script('return document.querySelectorAll("cite").length')
    print(length)
    for i in range(length):
        string=driver.execute_script('return document.querySelectorAll("cite")['+str(i)+'].innerHTML')
        # print(string)
        # if(string.find('http://')!=-1 or string.find('https://')!=-1 or string.find('https://www.')!=-1 or string.find('www.')!=-1 or string.find('.com')!=-1):
        print("in if block")
        length=driver.execute_script('return document.querySelectorAll(".ads-visurl").length')
        print(length)
        adlinks=[]                
        for i in range(length):
            adlinks.append(driver.execute_script('return document.querySelectorAll(".ads-visurl")['+str(i)+'].childNodes[1].innerHTML'))
            if adlinks[i]==string:
                print('Continue')
                continue                                          
        if(string.find(dmi)!=-1):
            rank+=1
            print(rank,":",string)
            print("-------------------------"+str(rank)+"----------------------------------")
            break 
        else:
            rank+=1
            print(rank,":",string)    
            
            
    # sys.exit()
    # except Exception:
    #     for i in range(1,11):
    #         link_selector='return document.querySelectorAll("#rso > div > div > div:nth-child('+str(i)+') > div > div > div > div > div > cite")[0].innerHTML'
    #         link=driver.execute_script(link_selector)
    #         # print(link)
    #         if(link.find(dmi)!=-1):
    #             rank+=1
    #             print(rank,". ",link)
    #             print("-------------------------"+str(rank)+"----------------------------------") 
    #             writeOnCSV(keyword,rank)    
    #             # break           
    #             # sys.exit()      
    #         else:
    #             rank+=1
    #             print(rank,". ",link)
    #             continue
    #             # driver.quit()     
                     
def readFromCSV():
    global rank;i=0
    with open('./files/csv/titlekwr.csv',newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            # print(row['Title']," : ",row['path'])
            print(row['Title'])
            rank=0            
            webBrowser(row['Title'],i)
            i+=1
            # driver.quit()
            sys.exit()

header=0
def writeOnCSV(keyword,rank):
    mode='a'
    if(header==0):
        mode='w'
    global header
    with open('sampledatarank.csv',mode,newline='') as csvfile:
        filednames=['Title','Rank']
        writer=csv.DictWriter(csvfile,fieldnames=filednames)
        if(header==0):
            writer.writeheader()
        writer.writerow({'Title':keyword,'Rank':rank})           

if __name__=="__main__":
    readFromCSV()
    # webBrowser(keyword)
    


#polypropylene battery separator market,/research-report/polypropylene-battery-separator-market/
# africa autoclaved aerated concrete market,/research-report/africa-autoclaved-aerated-concrete-market/
# oncolytics virus therapy market,/research-report/global-oncolytic-virus-therapy-market/