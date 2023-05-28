from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
from selenium.webdriver.common.by import By
import links

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

#these are the class names found inside the nike.com website
shoes_name = "mt2-sm.css-12whm6j"
hoodies_man = "mt2-sm.css-hzulvp"
hoodies_woman ="mt2-sm.css-1j3x2vp"


def find_sizes(url, class_name):
    driver.get(url)
    #from url get the part with all the sizes
    sizes = driver.find_element(By.CLASS_NAME, class_name)
    #from all the sizes create an array with each size
    size_array = sizes.find_elements(By.TAG_NAME, "div")

    #print out each size
    for i in size_array:
        label = i.find_element(By.TAG_NAME, "label")
        inputs = i.find_element(By.TAG_NAME, "input")
        print(label.get_attribute("innerHTML"))


def find_available_sizes(url, class_name):
    driver.get(url)
    #from url get the part with all the sizes
    sizes = driver.find_element(By.CLASS_NAME, class_name)
    #from all the sizes create an array with each size
    size_array = sizes.find_elements(By.TAG_NAME, "div")

    #print out only available shoes
    for i in size_array:
        label = i.find_element(By.TAG_NAME, "label")
        inputs = i.find_element(By.TAG_NAME, "input")

        #the unavailable shoes are marked with "disabled" in html file
        if not inputs.get_attribute("disabled"):
            print(label.get_attribute("innerHTML"))


#when calling the function you have to pass the url and the class name as parameters
find_available_sizes(links.link9, hoodies_woman)
find_sizes(links.link9, hoodies_woman)

driver.close()