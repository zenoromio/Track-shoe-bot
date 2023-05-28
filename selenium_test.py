from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
from selenium.webdriver.common.by import By
import links

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

shoes_name = "mt2-sm.css-12whm6j"
hoodies_name = "mt2-sm.css-hzulvp"


def find_sizes(url, class_name):
    driver.get(url)
    sizes = driver.find_element(By.CLASS_NAME, class_name)
    size_array = sizes.find_elements(By.TAG_NAME, "div")
    for i in size_array:
        label = i.find_element(By.TAG_NAME, "label")
        inputs = i.find_element(By.TAG_NAME, "input")
        print(label.get_attribute("innerHTML"))


def find_available_sizes(url, class_name):
    driver.get(url)
    sizes = driver.find_element(By.CLASS_NAME, class_name)
    size_array = sizes.find_elements(By.TAG_NAME, "div")
    for i in size_array:
        label = i.find_element(By.TAG_NAME, "label")
        inputs = i.find_element(By.TAG_NAME, "input")

        if not inputs.get_attribute("disabled"):
            print(label.get_attribute("innerHTML"))



find_available_sizes(links.link4, shoes_name)
print("")
find_sizes(links.link4, shoes_name)
driver.close()