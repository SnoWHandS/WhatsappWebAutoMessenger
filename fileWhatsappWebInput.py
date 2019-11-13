import csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


#Instantiate browser object
browser = webdriver.Firefox()

#read in the input csv file with URLs
with open('inputs.csv', 'rb') as csvfile:
    data = list(csv.reader(csvfile))

#initially authorise browser with whatsapp
wait = WebDriverWait(browser, 600)
browser.get('https://web.whatsapp.com/')
#browser.maximize_window()
input()
print("QR scanned")

#For every entry in the file
for url in data:
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
    print 'accessing URL: ',str(url)[2:-2]
    browser.get(str(url)[2:-2])
    
    #Find the send button
    linkElem = browser.find_element_by_id("action-button")
    #Click the button
    linkElem.click()


    #Page goes to download option or use whatsapp web

    #wait for it to redirect
    time.sleep(2)

    #Find "use whatsapp web link"
    useWWeb = browser.find_element_by_link_text('use WhatsApp Web')
    #Click the hyperlink
    useWWeb.click()

    #wait for phone to auth
    time.sleep(8)

    sendElem = browser.find_element_by_class_name("_3M-N-")
    sendElem.click()

    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    time.sleep(2) 

def newtab(ffBrowser):
    body = ffBrowser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')

