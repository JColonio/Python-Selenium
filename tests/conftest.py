import pytest


# used as a fixture to driver when running the tests
@pytest.fixture(scope='session')
def driver_get(request):
    from selenium import webdriver
    # web_driver = webdriver.Chrome('C:/Git/Github/Python-Selenium/drivers/chromedriver.exe')
    web_driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, 'driver', web_driver)
    yield
    web_driver.close()


# to setup the base class
@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome("C:/Git/Github/Python-Selenium/drivers/chromedriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()
