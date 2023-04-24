from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from notify import notification
import os
import time

keyword = ""
refreshtimemin = 10
refreshtime = 10*60

options = Options()         
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
url = "https://old.reddit.com/r/hardwareswap/new/"
driver.get(url)
post = driver.find_elements(By.XPATH, "//a[@data-event-action='title']")
posts = set()
for title in post:
    if (title.text).startswith('[USA'):
        posts.add(title.text)
while True:
    time.sleep(refreshtime)
    driver.refresh()
    newpost = driver.find_elements(By.XPATH, "//a[@data-event-action='title']")
    newposts = set()
    for title in newpost:
        if (title.text).startswith('[USA'):
            newposts.add(title.text)
    onlynewpost = newposts.difference(posts)
    posts = newposts
    for title in onlynewpost:
        print(title)
        if keyword in title:
            os.system('notify-send "Post found! Check reddit!"')
driver.quit()
    