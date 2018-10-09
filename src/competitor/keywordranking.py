from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ElementExistance as ele
import csv
import sys
import os
from selenium.webdriver.chrome.options import Options
import competitorList as cl


executable_path = "/home/gopal_admin/Music/chromedriver"
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
chrome_options.add_argument('--proxy-server=45.32.193.119:8123')
# chrome_options.add_extension('/home/gopal_admin/Downloads/Browsec-VPN-Free-and-Unlimited-VPN_v3.19.6.crx')
# chrome_options.add_extension('/home/gopal_admin/Downloads/chrome vpn extension/DotVPN-—-a-Better-way-to-VPN-for-Chrome_v2.3.2.crx')
# chrome_options.add_extension('/home/gopal_admin/Downloads/TunnelBear-VPN_v2.0.2.crx')
# chrome_options.add_extension('/home/gopal_admin/Downloads/Hotspot-Shield-VPN-Free-Proxy-–-Unblock-Sites_v3.3.21.crx')

# chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path=executable_path) #, chrome_options=chrome_options
# time.sleep(30)
driver.get("https://www.google.com/ncr")
# driver.quit()

# keyword="endoscopy devices market"   #96 dmi
dmi='www.datamintelligence.com'
 
# rank=0

def searchPageByPage(keyword,i,ranks):  
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
    
    for i in range(10):
        if i==0:
            ranks=searchWithinPage(keyword,ranks)
        else:
            if(ele.checkexistancebyxpath('//*[@id="pnnext"]/span[2]',driver)):
                driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
                time.sleep(2)
                ranks=searchWithinPage(keyword,ranks)        
        time.sleep(2) # need to reconsider       
        # print(rank)
        for r in range(len(ranks)):         
            if(ranks[r]!=None):
                writeOnCSV(keyword,ranks)
                break
            else:
                if(i==9):
                    
                    rank=100
                    writeOnCSV(keyword,rank)
                    break
            
#operations within the page      
def searchWithinPage(keyword,ranks):
    # global rank    
    length=driver.execute_script('return document.querySelectorAll("cite").length')
    print("Total cite Tags:",length)
    ads_numbers=driver.execute_script('return document.querySelectorAll(".ads-visurl").length')
    print("Total cite tag ads:",ads_numbers)
    adlinks=[]                
    for i in range(ads_numbers):
        adlinks.append(driver.execute_script('return document.querySelectorAll(".ads-visurl")['+str(i)+'].childNodes[1].innerHTML'))

    for i in range(length):
        string=driver.execute_script('return document.querySelectorAll("cite")['+str(i)+'].innerHTML')
        if(string.find('http://')!=-1 or string.find('https://')!=-1 or string.find('https://www.')!=-1 or string.find('www.')!=-1 or string.find('.com')!=-1 or string.find('/')!=-1 or string.find('.')!=-1 ):
            if(string.find('www.youtube.com')!=-1):
                continue
            else:            
                # print(string)
                # if(string.find('http://')!=-1 or string.find('https://')!=-1 or string.find('https://www.')!=-1 or string.find('www.')!=-1 or string.find('.com')!=-1): 
                for comp in range(len(cl.competitors)):                    
                    if(string.find(cl.competitors[comp])!=-1):
                        if(checkAds(ads_numbers,adlinks,string)!=1):
                            # rank+=1
                            cl.ranks[i]+=1
                            print(ranks[i],":",string)
                            print("-------------------------"+str(ranks[comp])+"----------------------------------")                                         
                    else:
                        if(checkAds(ads_numbers,adlinks,string)!=1):
                            # rank+=1
                            cl.ranks[i]+=1                            
                            print(ranks[i],":",string) 
                return ranks                     
            
def checkAds(ads_numbers,adlinks,string):
    for j in range(ads_numbers):
        if(adlinks[j]==string):
            print("Ads:",adlinks[j])                        
            return 1

def readFromCSV():
    # global rank;
    i=0    
    with open('../../files/csv/titlekwr.csv',newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            # print(row['Title']," : ",row['path'])
            for r in range(len(cl.ranks)):
                cl.ranks[r]=0
            print(row['Title'])
            # rank=0            
            searchPageByPage(row['Title'],i,cl.ranks)
            i+=1
            # driver.quit()
            # sys.exit()

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
        # print(rank)
        header+=1
        time.sleep(2)

if __name__=="__main__":
    readFromCSV()
    # webBrowser(keyword)
    


