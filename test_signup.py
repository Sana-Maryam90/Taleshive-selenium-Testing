from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://localhost/TryingTaleshive/login.html')

test_data = [["maryam", "sana123@html.com", "abcdefgh"], ["maryam", "maryam456@html.com", "abcdefgh"]]


def test_signup(username, email, password):
    login = driver.find_element(By.CLASS_NAME, "loginpopup")
    login.click()

    time.sleep(1)
    register_link = driver.find_element(By.CLASS_NAME, "register-link")
    register_link.click()

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    email_input = driver.find_element(By.CSS_SELECTOR, ".register input[name='email']")
    password_input = driver.find_element(By.CSS_SELECTOR, ".register input[name='password']")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".register input[type='submit']")
    terms = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

    username_input.send_keys(username)
    time.sleep(1)
    email_input.send_keys(email)
    time.sleep(1)  # Wait for 1 second
    password_input.send_keys(password)
    time.sleep(1)  # Wait for 1 second
    terms.click()
    submit_button.click()

    alert_msg = driver.find_element(By.CSS_SELECTOR, ".alert.active")

    if "Email already registered" in alert_msg.text:
        print("Email already registered! SignUp failed")
        close = driver.find_element(By.CLASS_NAME, "icon-close")
        close.click()
        time.sleep(4)
    else:
        print("SignUp successful with ", username, email)


def execute_test_cases():
    for data in test_data:
        test_signup(data[0], data[1], data[2])

execute_test_cases()



