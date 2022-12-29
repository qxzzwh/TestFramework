import logging
import time
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils

class SearchFlightsResults(BaseDriver):
    log = Utils().custom_logger(loglevel=logging.WARNING)

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    
    # locaters:
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'1 Stop') or contains(text(),'2 Stops') or contains(text(),'Non Stop')]"

    def get_filter_by_1_Stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)
    
    def get_filter_by_2_Stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)
    
    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_1_Stop().click()
            self.log.warning("Selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stops":
            self.get_filter_by_2_Stop().click()
            self.log.warning("Selected flights with 2 stops")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop().click()
            self.log.warning("Selected non stop flights")
            time.sleep(2)
        else:
            print("Please provide vaild filter")