import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

with open("Credentials.txt", "r") as file:
    lines = file.readlines()

username = lines[0].strip()
password = lines[1].strip()

class Login:
    #Username Entered
    driver.find_element(By.NAME, "username").send_keys(username)
    #Password Entered
    driver.find_element(By.NAME, "password").send_keys(password)
    #Login Button Pressed
    driver.find_element(By.XPATH, '//button[text()= " Login "]').click()
    time.sleep(10)