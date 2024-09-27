from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import sqlalchemy

options = Options() 
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0")
driver = webdriver.Chrome(options = options)
driver.get("https://www.matterport.com")
# assert "Python" in driver.title

page_source = ''
try:
    page_source = driver.page_source
except Exception as e:
    print("Error: ", e)

soup = BeautifulSoup(page_source)
out = soup.find_all("a")

count = 0
for item in out:
    count += 1
    # print(item)
print(count)

# for item in elem:
    # print(item)

# print(elem)
time.sleep(5)
driver.close()

# with open ("links.txt", "w") as f:(str(elem))