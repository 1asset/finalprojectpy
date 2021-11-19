from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

class Paragraphs:

    def get_url(self, coin_name):

        url = "https://coinmarketcap.com/currencies/" + coin_name + "/news/"

        options = webdriver.ChromeOptions()

        options.add_argument("--window-size=1920,1080")
        
        options.add_argument('--ignore-certificate-errors')

        options.add_argument('--incognito')

        options.add_argument('--headless')

        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

        driver.get(url)

        time.sleep(3)

        for x in range(4):

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            time.sleep(3)

            element = driver.find_element(By.XPATH, '//button[text()="Load More"]')

            driver.execute_script("arguments[0].click();", element)

            element.click()

            time.sleep(3)


        return BeautifulSoup(driver.page_source,"lxml")

    def get_p(self, coin_name):

        soup = self.get_url(coin_name)

        paraghraps = soup.find_all("div", {"class": "svowul-5 czQlor"})

        ls = []

        for i in paraghraps:

            title = i.h3.text

            body = ""

            if (i.p):

                body = i.p.text

            link = i.a.get("href")

            if (link.startswith("/headlines/news/")):

                link = "https://coinmarketcap.com" + link
            
            ls.append({"title": title, "body": body, "link": link})

        return ls

    def show_p(self, coin_name):

        soup = self.get_soup(coin_name)

        paraghraps = soup.find_all("div", {"class": "svowul-5 czQlor"})

        a = 1

        for x in paraghraps:
            if (x.p):
                print(str(a) + ")     Title : " + x.h3.text + ".\n    Link: "+ x.a.get("href"))
                print("Briefly: " + x.p.text)
                print("--------------------------------------------------------------------------------------------------")
                a+=1
