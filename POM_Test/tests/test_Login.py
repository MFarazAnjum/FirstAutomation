import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from login_page import LoginPage


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


@allure.feature('Login Fail')
@allure.story('Login Fail')
def test_blank_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.click_login()
    assert "Required" in driver.page_source


@allure.feature('Login Fails')
@allure.story('Login Failed')
def test_wrong_credentials_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("asdfd")
    login_page.enter_password("adasd")
    login_page.click_login()
    assert "Invalid credentials" in driver.page_source


@allure.feature('Login ')
@allure.story('Login Successful')
def test_login(driver):
    login_page = LoginPage(driver)
    with open("../../Credentials.txt", "r") as file:
        lines = file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    assert "Dashboard" in driver.page_source
