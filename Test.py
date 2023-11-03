import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from LoginCredentials import Login
from LoginCredentials import driver
from LoginCredentials import wait

Login()  # login function from login credentials file

# Dashboard Page
driver.find_element(By.XPATH, '//button[@title = "Assign Leave"]').click()

# Leave Page landed

# Employee Name Selection
employee_name = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Type for hints")]')
employee_name.send_keys("Andrews")
exist = driver.find_element(By.XPATH, '//span[contains(text(), "Lisa  Andrews")]')
wait.until(lambda d: exist.is_displayed())
employee_name.send_keys(Keys.ARROW_DOWN)
employee_name.send_keys(Keys.ENTER)

# Leave Type Selection
leave_type = driver.find_element(By.XPATH, '//*[@class= "oxd-select-text-input"]')
leave_type.send_keys(Keys.ENTER)
leave_type.send_keys(Keys.ARROW_DOWN)
leave_type.send_keys(Keys.ENTER)

# From Date Selection
driver.find_element(By.XPATH, '//label[text() = "From Date"]/../..//input').send_keys("2023-10-30")

# To Date Selection
to_date = driver.find_element(By.XPATH, '//label[text() = "To Date"]/../..//input')
to_date.send_keys(Keys.BACKSPACE*10)
to_date.send_keys("2023-11-30")
to_date.send_keys(Keys.TAB)

# Partial Day Selection
driver.find_element(By.XPATH, '//label[contains(text(), "Partial")]/../..//div[@class = "oxd-select-wrapper"]').click()
driver.find_element(By.XPATH, '//span[text() = "All Days"]').click()

# Duration Selection
driver.find_element(By.XPATH, '//label[contains(.,"Duration")]/../..//*[div=""]').click()
driver.find_element(By.XPATH, '//span[text() = "Half Day - Morning"]').click()

# Comment Adding
driver.find_element(By.XPATH, '//label[text() = "Comments"]/../..//textarea').send_keys("Sick Leave")

# # Assign Button Pressed
# driver.find_element(By.XPATH, '//button[contains(.," Assign ")]').click()
#
# # Closed The Window
# driver.close()
# driver.quit()
