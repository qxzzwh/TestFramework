import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightsResults
from utilities.utils import Utils

class LauchPage(BaseDriver):
    log = Utils().custom_logger()
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
    
    #locators:
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='ac_results dest_ac']//ul//li"
    SELECT_DATA_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD)
    def getGoingToField(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD)
    def getGoingToResult(self, goingto_location):
        self.wait_text_to_be_present_in_element(By.XPATH, self.GOING_TO_RESULT_LIST, goingto_location)
        return self.driver.find_elements(By.XPATH, self.GOING_TO_RESULT_LIST)
    def getDepartureDateField(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.SELECT_DATA_FIELD)
    def getAllDatesField(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ALL_DATES)
    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)
    
    def enterDepartFromField(self, depart_location):
        depart_from = self.getDepartFromField()
        depart_from.click()
        time.sleep(1)
        depart_from.send_keys(depart_location)
        depart_from.send_keys(Keys.ENTER)
    
    def enterGoingToField(self, goingto_location):
        going_to = self.getGoingToField()
        going_to.click()
        self.log.info("Clicked on going to")
        time.sleep(1)
        going_to.send_keys(goingto_location)
        self.log.info("Typed text into goingto field successfully")
        search_results = self.getGoingToResult(goingto_location)
        # print(len(search_results))
        for result in search_results:
            print(result.text)
            if goingto_location in result.text:
                result.click()
                break
    
    def enterDepartureDate(self, departure_data):
        self.getDepartureDateField().click()
    
        all_dates = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departure_data:
                date.click()
                break
    
    def clickSearchFlightButton(self):
        self.getSearchButton().click()
        time.sleep(1)
    
    def searchFlights(self, depart_location, goingto_location, departure_data):
        # Proivde departure from flights
        self.enterDepartFromField(depart_location)
        # Proivde going to flights
        self.enterGoingToField(goingto_location)
        # Select departure date
        self.enterDepartureDate(departure_data)
        # Click on flight search button
        self.clickSearchFlightButton()

        search_flight_result = SearchFlightsResults(self.driver)
        return search_flight_result