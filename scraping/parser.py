from typing import Union
from time import sleep
from abc import ABC, abstractmethod

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

import configuration.config as cfg


class Parser(ABC):
    '''
    Abstract class parser
    '''

    @abstractmethod
    def get_product_list(self, product_name: str) -> list:
        pass
    
    def get_page_content(self, 
                        product_name: str, 
                        url: str, 
                        searchbar_xpath: str,
                        scroll:bool=False,
                        scroll_timeout:Union[int,float]=0.3) -> str:
        options = Options()
        options.add_argument("window-size=1920,1080")

        with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
            #Simulate real user
            driver.get(url)
            sleep(cfg.LOAD_TIMEOUT)
            search_element = driver.find_element(By.XPATH, searchbar_xpath)
            search_element.click()
            search_element.clear()
            search_element.send_keys(product_name)
            search_element.send_keys(Keys.ENTER)
            sleep(cfg.LOAD_TIMEOUT)

            if scroll:
                for i in range(5):
                    sleep(scroll_timeout)
                    driver.execute_script(f"window.scrollTo({i * 300}, {(i+1)*300})") 
            
            content = driver.page_source

        return content