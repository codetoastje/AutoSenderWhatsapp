import time
from selenium import webdriver
import pyautogui as pg

options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\jadth\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome('C:/Users/jadth/PycharmProjects/whatsapp/chromedriver.exe', options=options)

x = 1
people = []

for person in people:
    driver.get(f'https://web.whatsapp.com/send?phone=91{person} text&app_absent=1')

    time.sleep(5)
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    time.sleep(1)
    image_box = driver.find_element_by_xpath('//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(f"")
    time.sleep(2)
    pg.click(960, 540)
    pg.press('enter')
    time.sleep(4)
    x+=1



