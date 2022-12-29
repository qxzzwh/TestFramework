import pytest
import softest
from pages.yatra_lauch_page import LauchPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
 
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LauchPage(self.driver)
        self.ut = Utils()
        self.log = self.ut.custom_logger()
    
    # @data(("New Delhi", "Mumbai", "22/12/2022", "1 Stop"), ("BOM", "PVG", "25/12/2022", "2 Stops"))
    @data(*Utils.read_data_from_excel("testdata\\testdata.xlsx", "testdata"))
    @unpack
    # @file_data("../testdata/testdata.json")
    def test_search_fights(self, depart_from, going_to, date, stops):
        # search flights
        search_flight_result = self.lp.searchFlights(depart_from, going_to, date)
        # To handle dynamic scroll
        search_flight_result.page_scroll()
        # Filter the flights
        search_flight_result.filter_flights_by_stop(stops)
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info("Fights in total: " + str(len(all_stops)))

        self.ut.assertListItemText(all_stops, stops)