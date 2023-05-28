from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import links

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.get(links.link4)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

shoes_name = "mt2-sm css-12whm6j"
hoodies_name = "mt2-sm css-hzulvp"


sizes = soup.find_all("div", class_=shoes_name)


def find_sizes():
    for size in sizes:
        divs = size.find_all("div")
        for input in divs:
            if "disabled" not in str(input):
                print(input.text) 

def find_available_sizes():
    for size in sizes:
        divs = size.find_all("div")
        for input in divs:
            print(input.text) 

find_sizes()
print("")
find_available_sizes()