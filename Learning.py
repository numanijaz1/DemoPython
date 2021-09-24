import time
from selenium import webdriver

#import jsonpath

#test

browser = webdriver.Chrome("C:\Test\Automation\\chromedriver.exe") #Webdriver browser
browser.get('http://172.20.22.81/OmniPCXRECORD/TenantAdmin.aspx') #Add a Website


email = browser.find_element_by_name('ctrl_TenantAdmin1$txtUserName') #enter email_id
email.send_keys('admin')

password = browser.find_element_by_name('ctrl_TenantAdmin1$txtPassword') #enter password
password.send_keys('1234567a')

sign_in = browser.find_element_by_id('ctrl_TenantAdmin1_imgBtnLogin') #press submit button
sign_in.click()

browser.set_page_load_timeout(30)

# Click on API token
browser.find_element_by_id('ctl00_ctrl_LeftMenuCloud1_hlnkAPIToken').click()

token_name = "rest_api"


browserApiTokenTable= browser.find_element_by_id('gvAPIToken')

#sizeOfTable = len(browserApiTokenTable.find_elements_by_xpath("//td[@class=' padding-left-25px token-name']/span"))
elementsofTable = browserApiTokenTable.find_elements_by_xpath("//td[@class=' padding-left-25px token-name']/span")



for i in elementsofTable:
    TokennameinTaBle = i.get_attribute('title')
    
    if(token_name.__contains__(TokennameinTaBle)):
        print(TokennameinTaBle)
        
        print(len(i.find_elements_by_xpath('/parent::td[1]')))

