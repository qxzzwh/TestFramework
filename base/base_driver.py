import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def page_scroll(self):
        page_length = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight; return pageLength")
        match = False
        while (match == False):
            last_count = page_length
            time.sleep(1)
            page_length = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight; return pageLength")
            if last_count == page_length:
                match = True
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
    
    def wait_presence_of_all_elements(self, locator_type, locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements
    
    def wait_element_to_be_clickable(self, locator_type, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
    
    def wait_text_to_be_present_in_element(self, locator_type, locator, text):
        self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

