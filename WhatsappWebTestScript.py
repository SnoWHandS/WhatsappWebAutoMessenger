import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


firefoxOptions = Options()
firefoxOptions.add_argument("--user-data-dir=/home/dillon/.mozilla/firefox/sosp1pw2.default")
firefoxOptions.add_argument("--incognito")

browser = webdriver.Firefox(options=firefoxOptions)

body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')


browser.get('https://api.whatsapp.com/send?phone=27840886666&text=Test%201%203')


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
time.sleep(10)

sendElem = browser.find_element_by_class_name("_3M-N-")
sendElem.click()

browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

#################################################################Repeat
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

browser.get('https://api.whatsapp.com/send?phone=27840886666&text=Test%201%203')


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
time.sleep(10)

sendElem = browser.find_element_by_class_name("_3M-N-")
sendElem.click()

browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')



