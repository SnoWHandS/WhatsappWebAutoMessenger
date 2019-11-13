import csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


#Functions-------------------------------------
def waitForElementWithID(elementID):
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, elementID)))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"

def waitForElementWithText(elementText):
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, elementText)))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"

def waitForElementWithClassName(elementClassName):
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, elementClassName)))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"

def waitForElementWithClassNameIsInvisible(elementClassName):
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.invisibility_of_element_located((By.CLASS_NAME, elementClassName)))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"




#Script-----------------------------------------

#Instantiate browser object
browser = webdriver.Firefox()

#read in the input csv file with URLs
with open('inputs.csv', 'rb') as csvfile:
    data = list(csv.reader(csvfile))

#initially authorise browser with whatsapp
wait = WebDriverWait(browser, 600)
browser.get('https://web.whatsapp.com/')
browser.maximize_window()
input()
print("QR scanned")

#For every entry in the file
for url in data:
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
    print 'accessing URL: ',str(url)[2:-2]
    browser.get(str(url)[2:-2])
    
    #Find the send button
    waitForElementWithID('action-button')
    linkElem = browser.find_element_by_id("action-button")
    #Click the button
    linkElem.click()

    #Page goes to download option or use whatsapp web

    #Find "use whatsapp web link"
    waitForElementWithText('use WhatsApp Web')
    useWWeb = browser.find_element_by_link_text('use WhatsApp Web')
    #Click the hyperlink
    useWWeb.click()

    waitForElementWithClassName("_3M-N-")
    waitForElementWithClassNameIsInvisible("-peIt")
    sendElem = browser.find_element_by_class_name("_3M-N-")
    sendElem.click()

    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    time.sleep(1)


