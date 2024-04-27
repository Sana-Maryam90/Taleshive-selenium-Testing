from common_functions import setup_driver
from selenium.webdriver.common.by import By
import time

driver = setup_driver()
driver.get('http://localhost/TryingTaleshive/login.html')


test_data = [["sana123@html.com", "abcd123"], ["sana456@html.com", "abcdefgh"], ["sana123@html.com", "abcdefgh"]]


def test_login(email, password):
    login = driver.find_element(By.CLASS_NAME, "loginpopup")
    login.click()

    username_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    username_input.send_keys(email)
    time.sleep(1)  # Wait for 1 second
    password_input.send_keys(password)
    time.sleep(1)  # Wait for 1 second
    submit_button.click()

    alert_msg = driver.find_element(By.CSS_SELECTOR, ".alert.active")

    print("Email: ", email, "\n", "Password: ", password)
    if alert_msg.text == "Invalid credentials! Please Login again":
        print("Invalid Credentials! Login failed")
        close = driver.find_element(By.CLASS_NAME, "icon-close")
        close.click()
        time.sleep(4)
    else:
        print("login successful")


def execute_test_cases():
    for data in test_data:
        test_login(data[0], data[1])


execute_test_cases()


