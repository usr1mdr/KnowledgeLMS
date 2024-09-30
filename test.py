from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import sqlalchemy
import requests

class Scrape():

    def __init__(self):
        self.url_array = []
        self.page_source = ''
        self.success_flag = False
    
    def test_url(self, url):
        self.url = url
        r = requests.get(url)
        self.success_flag = False
        print(type(r.status_code))
        print(r.status_code)
        if r.status_code == 200:
            print("HERE")
            self.success_flag = True
        return print("Status Code:" , str(r.status_code))
        # self.url_array.append()
        
    def scrape(self):
        counter = 0
        if self.success_flag == True:
            options = Options() 
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0")
            driver = webdriver.Chrome(options = options)
            driver.get(self.url)

            # assert "Python" in driver.title
            try:
                page_source = driver.page_source
            except Exception as e:
                print("Error: ", e)
                time.sleep(5)
                driver.close()
                return print("The page source was not accessible.")

            if (page_source):
                x = parse(page_source)
                print(x)
            
        else:
            return print("This website did not return a 200 response.")

def parse(page_source):
        parsed = []
        soup = BeautifulSoup(page_source, features="lxml")
        out = soup.find_all("a")
        for link in out:
            parsed.append(str(link.get('href')))
        return parsed

        # count = 0
        # for item in parsed:
        #     count += 1
        #     print(item)

# url = "https://matterport.com/solutions/property-marketing"
# x = Scrape()
# x.scrape(url)
        # with open ("links.txt", "w") as f:(str(elem))