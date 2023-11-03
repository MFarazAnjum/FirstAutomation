import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.spicejet.com/")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH,'//input/../../*[contains(text(),"From")]').click()
driver.find_element(By.XPATH,'//*[text() = "International"]').click()
driver.find_element(By.XPATH,'//*[text() = "Dammam"]').click()

# driver.find_element(By.XPATH,'//input/../../*[contains(text(),"To")]').click()
driver.find_element(By.XPATH,'//*[text() = "International"]').click()
driver.find_element(By.XPATH,'//*[text() = "Jeddah"]').click()

wait.until(EC.element_to_be_clickable(By.XPATH("//table[@class='ui-datepicker-calendar']//tr//a[contains(@class,'ui-state-default') and contains(.,'31')]"))).click()


time.sleep(10)