from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


class Fill_form:
    def __init__(self) -> None:
        pass


    def fill(self, dict_data):
        for key, item in dict_data.items():
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeiolQbJn5d3IGXJaa9xpd5cwpM2-I-y0OfLN2l8A1Pl7TYwQ/viewform?usp=sf_link") 
            address_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_btn = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            time.sleep(2)
            address_input.send_keys(item[0])
            price_input.send_keys(item[1])
            link_input.send_keys(item[2])
            submit_btn.click()
    
    def quit(self):
        driver.quit()



            
