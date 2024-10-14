import pytest
from selenium import webdriver


# This function adds a browser option to the pytest command-line arguments
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on. Options: chrome, firefox, edge")


# This fixture uses the browser option and initializes the WebDriver accordingly
@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    # Return the WebDriver instance
    yield driver

    # Quit the browser after tests
    #driver.quit()
