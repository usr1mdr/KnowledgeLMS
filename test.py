from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import sqlalchemy
import requests

class Scrape():

    def __init__(self,url):

        self.url_array = []
        self.page_source = ''
        self.success_flag = False
        r = requests.get(url)
        if r.status_code == 200:
            self.success_flag == True
        self.url_array.append()
    
    def scrape(self):

        if self.success_flag == True:
            options = Options() 
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0")
            driver = webdriver.Chrome(options = options)
            r = driver.get(self.url_array[0])

        # assert "Python" in driver.title
            try:
                self.page_source = driver.page_source
            except Exception as e:
                print("Error: ", e)

    def parse(self):
            
            parsed = []
            if self.page_source:
                soup = BeautifulSoup(self.page_source, features="lxml")
            out = soup.find_all("a")
            for link in out:
                parsed.append(str(link.get('href')))

            count = 0
            for item in parsed:
                count += 1
                print(item)

                time.sleep(5)
                driver.close()


url = "https://matterport.com/solutions/property-marketing"
x = Scrape()
x.scrape(url)
        
        # with open ("links.txt", "w") as f:(str(elem))