from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



s = Service(r"E:\CampusX_DS\week11 - Data Analysis Process\data\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)


#select filter
link1 = driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span').click()
link2 = driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()
time.sleep(2)

#click load more at bottom

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1

while True:
    driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    print(old_height)
    print(new_height)
    
    print(counter)
    counter += 1
    
    if new_height == old_height:
        break
    
    old_height = new_height


html = driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)



while True:
    pass