from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import links

#this whole block of code will open the url with selenium and extract the html with BeautifulSoup and store it inside the "soup" variable
chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.get(links.link11)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

#these are the class names found inside the nike.com website
shoes_name = "mt2-sm css-12whm6j"
hoodies_man = "mt2-sm css-hzulvp"
hoodies_woman ="mt2-sm css-1j3x2vp"

#find all element with class name (class name must match with selected link)
sizes = soup.find("div", class_=hoodies_woman)


def find_sizes():
    #get each size
    size_array = sizes.find_all("div")

    #print out each available size
    for size in size_array:
        #the unavailable shoes are marked with "disabled" in html file
        if "disabled" not in str(size):
            print(size.text) 


def find_available_sizes():
    #get each size
    size_array = sizes.find_all("div")

    #print out each available size
    for size in size_array:
        print(size.text) 


find_sizes()
find_available_sizes()