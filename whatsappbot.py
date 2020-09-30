from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath (images/video): ')

name = input('enter any no. after QR code scan is completed ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()
