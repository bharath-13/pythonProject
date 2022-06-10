from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://themanifest.com/in/it-services/companies/bengaluru")
element_list = []
lnk = driver.find_elements(By.TAG_NAME, "a")
images = driver.find_elements(By.CLASS_NAME, "provider-logo")


for page in range(0, 10, 1):
    page_url = "https://themanifest.com/in/it-services/companies/bengaluru?page=" + str(page)
    driver.get(page_url)
    lnk = driver.find_elements(By.TAG_NAME, "a")
    for i in lnk:
        if i.get_attribute("href").__contains__("referral"):
            element_list\
                .append([i.get_attribute("href").split("?utm")[0]])

flattened_list = [value for sublist in element_list for value in sublist]
unique = list(set(flattened_list))
for i in range(len(unique)):
    print(unique[i]+"careers")
print("Total Companies listed", len(unique))
