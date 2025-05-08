import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield driver


@pytest.fixture
def driver_edge():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)

    yield driver

