from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        chrome_service = Service(ChromeDriverManager().install())
        # 加启动配置
        chrome_options = Options()
        # 防止被各大网站识别出来使用了Selenium: (does not work for mobile emulation)
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])#禁止打印日志
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])#跟上面只能选一个
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    elif browser == "firefox":
        firefox_service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)
    elif browser == "edge":
        edge_service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=edge_service)
    else:
        pass
    
    # driver.get("https://www.yatra.com")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")